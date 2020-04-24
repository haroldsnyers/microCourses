import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='corpus text file to analyse')
    parser.add_argument('-o', '--out', metavar='PATH', help='path to the file where to output the result of the analysis')
    args = parser.parse_args()

    print('Analysing', args.file)
    if args.out:
        print('Writing output to', args.out)
    else:
        print('Writing output to stdout')