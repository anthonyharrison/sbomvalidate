# SBOMValidate

The SBOMValidate is a free, open source tool to validate a SBOM (Software Bill of Materials) against the specifications for
[SPDX](https://www.spdx.org) and [CycloneDX](https://www.cyclonedx.org).

It is intended to be used as part of a continuous integration system to ensure only valid SBOMs are processed.

## Installation

To install use the following command:

`pip install sbomvalidate`

Alternatively, just clone the repo and install dependencies using the following command:

`pip install -U -r requirements.txt`

The tool requires Python 3 (3.7+). It is recommended to use a virtual python environment especially
if you are using different versions of python. `virtualenv` is a tool for setting up virtual python environments which
allows you to have all the dependencies for the tool set up in a single environment, or have different environments set
up for testing using different versions of Python.

## Usage

```bash
usage: sbomvalidate [-h] [-i INPUT_FILE] [--debug] [-V]

SBOMvalidate validates a SBOM.

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit

Input:
  -i INPUT_FILE, --input-file INPUT_FILE
                        Name of SBOM file
  --debug               add debug information
```
						
## Operation

The `--input-file` option is used to specify the SBOM to be processed. The format of the SBOM is determined according to
the following filename conventions.

| SBOM      | Format    | Filename extension |
| --------- | --------- |--------------------|
| SPDX      | TagValue  | .spdx              |
| SPDX      | JSON      | .spdx.json         |
| SPDX      | YAML      | .spdx.yaml         |
| SPDX      | YAML      | .spdx.yml          |
| SPDX      | XML       | .spdx.xml          |
| SPDX      | RDF       | .spdx.rdf          |
| CycloneDX | JSON      | .json              |
| CycloneDX | XML       | .xml               |

For CycloneDX SBOMs, versions 1.3, 1.4. 1.5 and 1.6 are supported; for SPDX SBOMs, versions 2.2 and 2.3 are supported.

The `--debug` option is used to provide more information on the validation process. The default is for no information to be reported.

## Return Values

The return value indicates the validity of the SBOM

0 indicates that the SBOM has been validated
1 indicates that the SBOM failed to validate

Example usage

```bash
sbomvalidate -i <goodsbomfilename>
echo $?
0
sbomvalidate -i <badsbomfilename>
echo $?
1
```

## Licence

Licenced under the Apache 2.0 Licence.

## Limitations

The validation of SPDX SBOMs in RDF, TagValue and XML formats is limited to detecting the presence of key tags in the document.

## Feedback and Contributions

Bugs and feature requests can be made via GitHub Issues.