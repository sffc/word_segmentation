import numpy as np
from . import constants


def is_ascii(input_str):
    """
    A very basic function that checks if all elements of str are ASCII or not
    Args:
        input_str: input string
    """
    return all(ord(char) < 128 for char in input_str)


def diff_strings(str1, str2):
    """
    A function that returns the number of elements of two strings that are not identical
    Args:
        str1: the first string
        str2: the second string
    """
    if len(str1) != len(str2):
        print("Warning: length of two strings are not equal")
        return -1
    return sum(str1[i] != str2[i] for i in range(len(str1)))


def sigmoid(inp):
    """
    Computes the sigmoid function of a scalar or a 1d numpy array
    Args:
        inp: the input which can be a scalar or a 1d numpy array
    """
    inp = np.asarray(inp)
    # Checking for case when the input is an array/np.array of arrays. In this case only the first element of inp is
    # used. A common example is when A = np.array([np.array([1, 2, 3])]).
    if inp.ndim == 2:
        inp = inp[0]
    return 1.0 / (1.0 + np.exp(-np.clip(inp, -709.78, 709.78)))


def print_grapheme_clusters(thrsh, language, exclusive):
    """
    This function print the grapheme clusters and their frequencies for a given langauge. It also computes what
    percentage of grapheme clusters form which percent of the text
    Args:
        thrsh: shows what percent of the text we want to be covered by grapheme clusters
        language: shows the language that we are working with
        exclusive: shows if we only consider grapheme clusters in a single script or not
    """
    ratios = None
    if language == "Thai" and exclusive is False:
        ratios = constants.THAI_GRAPH_CLUST_RATIO
    if language == "Thai" and exclusive is True:
        ratios = constants.THAI_EXCLUSIVE_GRAPH_CLUST_RATIO
    if language == "Burmese" and exclusive is False:
        ratios = constants.BURMESE_GRAPH_CLUST_RATIO
    if language == "Burmese" and exclusive is True:
        ratios = constants.BURMESE_EXCLUSIVE_GRAPH_CLUST_RATIO
    if language == "Thai-Burmese":
        ratios = constants.THAI_BURMESE_GRAPH_CLUST_RATIO
    if ratios is None:
        print("No grapheme cluster dictionary has been computed for the input language.")
        return
    cum_sum = 0
    cnt = 0
    for val in ratios.values():
        cum_sum += val
        cnt += 1
        if cum_sum > thrsh:
            break
    print(ratios)
    print("number of different grapheme clusters in {} = {}".format(language, len(ratios.keys())))
    print("{} grapheme clusters form {} of the text".format(cnt, thrsh))
