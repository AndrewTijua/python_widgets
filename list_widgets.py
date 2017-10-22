#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:31:24 2017

@author: Benjamin Cox (https://github.com/AndrewTijua)
"""

def addLists(*args):
    """
    Takes an arbitrary number of lists with the same number of elements and sums them elementwise
    """
    listsum = args[0]
    for i in range(len(args)-1):
        listsum = list(map(lambda a, b: a + b, listsum, args[i+1]))
    return listsum

def multLists(*args):
    """
    Takes an arbitrary number of lists with the same number of elements and multiplies them elementwise
    """
    listprod = args[0]
    for i in range(len(args)-1):
        listprod = list(map(lambda a, b: a * b, listprod, args[i+1]))
    return listprod

def extractIndices(extract_list, element):
    indices = []
    for i in range(len(extract_list)):
        if extract_list[i] == element:
            indices.append(i)  
    return indices

def extractNotIndices(extract_list, element):
    indices = []
    for i in range(len(extract_list)):
        if extract_list[i] != element:
            indices.append(i)  
    return indices

def extractFromIndices(listToExtract, indices):
    extracted = []
    for i in indices:
        extracted.append(listToExtract[i])
    return extracted

def createPopulation(listOfLists, indices):
    listReturn = []
    for i in range(len(listOfLists)): 
        listReturn.append([])
    for i in range(len(listOfLists)):
        for j in indices:
            listReturn[i].append(listOfLists[i][j])
    return listReturn