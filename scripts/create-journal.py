#!/usr/bin/env python3

import argparse
import datetime
import os
import pathlib
import string


def read_template(name):
    template_path = pathlib.Path(__file__).with_name(name)
    with open(template_path) as f:
        return string.Template(f.read())


def write_journal(template: string.Template, journal_date: datetime.date):
    date_string = journal_date.isoformat()
    journal_dir = os.path.join('docs', 'journal', 'posts', f'{date_string}')
    os.makedirs(journal_dir, exist_ok=True)
    journal_path = os.path.join(journal_dir, f'{date_string}.md')
    if os.path.exists(journal_path):
        print(f'File "{journal_path}" exists, aborting')
        exit(1)
    print(f'Creating "{journal_path}"')
    with open(journal_path, 'w') as f:
        f.write(template.substitute(DATE=date_string))


def main():
    parser = argparse.ArgumentParser(description='Create a new journal entry')
    parser.add_argument(
        '-d', '--date',
        type=datetime.date.fromisoformat,
        metavar='YYYY-MM-DD',
        help='Date of the journal entry',
        default=datetime.date.today()
    )
    args = parser.parse_args()

    template_name = f'journal-template.md'
    template = read_template(template_name)

    write_journal(template, args.date)


if __name__ == '__main__':
    exit(main())
