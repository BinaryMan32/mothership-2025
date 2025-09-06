#!/usr/bin/env python3

import argparse
import glob
import os
import re
import sys


EPILOG = r"""Example:

%(prog)s docs/journal/posts/2025-08-18/2025-08-18.md | xclip
"""


def get_frontmatter_link_pattern(file_path):
    FRONT_MATTER_SEPARATOR = '---'
    regex = re.compile(r'linkPattern:\s+(.+)\s*')
    link_pattern = None
    with open(file_path, 'r', encoding='utf-8') as f:
        first = f.readline().strip()
        if first == FRONT_MATTER_SEPARATOR:
            while True:
                line = f.readline().strip()
                if line == FRONT_MATTER_SEPARATOR:
                    break
                match = regex.match(line)
                if match:
                    link_pattern = match.group(1)
                    break
    return link_pattern


def get_link_patterns(links_dir):
    link_patterns = []
    for file_path in glob.glob(pathname='**/*.md', root_dir=links_dir, recursive=True):
        link_pattern = get_frontmatter_link_pattern(os.path.join(links_dir, file_path))
        if link_pattern:
            file_name = os.path.basename(file_path)
            link_patterns.append((link_pattern, file_name))
    return link_patterns


def replace_link_patterns(content, link_patterns):
    for (link_pattern, file_path) in link_patterns:
        pattern = re.compile(fr'(?<!\[)({link_pattern})(?!\])')
        (content, count) = pattern.subn(fr'[\1]({file_path})', content)
        if count > 0:
            print(f"Added {count} links to {file_path}", file=sys.stderr)
    return content


def default_docs_dir():
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(scripts_dir)
    return os.path.join(root_dir, 'docs')


class CustomHelpFormatter(argparse.RawDescriptionHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    pass


def main():
    parser = argparse.ArgumentParser(
        description='Add links to a markdown file',
        formatter_class=CustomHelpFormatter,
        epilog=EPILOG
    )
    parser.add_argument(
        'input', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
        help='Input markdown file',
    )
    parser.add_argument(
        '--links-dir', default=default_docs_dir(),
        help='directory containing markdown files to link'
    )
    args = parser.parse_args()

    link_patterns = get_link_patterns(args.links_dir)
    print("Link Patterns:", file=sys.stderr)
    for (link_pattern, file_path) in link_patterns:
        print(f"{link_pattern} -> {file_path}", file=sys.stderr)

    content = args.input.read()
    content = replace_link_patterns(content, link_patterns)
    sys.stdout.write(content)

if __name__ == '__main__':
    exit(main())
