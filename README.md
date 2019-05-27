# UBC Spider

Spider that performs search queries by faculty name on the [UBC Faculty Directory](https://directory.ubc.ca/index.cfm?).

Returns position, department and gender on console.

To change names to search, modify array `NAMES` in `spider.py`. Assumes names are in `lastname firstname middlename` order.

## Prerequisites

[Python3](https://wiki.python.org/moin/BeginnersGuide/Download)

## Setup

1. Git clone repository.
2. Navigate into repository and create venv:
    `pyvenv venv`
3. Activate venv:
    `source venv/bin/activate`
4. Install dependencies:
    `pip install -r requirements.txt`
5. To run spider:
    `python3 spider.py`