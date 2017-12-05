import re
import random
hand=open("mbox.txt","r")
out=open("mbox-anon.txt","w")
out1=open("mbox-anon-key.txt","w")
email=[]
for line in hand:
    line=line.rstrip()
    x=re.findall("[a-zA-Z0-9.]\S+@\w+\.[a-z.]+",line)
    if len(x)>0 and not x[0][0].isdigit():
        email.append(x[0])
uniqemail=set(email)
n=len(uniqemail)
num=random.sample(range(10000,99999),n)
match=dict(zip(list(uniqemail),num))
hand.seek(0)
allfile=hand.read()
for mail in uniqemail:
    allfile=allfile.replace(mail,"%%"+str(match[mail])+"%%")
out.write(allfile)
match=dict(zip(match.values(),match.keys()))
for i in match.keys():
    out1.write(str(i)+"="+match[i]+"\n")
hand.close()
out.close()
out1.close()