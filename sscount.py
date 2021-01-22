"""Advanced Algorithms, January 2021
Assignment 3: Space Saving Count
Author: João Ferreira, 80041

This program needs 1 argument, a text file
Example of usage:
    python3 sscount.py text/<english/portuguese>/<text_file> 
"""

import sys
import argparse
import coloredlogs, logging


logger = logging.getLogger('root')

def exact_counter(words):
    '''
    returns a dictionary <word,count>
    '''
    counter = {}
    for word in words:
        word = word.lower()
        if word in counter:
            counter[word]+=1
        else:
            counter[word]=1
    
    logger.info('Completed Exact Counter.')
    return counter


def read_file(text_file):
    '''
    returns an array of words
    '''
    words = []
    try:
        with open(text_file,'r') as file:  
            for line in file:        
                for word in line.strip().split():      
                    words.append(word)    

    except:
        logger.error('File not found.')
        sys.exit(2) #Code 2 - Command line syntax errors

    logger.info('Text file read with success.')
    
    return words

def main(text_file):
    words = read_file(text_file)

    exact = exact_counter(words)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Count words from a text file')
    parser.add_argument('-f', metavar='<text_file>', help='Text file', required=True)
    args = parser.parse_args()
    
    coloredlogs.install(logging.INFO)
	
    logger.setLevel(logging.INFO)

    main(args.f)