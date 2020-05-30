from hashlib import sha256
import rsa
import base64
import json
import time


class Block:
    def __init__(self, index, timestamp, prevHash, data):
        self.index = index
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.data = data

    def __str__(self):
        return 'Block: {0}'.format(self.return_dict())

    def return_dict(self):
        return json.dumps(self.__dict__, sort_keys=True)

    def compute_hash(self):
        """
            A function that return the hash of the block contents.
        """
        block_string = self.return_dict()
        return sha256(block_string.encode()).hexdigest()

    def compute_encryption(self, public_key):
        block_string = self.return_dict()
        cipher = rsa.encrypt(block_string.encode(), public_key)
        return base64.b64encode(cipher).decode()

    def compute_decryption(self, private_key, encrypted_message):
        text = rsa.decrypt(base64.b64decode(encrypted_message.encode()), private_key)
        return text.decode()


class GenesisBlock(Block):
    def __init__(self, index, timestamp, data):
        super().__init__(index, timestamp, "0", data)


class BlockChain:

    def __init__(self, name, encrypt=None):
        self.name = name
        self.chains = []
        self.encrypt = encrypt

    def __str__(self):
        string = 'BlockChain: {0}\n{1}'.format(self.name, self.chains) if len(self.chains) > 0 else 'BlockChain: {0}\n'.format(self.name)
        return string

    def create_genesis_block(self, genesis_block):
        genesis_block.hash = genesis_block.compute_hash()
        self.chains.append(genesis_block)

    @property
    def last_block(self):
        return self.chains[-1]

    def append(self, data):
        """
        Add a new piece of data in this blockchain.
        :param data: transaction data
        :return: True
        """
        last_block = self.last_block
        last_hash = last_block.hash
        delattr(last_block, "hash")
        new_block = Block(index=last_block.index + 1,
                          timestamp=time.time(),
                          prevHash=last_block.compute_hash(),
                          data=data)
        last_block.hash = last_hash
        new_block.hash = new_block.compute_hash()
        self.chains.append(new_block)
        if not self.is_valid:
            return False
        return True

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        # return (block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash())
        return block_hash == block.compute_hash()

    def is_valid(self):
        """
        Checks whether this blockchain is valid.
        """
        result = True
        indexFalse = None
        self.show_blocks()
        for block in self.chains:
            block_hash = block.hash
            # # remove the hash field to recompute the hash again
            # # using `compute_hash` method.
            delattr(block, "hash")
            if not self.is_valid_proof(block, block_hash):
                result = False
                indexFalse = block.index
                break

            block.hash, previous_hash = block_hash, block_hash

        return result, indexFalse

    def __len__(self):
        return len(self.chains)

    def __getitem__(self, i):
        return self.chains[i]

    def show_blocks(self, private_key=None):
        for block in self.chains:
            if self.encrypt is None:
                print(block)
            else:
                encrypted = block.compute_encryption(self.encrypt)
                if private_key is None:
                    print(encrypted)
                else:
                    try:
                        print(block.compute_decryption(private_key, encrypted))
                    except:
                        print("Wrong private key")
        print("\n")

    def show_valid_result(self):
        status, block_index = self.is_valid()
        if status:
            print("BlockChain is valid: " + str(status) + "\n")
        else:
            print("BlockChain is valid: " + str(status) + ", block at index " + str(block_index) + " is not valid\n")


if __name__ == '__main__':
    print("\n" + "#"*120)
    print("\nBlockChain without encryption for content")
    block_chain = BlockChain('CombéCoin')
    print(block_chain)
    genesis_block = GenesisBlock(0, 0, [])
    block_chain.create_genesis_block(genesis_block)

    transaction1 = ["Some data 1"]
    transaction2 = ["Some data 2"]
    block_chain.append(data=transaction1)
    block_chain.append(data=transaction2)

    block_chain.show_valid_result()

    block_chain.chains[1].data = ["some other data"]

    block_chain.show_valid_result()

    print("\n" + "#"*120)
    print("\nBlockChain with encryption for content")

    publicKey, privateKey = rsa.newkeys(2048)
    print(privateKey)

    block_chain = BlockChain('CombéCoin', encrypt=publicKey)
    print(block_chain)
    genesis_block = GenesisBlock(0, 0, [])
    block_chain.create_genesis_block(genesis_block)

    transaction1 = ["Some data 1"]
    transaction2 = ["Some data 2"]
    block_chain.append(data=transaction1)
    block_chain.append(data=transaction2)

    block_chain.show_blocks()
    block_chain.show_blocks(privateKey)
    block_chain.show_blocks()
    block_chain.show_blocks(1345435646748657878678)


