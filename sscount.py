'''Advanced Algorithms, January 2021
Assignment 3: Space Saving Count
Author: João Ferreira, 80041

This program needs 1 argument, a text file
Example of usage:
    python3 sscount.py -f text/portuguese/os_maias.txt
    python3 sscount.py -f text/english/hamlet.txt
'''

import sys
import argparse
import csv


def ssc(chars, k):
    '''
    returns a dictionary <char,count>
    '''
    counters = {}                   
    for char in chars:
        char = char.lower()              
        if char in counters:        
            counters[char] += 1
        else:                               
            if len(counters) + 1 > k:
                min_counter = min(counters, key=counters.get)       
                counters[char] = counters.pop(min_counter) + 1      
            else:
                counters[char] = 1
    return counters


def exact_counter(chars):
    '''
    returns a dictionary <char,count>
    '''
    counter = {}
    for char in chars:
        char = char.lower()
        if char in counter:
            counter[char]+=1
        else:
            counter[char]=1
    

    return counter


def read_file(text_file):
    '''
    returns an array of chars
    '''
    chars = []
    try:
        with open(text_file,'r') as file:  
            for line in file:        
                for word in line.strip().split():
                    for l in word:
                        if l.isalnum():
                            chars.append(l)

    except:
        print('File not found.')
        sys.exit(2) #Code 2 - Command line syntax errors

    return chars

def relative_error(exact, ssc):
    rel_error = {}
    for key in ssc:
        rel_error[key] = round(( abs(ssc[key]-exact[key]) / exact[key]) * 100, 3)
    
    rel_error = {k: v for k, v in sorted(rel_error.items(), key=lambda item: item[1])}
    
    return rel_error

def avg_error(errors):
    sum = 0
    n = 0
    for e in errors:
        sum += errors[e]
        n += 1
    return round(sum/n,2) 

def main(text_file):
    chars = read_file(text_file)

    exact = exact_counter(chars)

    # SPACE SAVING COUNTER , K=10
    ssc10 = ssc(chars,10) 

    # SPACE SAVING COUNTER , K=15
    ssc15 = ssc(chars,15) 
    
    # SPACE SAVING COUNTER , K=20
    ssc20 = ssc(chars,20) 

    # SPACE SAVING COUNTER , K=25
    ssc25 = ssc(chars,25) 

    # SPACE SAVING COUNTER , K=50
    ssc50 = ssc(chars,50) 

    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Count chars from a text file')
    parser.add_argument('-f', metavar='<text_file>', help='Text file', required=True)
    args = parser.parse_args()

    main(args.f)