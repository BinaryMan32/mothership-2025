#!/usr/bin/env python3

import argparse
import json
import os
import re
import sys


EPILOG = r"""Example:

%(prog)s transcripts/2025-09-10.txt | xclip
"""


def get_name_mapping(name_mapping_path):
    with open(name_mapping_path, 'r') as f:
        return json.load(f)


def replace_names(file_in, file_out, name_mapping):

    long_regex = re.compile('^\\[(' + '|'.join([e['person'][0] for e in name_mapping]) + ')\\]')
    long_names = {e['person'][0]: e['character']['long'] for e in name_mapping}

    short_regex = re.compile('\\b(' + '|'.join([p for e in name_mapping for p in e['person']]) + ')\\b')
    short_names = {p: e['character']['short'] for e in name_mapping for p in e['person']}

    stats = {
        **{e['character']['long']: {e['person'][0]: 0} for e in name_mapping},
        **{e['character']['short']: {p: 0 for p in e['person']} for e in name_mapping}
    }
    def replacer(mapping):
        def replace(match):
            name_in = match.group(1)
            name_out = mapping[name_in]
            stats[name_out][name_in] += 1
            before = match.string[match.start(0):match.start(1)]
            after = match.string[match.end(1):match.end(0)]
            return before + name_out + after
        return replace

    for line_in in file_in:
        if line_in.startswith('['):
            line_out, n = long_regex.subn(replacer(long_names), line_in)
            if n != 1:
                raise ValueError(f'Unable to replace name in {line_in!r}')
        else:
            line_out = short_regex.sub(replacer(short_names), line_in)
        file_out.write(line_out)

    print('Replacement stats:', file=sys.stderr)
    for name_out, names_in in sorted(stats.items()):
        names_in_stats = ' '.join([f'{name_in!r}({count})' for name_in, count in sorted(names_in.items())])
        print(f'{name_out}: {names_in_stats}', file=sys.stderr)


def default_name_mapping():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(scripts_dir)
    return os.path.join(root_dir, 'name-mapping.json')


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


def main():
    parser = argparse.ArgumentParser(
        description='Replace real names with character names',
        formatter_class=CustomHelpFormatter,
        epilog=EPILOG
    )
    parser.add_argument(
        'input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='Input transcript file',
    )
    parser.add_argument(
        'output', nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help='Output transcript file',
    )
    parser.add_argument(
        '--name-mapping', default=default_name_mapping(),
        help='file containing mapping from real names to character names'
    )
    args = parser.parse_args()

    name_mapping = get_name_mapping(args.name_mapping)
    replace_names(args.input, args.output, name_mapping)

if __name__ == '__main__':
    exit(main())
