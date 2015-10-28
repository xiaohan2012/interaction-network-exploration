from collections import Counter

TAG_PREFIX = 'topics/companies/'

def count_tags(edge_cursor):
    total_tag_count = 0
    tag_freq = Counter()
    
    # Company frequency
    for a in edge_cursor:
        total_tag_count += len(a['tags'])
        for tag in a['tags']:
            if tag.startswith(TAG_PREFIX):
                tag_freq[tag] += 1
    return tag_freq

def compactize_edges_by_tags(edge_cursor, tag_set):
    edges = []
    for e in edge_cursor:
        shared_tags = set(e['tags']).intersection(tag_set)
        if shared_tags:
            edges.append({'tags': shared_tags,
                          'url': e['url'],
                          'title': e['title'],
                          'publish_time': e['publish_time']})
    return edges
