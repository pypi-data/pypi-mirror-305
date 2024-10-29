## NOTICE

This is the new home of "pyShodan".

##

pyShodan (https://shanewilliamscott.com)
==
[![Python package](https://github.com/Hackman238/pyShodan/actions/workflows/master.yml/badge.svg)](https://github.com/Hackman238/pyShodan/actions/workflows/master.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/Hackman238/pyShodan/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/Hackman238/pyShodan?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/5e1845e74fd98a901aa4/maintainability)](https://codeclimate.com/github/Hackman238/pyShodan/maintainability)

# About pyShodan
Python 3 script for interacting with Shodan API. Has three modes of operation: making an API query for a search term, a single IP address, or for a list of IP addresses in a .txt file.

## Installation
```
pip3 install pyShodan
```

## Recommended Python Version
Tested on Python 3.6+.

## Dependencies
* Shodan (pip3 install shodan)

Output is printed to stdout as well as CSV files in the script directory.

## Credits
Based on fork from https://github.com/GoVanguard/pyExploitDb by Shane Scott.
