'''Advanced Algorithms, January 2021
Assignment 3: Space Saving Count
Author: João Ferreira, 80041

This program needs 1 argument, a text file
Example of usage:
    python3 sscount.py text/portuguese/os_maias.txt
    python3 sscount.py text/english/hamlet.txt
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

    print(len(chars))
    # SPACE SAVING COUNTER , K=10
    ssc10 = ssc(chars,10) 

    relative_error_10 = relative_error(exact,ssc10)

    print( 'Space Saving Counter, K=10')
    print( 'Max Relative Error: ' + str(relative_error_10[list(relative_error_10.keys())[-1] ]))
    print( 'Min Relative Error: ' + str(relative_error_10[list(relative_error_10.keys())[0] ]))
    print( 'Avg Relative Error: ' + str(avg_error(relative_error_10)))
    print( '--------------------------')

    # SPACE SAVING COUNTER , K=15
    ssc15 = ssc(chars,15) 

    relative_error_15 = relative_error(exact,ssc15)

    print( 'Space Saving Counter, K=15')
    print( 'Max Relative Error: ' + str(relative_error_15[list(relative_error_15.keys())[-1] ]))
    print( 'Min Relative Error: ' + str(relative_error_15[list(relative_error_15.keys())[0] ]))
    print( 'Avg Relative Error: ' + str(avg_error(relative_error_15)))
    print( '--------------------------')
    
    # SPACE SAVING COUNTER , K=20
    ssc20 = ssc(chars,20) 

    relative_error_20 = relative_error(exact,ssc20)

    print( 'Space Saving Counter, K=20')
    print( 'Max Relative Error: ' + str(relative_error_20[list(relative_error_20.keys())[-1] ]))
    print( 'Min Relative Error: ' + str(relative_error_20[list(relative_error_20.keys())[0] ]))
    print( 'Avg Relative Error: ' + str(avg_error(relative_error_20)))
    print( '--------------------------')

    # SPACE SAVING COUNTER , K=25
    ssc25 = ssc(chars,25) 

    relative_error_25 = relative_error(exact,ssc25)

    print( 'Space Saving Counter, K=25')
    print( 'Max Relative Error: ' + str(relative_error_25[list(relative_error_25.keys())[-1] ]))
    print( 'Min Relative Error: ' + str(relative_error_25[list(relative_error_25.keys())[0] ]))
    print( 'Avg Relative Error: ' + str(avg_error(relative_error_25)))
    print( '--------------------------')


    # SPACE SAVING COUNTER , K=50
    ssc50 = ssc(chars,50) 

    relative_error_50 = relative_error(exact,ssc50)

    print( 'Space Saving Counter, K=50')
    print( 'Max Relative Error: ' + str(relative_error_50[list(relative_error_50.keys())[-1] ]))
    print( 'Min Relative Error: ' + str(relative_error_50[list(relative_error_50.keys())[0] ]))
    print( 'Avg Relative Error: ' + str(avg_error(relative_error_50)))

    #write results - only common chars to all the counters
    
    file_name = text_file.split('/')[ len(text_file.split('/'))-1 ]
    
    with open('results/results_'+file_name+'.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([ 'char','exact2','ssc10','ssc15','ssc20','ssc25','ssc50' ] )
        for char in exact:
            if char in ssc10:
                s10=ssc10[char]
            else:
                s10='-'
            if char in ssc15:
                s15=ssc15[char]
            else:
                s15='-'
            if char in ssc20:
                s20=ssc20[char]
            else:
                s20='-'
            if char in ssc25:
                s25=ssc25[char]
            else:
                s25='-'
            if char in ssc50:
                s50=ssc50[char]
            else:
                s50='-'
            
            writer.writerow( [ char,exact[char],s10,s15,s20,s25,s50 ] )
    
    #write error results 
    with open('results/error_results_'+file_name+'.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([ 'char','error-ssc10','error-ssc15','error-ssc20','error-ssc25','error-ssc50' ] )
        for char in exact:
            if char in relative_error_10:
                e10=relative_error_10[char]
            else:
                e10='-'
            if char in relative_error_15:
                e15=relative_error_15[char]
            else:
                e15='-'
            if char in relative_error_20:
                e20=relative_error_20[char]
            else:
                e20='-'
            if char in relative_error_25:
                e25=relative_error_25[char]
            else:
                e25='-'
            if char in relative_error_50:
                e50=relative_error_50[char]
            else:
                e50='-'
            writer.writerow( [ char,e10,e15,e20,e25,e50 ] )

    

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Count chars from a text file')
    parser.add_argument('-f', metavar='<text_file>', help='Text file', required=True)
    args = parser.parse_args()

    main(args.f)