f = open("input.txt","r")
out = open("output.txt","w")
for l in f:
    for c in l:
        if c == u"\u0020":
            out.write(u"\u00A0")
        elif c == u"\u0009":
            out.write(u"\u00A0\u00A0\u00A0\u00A0")
        else:
            out.write(c)