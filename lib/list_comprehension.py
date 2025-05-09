#!/usr/bin/env python3

def return_evens(num_list):
    """
    Return a list of even numbers from the input list.

    :param num_list: List of integers
    :return: List of even integers
    """
    return [num for num in num_list if num % 2 == 0]
    
    

def make_exclamation(sentence_list):
    
    """
    Append an exclamation mark to each sentence in the input list.

    :param sentence_list: List of strings
    :return: List of strings with exclamation marks
    """
    return [sentence + "!" for sentence in sentence_list]