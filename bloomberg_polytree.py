from pprint import pprint
from util import count_tags, compactize_edges_by_tags
from poly_tree import construct_ptree

def main():
    N_TOP_TAGs = 50
    
    from db import conn
    articles = conn['bloomberg'].articles
    tag_freq = count_tags(articles.find())
    target_tags = set([k for k, _ in tag_freq.most_common(N_TOP_TAGs)])
    compact_edges = compactize_edges_by_tags(articles.find(), target_tags)
    
    pprint(compact_edges[:10])
    print(sum([1 for e in compact_edges if len(e['tags']) > 1]))
    pprint(len(compact_edges))
    
    sorted_compact_edges = sorted(compact_edges, key=lambda item: item['publish_time'])
    tagset_list = [e['tags'] for e in sorted_compact_edges]
    tree = construct_ptree(tagset_list)
    

if __name__ == '__main__':
    main()
