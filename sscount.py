"""Advanced Algorithms, January 2021
Assignment 3: Space Saving Count
Author: João Ferreira, 80041

This program needs 1 argument, a text file
Example of usage:
    python3 sscount.py text/portuguese/os_maias.txt
    python3 sscount.py text/english/hamlet.txt
"""

import sys
import argparse
import coloredlogs, logging
import csv


logger = logging.getLogger('root')

def sscounter(chars, k):
    '''
    returns a dictionary <char,count>
    '''
    counters = {}                   
    for elem in chars:
        elem = elem.lower()              
        if elem in counters:        
            counters[elem] += 1
        else:                               
            if len(counters) + 1 > k: #Tamanho actual mais um (que corresponde ao novo elemento)
                min_counter = min(counters, key=counters.get)       
                counters[elem] = counters.pop(min_counter) + 1      
            else:
                counters[elem] = 1
    
    logger.info('Completed Space Saving Counter (k = {}).'.format(k))    
    
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
    
    logger.info('Completed Exact Counter.')
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
        logger.error('File not found.')
        sys.exit(2) #Code 2 - Command line syntax errors

    logger.info('Text file read with success.')
    
    return chars

def relative_error(exact, ssc):
    rel_error = {}
    for key in ssc:
        rel_error[key] = round(( abs(ssc[key]-exact[key]) / exact[key]) * 100, 3)
    
    return rel_error

    

def main(text_file):
    chars = read_file(text_file)

    exact = exact_counter(chars)

    
    # SPACE SAVING COUNTER , K=10
    ssc10 = sscounter(chars,10) 

    relative_error_10 = relative_error(exact,ssc10)


    # SPACE SAVING COUNTER , K=15
    ssc15 = sscounter(chars,15) 

    relative_error_15 = relative_error(exact,ssc15)

    
    # SPACE SAVING COUNTER , K=20
    ssc20 = sscounter(chars,20) 

    relative_error_20 = relative_error(exact,ssc20)


    # SPACE SAVING COUNTER , K=25
    ssc25 = sscounter(chars,25) 

    relative_error_25 = relative_error(exact,ssc25)


    # SPACE SAVING COUNTER , K=100
    ssc100 = sscounter(chars,100) 

    relative_error_100 = relative_error(exact,ssc100)

    
    #write results - only common chars to all the counters
    
    file_name = text_file.split("/")[ len(text_file.split("/"))-1 ]
    
    with open('results/results_'+file_name+'.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([ 'char','exact','ssc10','ssc15','ssc20','ssc25','ssc100' ] )
        for char in exact:
            if char in ssc10 and char in ssc15 and char in ssc20 and char in ssc25 and char in ssc100:
                writer.writerow( [ char,exact[char],ssc10[char],ssc15[char],ssc20[char],ssc25[char],ssc100[char] ] )
    
    #write error results 
    with open('results/error_results_'+file_name+'.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([ 'char','error-ssc10','error-ssc15','error-ssc20','error-ssc25','error-ssc100' ] )
        for char in exact:
            if char in ssc10 and char in ssc15 and char in ssc20 and char in ssc25 and char in ssc100:
                writer.writerow( [ char,relative_error_10[char],relative_error_15[char],relative_error_20[char],relative_error_25[char],relative_error_100[char] ] )

    logger.info('Wrote results to .csv files in results/ folder.')
    

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Count chars from a text file')
    parser.add_argument('-f', metavar='<text_file>', help='Text file', required=True)
    args = parser.parse_args()
    
    coloredlogs.install(logging.INFO)
	
    logger.setLevel(logging.INFO)

    main(args.f)