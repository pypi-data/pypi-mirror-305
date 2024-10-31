# PO2Dataset

[![PyPI version](https://badge.fury.io/py/po2dataset.svg)](https://badge.fury.io/py/po2dataset)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/po2dataset.svg)](https://pypi.python.org/pypi/po2dataset/)
[![check](https://github.com/urtzai/po2dataset/actions/workflows/python-test.yml/badge.svg)](https://github.com/urtzai/po2dataset/actions/workflows/python-test.yml)

**po2dataset** is a python tool to extract sentences from po files and create language datasets for machine translation.

This command line tool is intended to create dataset packages suitable for [Argos Train](https://github.com/argosopentech/argos-train).

## How to install

### From pip

```bash
pip install po2dataset
```

### Manual installation

Create a virtual environment using [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)

```bash
git clone https://github.com/itzune/po2dataset.git
virtualenv po2dataset
cd po2dataset
source ./bin/activate
```

## Quick start guide

### Create Argos Train suitable dataset

```bash
po2dataset path/to/yourfile.po --name "MyProject" --source_code en --target_code eu --ref "Some reference information of the project"
```

Where:

- `name`: The name of the project
- `source_code`: Source language code ([ISO 639](https://en.wikipedia.org/wiki/ISO_639))
- `target_code`: Target language code ([ISO 639](https://en.wikipedia.org/wiki/ISO_639))
- `ref`: Some reference information of the project

Optional arguments:

- `format`: Extension name of the zip file (default **argosdata**)
- `license`: License to add into the package (default [**CC0**](https://creativecommons.org/publicdomain/zero/1.0/)). Options are: CC0, CC-BY, CC-BY-SA

### Usage Examples

#### Basic Dataset Creation

To create a dataset from a .po file for an English-Basque translation project, run:

```bash
po2dataset path/to/yourfile.po --name "MyProject" --source_code en --target_code eu --ref "Translation dataset for project X"
```

#### Specifying Format and License

For different file format and license, use:

```bash
po2dataset path/to/yourfile.po --name "MyProject" --source_code en --target_code eu --format "zip" --license "CC-BY"
```

These commands create language dataset packages, with zip file format and CC-BY licensing options.

## Support

Should you experience any issues do not hesistate to post an issue or contribute in this project pulling requests.
