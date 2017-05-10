import sys 

current_word = None 
current_count = 0
word = None 

# input comes from STDIN 
for line in sys.stdin: 
    # strip new lines and everything else
    line = line.strip()

    # parse the input we got from the mapper.py
    word, count = line.split('\t', 1)
    
    # convert count to int
    count = int(count)

    # aggregation phase
    if current_word == word: 
        current_count += 1
    else:
        if current_word:
            print '{}\t{}'.format(current_word, current_count)
        current_word = word
        current_count = count 

if current_word == word: 
    print '{}\t{}'.format(current_word, current_count)
