import sys
f = open('out.log', 'w')
sys.stdout = f
n = int(sys.argv[1])
power = 1
for x in range(n+1):
    print(x, "\t", x*2, "\t", power)
    power *= 2
sys.stdout = sys.__stdout__
print("done!")
