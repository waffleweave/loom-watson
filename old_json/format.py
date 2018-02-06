import sys
import json

f_in = open(sys.argv[1],'r')
f_out = open(sys.argv[2],'w')

for line in f_in:
    l2 = json.dumps(line[:len(line)-1])
    f_out.write(l2+"\\\n")
