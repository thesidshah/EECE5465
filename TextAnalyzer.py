import sys
import argparse
import findspark
findspark.init()
from time import time
from pyspark import SparkContext
from operator import add
def count_sentences(rdd):
    """ Count the sentences in a file.

    Input:
    - rdd: an RDD containing the contents of a file, with one sentence in each element.

    return rdd.map(lambda x:1)\
		.reduce(add)
    Return value: The total number of sentences in the file.
    """
    return rdd.map(lambda x:1)\
		.reduce(add)

def count_words(rdd):
    """ Count the number of words in a file.

    Input:
    - rdd: an RDD containing the contents of a file, with one sentence in each element.
    Return value: The total number of words in the file.
    """
    count = rdd.flatMap(lambda line:line.split(" ")) \
    .map(lambda word: 1) \
    .reduce(add)
    return count
    # pass
from helpers import to_lower_case, strip_non_alpha
def compute_counts(rdd,numPartitions = 10):
    """ Produce an rdd that contains the number of occurences of each word in a file.

    Each word in the file is converted to lowercase and then stripped of leading and trailing non-alphabetic
    characters before its occurences are counted.

    Input:
    - rdd: an RDD containing the contents of a file, with one sentence in each element.

    
    Return value: an RDD containing pairs of the form (word,count), where word is is a lowercase string, 
    without leading or trailing non-alphabetic characters, and count is the number of times it appears
    in the file. The returned RDD should have a number of partitions given by numPartitions.

    """
    # pass
    count = rdd.flatMap(lambda line: line.split(" ")) \
      .map(lambda word: strip_non_alpha(to_lower_case(word))) \
        .map(lambda word: (word,1)) \
          .reduceByKey(lambda x,y: x + y) 
    return count
    

def count_difficult_words(counts,easy_list):
    """ Count the number of difficult words in a file.

    Input:
    - counts: an RDD containing pairs of the form (word,count), where word is a lowercase string, 
    without leading or trailing non-alphabetic characters, and count is the number of times this word appears
    in the file.
    - easy_list: a list of words deemed 'easy'.


    Return value: the total number of 'difficult' words in the file represented by RDD counts. 

    A word should be considered difficult if is not the 'same' as a word in easy_list. Two words are the same
    if one is the inflection of the other, when ignoring cases and leading/trailing non-alphabetic characters. 
    """
    pass   




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Text Analysis via the Dale Chall Formula',formatter_class=argparse.ArgumentDefaultsHelpFormatter)    
    parser.add_argument('mode', help='Mode of operation',choices=['SEN','WRD','UNQ','TOP20','DFF','DCF']) 
    parser.add_argument('input', help='Text file to be processed. This file contains text over several lines, with each line corresponding to a different sentence.')
    parser.add_argument('--master',default="local[20]",help="Spark Master")
    parser.add_argument('--N',type=int,default=20,help="Number of partitions to be used in RDDs containing word counts.")
    parser.add_argument('--simple_words',default="DaleChallEasyWordList.txt",help="File containing Dale Chall simple word list. Each word appears in one line.")
    args = parser.parse_args()
  
    sc = SparkContext(args.master, 'Text Analysis')
    sc.setLogLevel('warn')

    start = time()

    # Add tour code here
    lines = sc.textFile(args.input)
    if(args.mode == "SEN"):
      count = count_sentences(lines)
      print(f"Total count of sentences in {args.input} is {count}")
    elif(args.mode == "WRD"):
      count = count_words(lines)
      print(f"Total count of words in {args.input} is {count}")
    elif(args.mode == "UNQ"):
      # count = compute_counts()
      lines = sc.textFile(args.input, args.N)
      count = compute_counts(lines)
      output = count.sortBy(lambda x: x[2]).collect()
      for (word, counts) in output:
          print("%s: %i" % (word, counts))
    end = time()
    print('Total execution time:',str(end-start)+'sec')
