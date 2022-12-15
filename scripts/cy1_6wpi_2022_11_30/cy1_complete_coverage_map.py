"""
Produces a complete coverage map of CY1 genome sequence taking into
account all reads that align to CY1 genome sequence.
"""

import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np


def is_cy1_hit(hit):
    return hit.description[0]['title'].lower() == 'cy1'


blast_output2_file_path = '/Users/philip/epi2melabs-data/2022-11-30/blastn.json'

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

searches_with_only_one_cy1_hit = list(filter(
    lambda search : search.num_hits == 1 and is_cy1_hit(search.hits[0]),
    searches,
))
print(
    'Seaches with only one CY1 hit: '
    + str(len(searches_with_only_one_cy1_hit))
)

assert len(searches_with_hits) == len(searches_with_only_one_cy1_hit)
print('All hits are CY1 and all searches have at most one hit.')

# print blank line
print()

covered_cy1_positions = []
for search in searches_with_only_one_cy1_hit:
    hit = search.hits[0]
    covered_cy1_positions.extend(hit.covered_hit_positions)

fig, ax = plt.subplots()

cy1_length = 2692
bins = [i + 0.5 for i in range(0, cy1_length + 1)]

print('Producing histogram plot... (This might take a little bit.)')
ax.hist(covered_cy1_positions, bins=bins)

print('Showing histogram plot.')
plt.show()
