f = open('1ex.txt')
s_in = f.read()
s_out = ""
count = 1
for i in range(0, len(s_in)-1):
    if s_in[i] == s_in[i+1]:
        count = count + 1
    else:
        if (count != 1):
            s_out += str(count)
        s_out += s_in[i]
        count = 1
if (count != 1):
    s_out += str(count)
s_out += s_in[len(s_in)-1]
print(s_out)
f.close()