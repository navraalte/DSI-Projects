from pyspark import SparkConf, SparkContext 

# boilerplate 
conf = SparkConf().setMaster("local").setAppName("Gutenberg")  
sc = SparkContext(conf=conf)

# read in data file and execute transformations 
alice_wonderland = sc.textFile("proj_gutenberg_alic.txt")
mapper = alice_wonderland.map(lambda line: line.split()).flatMap(lambda word: word).map(lambda word: (word, 1))
reducer = mapper.reduceByKey(lambda x, y: x + y)

# collect and print the output 
for key, word_count in reducer.collect():
    print key.strip(), word_count 
