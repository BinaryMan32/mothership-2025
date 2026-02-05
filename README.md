# Mothership 2025

Published at <https://binaryman32.github.io/mothership-2025>

Documentation is built as a static site using [mkdocs][] and the [material][mkdocs-material] theme.
If you want to do something that it doesn't support, check the [mkdocs catalog][mkdocs-catalog] for plugins.

[mkdocs]: https://www.mkdocs.org/
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material
[mkdocs-catalog]: https://github.com/mkdocs/catalog

## Local Preview with Virtualenv

Create virtualenv:

```sh
python3 -m venv .venv/ && source .venv/bin/activate && pip3 install -r requirements.txt
```

Preview:

```sh
mkdocs serve --livereload
```

## Local Preview with Docker

```sh
./preview-docker.sh
```

## Pre-commit

Use `pre-commit` to find broken links before committing.

```sh
sudo apt install pre-commit
pre-commit install
```

## Renaming Images

Command to rename all `*.png` files to:

- change all characters to lower case
- add leading `0` to files starting with a non-zero digit
- replace all sequences of spaces and `-` with a single `-`

```sh
rename -e 'y/A-Z/a-z/;' -e 's/^([1-9])[ -]/0\1-/;' -e 's/[ -]+/-/g;' *.(png|jpg)
```

Requires `rename` package:

```sh
sudo apt install rename
```

## Resizing Images

```sh
mkdir reduced
for x in full/*.(png|jpg); do convert "$x" -resize '800x800>' reduced/$(basename "$x"); done
```

## Embedding All Images

Fills the clipboard with text to embed all images in the current directory.
Paste into a scratch file and cut and paste as you add captions.

```sh
for img in *.(png|jpg); do
echo "\![](./${img})
/// caption
///
"
done | xclip
```
