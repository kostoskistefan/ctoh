# CToH [![version](https://img.shields.io/badge/version-1.0-red.svg)](https://semver.org)

CToH is a very simple Python script that takes a C/C++ source file and generates a corresponding header file. 

## Quick note
This script only generates the functions from the source file. You'll still need to fix import errors and possible global variables that you might want to use.

## Requirements
* Any version of Python3

## Installation
Clone the repository using `git clone https://github.com/kostoskistefan/ctoh.git`

Change to the cloned directory `cd ctoh`

Run the script `python ctoh.py [OPTIONS]`

## Usage options
```
usage: ctoh.py [-h] -i INPUT [-s] [-o OUTPUT]

Create header file from a source file

required arguments:
  -i INPUT, --input INPUT
                        Path to the source file

optional arguments:
  -h, --help            show this help message and exit
  -s, --sort            Sort the functions in the header file by length
  -o OUTPUT, --output OUTPUT
                        Specify the full output path and filename for the generated header file
```

## Example usage
Parse the source file `/home/user/source.c` and generate the header file in `/home/user/another_directory/` with the name `new_name.h`.

`python ctoh.py -i /home/user/source.c -o /home/user/another_directory/new_name.h`