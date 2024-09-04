def ful_e(p):
    r = []
    for em, na in p:
        r.append("\n{} : {}".format(na, em))
    return r
# Test cases
output = ful_e([("arjun@gmail.com", "arjun murmu"), ("jit@gmail.com", "jitmohan hembram")])
for line in output:
    print(line)
