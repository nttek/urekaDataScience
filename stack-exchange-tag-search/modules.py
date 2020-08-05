#import essential libraries
import ast                  #for text processing
import itertools
import collections
from collections import Counter
import networkx as nx      #networkx for w. graph
import pandas as pd

def get_rows(records):
    #save the dataframe as a list of row lists
    rows_list = []
    
    i=0
    while i < len(records.index):
        row = str(records.iloc[i,0])
        row = ast.literal_eval(row) 
        rows_list.append(row)
        i = i + 1
        
    return rows_list


def create_graph():
    #read records (step can be skipped if API call was executed beforehand)
    records = pd.read_csv('Data/tags.csv',index_col=0)
    
    #get the info stored in each row as a list
    rows_list = get_rows(records)
    
    #combine all the tags in a single list
    rows_concat = list(itertools.chain.from_iterable(rows_list))
    counts = collections.Counter(rows_concat)
    
    #remove term frequency from the dictionary (there may be other uses to it though)
    key_tags = list(counts.keys())
        
    #create a new weighted graph
    G=nx.Graph() 

    #add nodes for each of the key tags 
    G.add_nodes_from(key_tags)

    #create or change edge weights based on prior condition/value 
    #for between cluster of the key tags
    for row in rows_list:
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                if G.has_edge(row[i],row[j]):
                    G[row[i]][row[j]]['weight'] = G[row[i]][row[j]]['weight'] + 1
                else:
                    G.add_edge(row[i],row[j], weight=1)
                    
    return G
        
#method to return list of tags which are related to a search query 
#version 2.1, handles multiple tags
def tag_query(G, key_tag):
    word_split = str(key_tag).split()
    sum_dict = {}

    for word in word_split:
        temp_dict = {}
        edges = list(G.edges(word.lower())) #returns a list of all the edges from EdgeDataView

        for edge in edges:
            x = G.get_edge_data(edge[0],edge[1])
            temp_dict[edge[1]] = x['weight']

        sum_dict = dict(Counter(sum_dict) + Counter(temp_dict))       

    if sum_dict:
        result = sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in result]
        result = ' | '.join(result)
        
    else:
        result = 'No results match your search query'
        
    return result
    