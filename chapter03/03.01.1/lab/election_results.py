"""
A monstrosity of an election results script. Calculates total votes for
races and candidates, and determines if there is a winner in each race.

This module bundles together way too much functionality and is near impossible 
to test, beyond eye-balling results.

USAGE:

    python election_results.py

OUTPUT:

    summary_results.csv

"""
import os
import csv
import ssl
import urllib.request
import urllib

from operator import itemgetter
from collections import defaultdict
from os.path import dirname, join

###-------------------------------------------------------------------------###

# Download CSV of fake Virginia election results to root of project
url = "http://docs.google.com/spreadsheet/pub?key=0AhhC0IWaObRqdGFkUW1kUmp2ZlZjUjdTYV9lNFJ5RHc&output=csv"

this_folder = os.path.dirname(__file__)
result_file = join(this_folder, 'fake_va_elec_results.csv')

context = ssl._create_unverified_context()

###-------------------------------------------------------------------------###
# TODO: Old API
#response = urllib.urlopen(url, context=context)

response = urllib.request.urlopen(url, context=context)

###-------------------------------------------------------------------------###
# Create reader for ingesting CSV as array of dicts
reader = csv.DictReader(open(filename, 'rb'))

# Use defaultdict to automatically create non-existent keys with an empty dictionary as the default value.
# See https://pydocs2cn.readthedocs.org/en/latest/library/collections.html#defaultdict-objects
results = defaultdict(dict)

# Initial data clean-up
for row in reader:
    print(row)
    