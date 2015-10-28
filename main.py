import matplotlib as mpl
mpl.use('Agg')

from collections import Counter, defaultdict
from pprint import pprint
from datetime import datetime

import numpy as np
from matplotlib import pyplot as plt
from pymongo import MongoClient

TAG_PREFIX = 'topics/companies/'

db = MongoClient()['bloomberg']

total_tag_count = 0
tag_freq = Counter()

# Company frequency
for a in db.articles.find():
    total_tag_count += len(a['tags'])
    for tag in a['tags']:
        if tag.startswith(TAG_PREFIX):
            tag_freq[tag] += 1

print('-' * 100)

print("Top 100 companies ranked by frequency:")
print('-' * 100)
pprint(tag_freq.most_common(100))

tags_to_be_considered = set([k for k, _ in tag_freq.most_common(10)])

datetime_by_tags = defaultdict(list)

# Company stacked area graph
for a in db.articles.find():
    day_of_year = datetime.fromtimestamp(a['publish_time']).timetuple().tm_yday
    
    for tag in a['tags']:
        if tag in tags_to_be_considered:
            datetime_by_tags[tag].append(day_of_year / 30)

rows = np.zeros((len(tags_to_be_considered), 12))

id2tag = {}
for i, (tag, months) in enumerate(datetime_by_tags.items()):
    id2tag[i] = tag
    for month in months:
        rows[i][month] += 1

rows = np.cumsum(rows, axis=0)

# PLOT

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(12)

colors = ['#a6cee3', '#1f78b4', '#b2df8a', '#33a02c', '#fb9a99',
          '#e31a1c', '#fdbf6f', '#ff7f00', '#cab2d6', '#6a3d9a']

for i in xrange(len(tags_to_be_considered)):
    if i == 0:
        y1 = np.zeros(x.shape)
    else:
        y1 = rows[i-1, :]

    y2 = rows[i, :]

    ax.fill_between(x, y1, y2,
                    facecolor=colors[i], alpha=.7)
    ax.text(2.5, (y1[3]+y2[3]) / 2, id2tag[i].split('/')[-1])

print(rows)
plt.savefig('/cs/fs/home/hxiao/public_html/company_frequency_stream.png')
