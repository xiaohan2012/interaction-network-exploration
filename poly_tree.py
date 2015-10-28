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

    frontier_node_ids = set()
    
    for new_node_id, new_node in enumerate(labelset_list):
        print(new_node_id, len(frontier_node_ids))
        # iterate through the current frontier list
        # and find all possible parent for the new_node
        frontiers_to_be_removed = []
        for f_node_id in frontier_node_ids:
            node_id_queue = [f_node_id]
            while len(node_id_queue) > 0:
                print(len(node_id_queue))
                cur_node_id = node_id_queue.pop(0)
                if labelset_list[cur_node_id].intersection(new_node):
                    tree[new_node_id].append(cur_node_id)
                    if cur_node_id in frontier_node_ids:
                        frontiers_to_be_removed.append(cur_node_id)
                    break
                else:
                    for parent_id in tree[cur_node_id]:
                        node_id_queue.append(parent_id)
        frontier_node_ids -= set(frontiers_to_be_removed)
        frontier_node_ids.add(new_node_id)
    # edges = []
    # for node_id, parent_ids in enumerate(tree):
    #     for p_id in parent_ids:
    #         edges.append((p_id, node_id))
    # return edges
    return tree
