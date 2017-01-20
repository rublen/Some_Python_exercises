key = "aaaaabbbbbabbbaabbababbaaababaab"
alphabet = 'abcdefghijklmnopqrstuvwxyz'
import sys
del sys.argv[0]
ab_shyfr = ''
for i in range(0,len(''.join(sys.argv))): 
    if ''.join(sys.argv)[i].islower(): ab_shyfr += 'a'
    elif ''.join(sys.argv)[i].isupper(): ab_shyfr += 'b'
result = ''
for j in range(5,len(ab_shyfr),5):
    result += alphabet[key.find(ab_shyfr[j-5:j])]
print(result)
