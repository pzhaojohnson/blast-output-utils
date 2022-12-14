import json

from wrappers.blast_output2.BlastOutput2Wrapper import BlastOutput2Wrapper

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np


# change depending on the blast output to analyze
#blast_output2_file_path = '/Users/philip/epi2melabs-data/2022-11-30/blastn.json'
blast_output2_file_path = '/Users/philip/Dropbox/UMD/PhD/nanopore/2022-07-01/analysis/blastn.json'

# for the virus genome that reads were aligned to
#virus_genome_length = 2692
virus_genome_length = 2983

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

searches_with_one_hit = list(filter(
    lambda search : search.num_hits == 1,
    searches,
))
print('Searches with one hit: ' + str(len(searches_with_one_hit)))

# should be equal if only one reference sequence was used
assert len(searches_with_one_hit) == len(searches_with_hits)
print('No searches have multiple hits.')

# print blank line
print()

hits = list(map(lambda search : search.hits[0], searches_with_hits))

hits_with_one_hsp = list(filter(
    lambda hit : len(hit.hsps) == 1,
    hits,
))
print('Hits with one hsp: ' + str(len(hits_with_one_hsp)))

hits_with_two_hsps = list(filter(
    lambda hit : len(hit.hsps) == 2,
    hits,
))
print('Hits with two hsps: ' + str(len(hits_with_two_hsps)))

hits_with_more_than_two_hsps = list(filter(
    lambda hit : len(hit.hsps) > 2,
    hits,
))
print(
    'Hits with more than two hsps: '
    + str(len(hits_with_more_than_two_hsps))
)

hits_with_multiple_hsps = hits_with_two_hsps + hits_with_more_than_two_hsps
print('Hits with multiple hsps: ' + str(len(hits_with_multiple_hsps)))

# print blank line
print()

junctions = []
for hit in hits_with_multiple_hsps:
    hsps_sorted_by_hit_from = hit.hsps_sorted_by_hit_from
    for i in range(len(hsps_sorted_by_hit_from) - 1):
        x = hsps_sorted_by_hit_from[i].hit_to
        y = hsps_sorted_by_hit_from[i + 1].hit_from
        junctions.append([x, y])

print('Junctions: ' + str(len(junctions)))

"""
xs = list(map(lambda junction : junction[0], junctions))
ys = list(map(lambda junction : junction[1], junctions))

fig, ax = plt.subplots()

bins = [i + 0.5 for i in range(virus_genome_length + 1)]

ax.hist2d(xs, ys, bins=bins, cmin=1, cmap=mpl.cm.Blues)
#ax.hexbin(xs, ys, gridsize=2692, mincnt=1, cmap=mpl.cm.Blues)
#ax.hexbin(xs, ys, gridsize=53.84, mincnt=1, cmap=mpl.cm.Blues)

#ax.set(xlim=(1, virus_genome_length), ylim=(1, virus_genome_length))
ax.set(xlim=(665, 675), ylim=(2408, 2418))

plt.show()
"""

# print blank line
print()

di_searches = []
for search in searches:
    if search.num_hits > 0:
        assert search.num_hits == 1 # none should have multiple hits
        hit = search.hits[0]
        if len(hit.hsps) == 2:
            hsps = hit.hsps_sorted_by_hit_from
            if hsps[0].hit_to == 671 and hsps[1].hit_from == 2703:
                di_searches.append(search)
print('DI-RNA searches: ' + str(len(di_searches)))

di_hits = [search.hits[0] for search in di_searches]

"""
di_hits = []
for hit in hits_with_two_hsps:
    hsps = hit.hsps_sorted_by_hit_from
    if hsps[0].hit_to == 670 and hsps[1].hit_from == 2692:
        di_hits.append(hit)
print('DI-RNA hits: ' + str(len(di_hits)))
"""

# print blank line
#print()
#print(di_searches[1].query_title)


"""
query_to_minus_from = []
for hit in di_hits:
    hsps = hit.hsps_sorted_by_hit_from
    query_to_minus_from.append(hsps[1].query_from - hsps[0].query_to)

fig, ax = plt.subplots()

ax.hist(
    query_to_minus_from,
    bins=[-10.5, -9.5, -8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5],
)

ax.set(
    xlim=(-10.5, 0.5),
    xticks=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0],
)

plt.show()
"""

# print blank line
print()

bases7 = []
for hit in di_hits:
    hsp = hit.hsps_sorted_by_hit_from[0]
    qseq = hsp.hsp['qseq']
    bases7.append(qseq[-7:])
for bs in bases7:
    print(bs)
