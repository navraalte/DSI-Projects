import sys 

# input comes from standard input 
for line in sys.stdin: 
    # remove bad characters 
    line = line.strip()

    # words 
    words = line.split()

    # increase counters 
    for word in words: 
        print '{}\t{}'.format(word, 1)
