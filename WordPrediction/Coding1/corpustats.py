import argparse
import csv

import string

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='corpus text file to analyse')
    parser.add_argument('-o', '--out', metavar='PATH',
                        help='path to the file where to output the result of the analysis')
    args = parser.parse_args()

    print("Analyzing file : " + args.file)
    text = open(args.file, "r").read().lower().replace("\n", " ").translate({ord(c): " " for c in "!@#$%^&*()\"[]{};:,./<>?\|`~-=_+"})
    text = text.split(" ")
    dico = {}
    for i in text:
        try:
            dico[i] += 1
        except:
            dico[i] = 1

    if '' in dico:
        del dico['']

    if args.out:
        print('Writing output to', args.out)
        a_file = open(args.out, "w", newline='')
        writer = csv.writer(a_file)

        for key, value in dico.items():
            writer.writerow([key, value])

        a_file.close()

    else:
        print('Writing output to stdout')
        print(dico)
