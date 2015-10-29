from nose.tools import assert_equal
from poly_tree import construct_ptree

def test_construct_ptree():
    A, B, C, D = 'A', 'B', 'C', 'D'
    labelset_list = [(A, B, C),
                     (B),
                     (A, C),
                     tuple([D]),
                     (B, C),
                     (A)]
    labelset_list = map(set, labelset_list)
    actual_tree = construct_ptree(labelset_list)
    expected_tree = [[], [0], [0], [], [0, 1, 2], [0, 2]]
    # [(0, 1), (0, 2),
    #                   (1, 4), (2, 4), (2, 5)]
    assert_equal(actual_tree, expected_tree)
    
