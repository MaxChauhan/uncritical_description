#! /usr/bin/env python
"""
Extracts the info from a

"""
import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('-i', '--input',
                        metavar='input',
                        default='test_event.tsv',
                        help='Tab separated input file')

    args = parser.parse_args()

    with open(args.input) as infile:
        eventreader = csv.reader(infile, delimiter='\t')
        for row in eventreader:

            out = (f'{row[1]}\n\n'
                   f'Location: {row[2]}\n\n'
                   f'Description: {row[3]}\n\n'
                   f'Date/Time: {row[4]}\n\n'
                   f'Do you agree to follow all required COVID-19 safety protocols, as outlined here: {row[5]}'
                   f'How do you plan to make your project safe for participants/spectators regarding COVID-19 (i.e. '
                   f'distancing, sanitizer provided, not applicable for your project, etc.): {row[6]}\n\n'
                   f'Are there any accessibility challenges that participants should be aware of: {row[7]}\n\n'
                   f'Is registration required: {row[8]}\n\n'
                   f'Public contact: {row[9]}\n'
                   f'Private contact: {row[10]} {row[11]}\n\n'
                   f'Grant funding needed: {row[12]}\n\n'
                   f'Is grant funding required for this to happen: {row[13]}\n\n'
                   f'Placement help: {row[14]}\n\n'
                   f'Space for other projects: {row[15]}\n\n'
                   f'Other: {row[16]}\n'
                 )
            print(out)

if __name__ == "__main__":
    main()

