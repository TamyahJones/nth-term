import sys

# nth term, e.g. 'n + 1'
nth =  sys.argv[1]

# number of terms to print, e.g 10
n = int(sys.argv[2])

def nth_term(n):
    #eval is sloooow
    return eval(nth)

print "The first ", n, " terms of seqence '", nth, "' are:"

for i in range(n):
    print i + 1, " -> ", nth_term(i + 1)
