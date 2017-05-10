

def substrings(s) :
  if len(s) == 1 :  # Base case
    return [s];
  subs = substrings(s[1:]) #Recursively iterates through string
  #print "This is subs", subs
  #print "Return is ", [string[0]+i for i in subs]+subs+[string[0]] 
  return [s[0]+i for i in subs]+subs+[s[0]]; #Returns combinations

number = int(raw_input())

strings = []
for i in range(number) :
  length = int(raw_input())
  strings.append(raw_input())

for string in strings :
  sub = substrings(string)
  sub.sort() # Sort the combinations in lexographical order
  for i in sub : print i


 """
 Input
1
3
xyz

Iteration 1 : Goes to base case
This is subs ['z'] # Base case
Return is  ['yz', 'z', 'y']
Iteration 2 : Returns from substrings call
This is subs ['yz', 'z', 'y']
Return is  ['xyz', 'xz', 'xy', 'yz', 'z', 'y', 'x']

Output :
x
xy
xyz
xz
y
yz
z


 """