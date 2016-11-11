import networkx as nx
import pandas as pd
import time

##########
Trust = 4  #
##########
input_file = './stream_payment.csv'
output_file = './batch_payment.csv'
result = './output3.csv'


def fraud_detection():
    df = pd.read_csv(input_file, usecols=range(4), dtype=str) # creat matrix
    df2 = df[[1, 2]].drop_duplicates() # drop duplicates
    g = nx.from_pandas_dataframe(df2, df2.columns[0], df2.columns[1]) # construct relationship graph
    print 'begin...' #check progress
    df_output = pd.read_csv(output_file, usecols=range(4), dtype=str)  # load test file

    df_clean = df_output.dropna(how='any') # dropout rows' with null value
    print 'start...'
    df_clean['label'] = df_clean.apply(lambda l: 'untrusted' if nx.shortest_path_length(g, l[1], l[2]) > Trust else 'trusted',
                                         axis=1) # determine whether shortest path less equall than trust (degree)
    df_clean['label'].to_csv(result) # output detaction reasult


if __name__ == '__main__': # record running time
    start = time.time()
    fraud_detection()
    end = time.time()
    print(end - start)
