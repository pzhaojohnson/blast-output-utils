"""
Produces a coverage map of CY1 genome sequence taking into account all
hsps with "Plus" hit strands.
"""

import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np


def is_cy1_hit(hit):
    return hit.description[0]['title'].lower() == 'cy1'


def has_plus_hit_strand(hsp):
    return hsp.has_plus_hit_strand()


def get_covered_hit_positions(hsps):
    """Returns a set of the covered hit positions given a list of hsps.
    """
    covered_hit_positions = set()
    for hsp in hsps:
        covered_hit_positions.update(hsp.covered_hit_positions)
    return covered_hit_positions


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

hits = list(map(lambda search : search.hits[0], searches_with_hits))

# print blank line
print()

covered_cy1_positions = []
for hit in hits:
    hsps_with_plus_hit_strands = list(filter(has_plus_hit_strand, hit.hsps))
    ps = get_covered_hit_positions(hsps_with_plus_hit_strands)
    covered_cy1_positions.extend(ps)

fig, ax = plt.subplots()

cy1_length = 2692
bins = [i + 0.5 for i in range(0, cy1_length + 1)]

print('Producing histogram plot... (This might take a little bit.)')
ax.hist(covered_cy1_positions, bins=bins, color='black')

print('Showing histogram plot.')
plt.show()
