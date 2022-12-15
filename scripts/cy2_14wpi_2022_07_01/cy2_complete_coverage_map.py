"""
Produces a complete coverage map of CY2 genome sequence taking into
account all reads that align to CY2 genome sequence.
"""

import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np


def is_cy2_hit(hit):
    return hit.description[0]['title'].lower() == 'cy2'


blast_output2_file_path = '/Users/philip/Dropbox/UMD/PhD/nanopore/2022-07-01/analysis/blastn.json'

with open(blast_output2_file_path, 'r') as f:
    blast_output2 = BlastOutput2Wrapper(json.loads(f.read()))

# print blank line
print()

reports = blast_output2.reports
results_list = [report.results for report in reports]
searches = [results.search for results in results_list]

searches_with_hits = list(filter(
    lambda search : search.num_hits > 0,
    searches,
))
print('Searches with at least one hit: ' + str(len(searches_with_hits)))

searches_with_only_one_cy2_hit = list(filter(
    lambda search : search.num_hits == 1 and is_cy2_hit(search.hits[0]),
    searches,
))
print(
    'Seaches with only one CY2 hit: '
    + str(len(searches_with_only_one_cy2_hit))
)

assert len(searches_with_hits) == len(searches_with_only_one_cy2_hit)
print('All hits are CY2 and all searches have at most one hit.')

# print blank line
print()

covered_cy2_positions = []
for search in searches_with_only_one_cy2_hit:
    hit = search.hits[0]
    covered_cy2_positions.extend(hit.covered_hit_positions)

fig, ax = plt.subplots()

cy2_length = 2983
bins = [i + 0.5 for i in range(0, cy2_length + 1)]

print('Producing histogram plot... (This might take a little bit.)')
ax.hist(covered_cy2_positions, bins=bins, color='black')

print('Showing histogram plot.')
plt.show()
