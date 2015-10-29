# construct the polytree

def construct_ptree(labelset_list):
    """
    labelset_list: list of labelset in order

    Return:
    ---------
    list of tuples: the edges(where node are the index of the labelset in labelset_list)
    """
    tree = [] # for the ith element, it stores the ith labelset's parent node ids
    for i in xrange(len(labelset_list)):
        tree.append([])

    for new_node_id, new_node in enumerate(labelset_list):
        for cur_node_id in xrange(new_node_id):
            if labelset_list[cur_node_id].intersection(new_node):
                tree[new_node_id].append(cur_node_id)
    return tree
