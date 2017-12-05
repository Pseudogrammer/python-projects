

hand=open("gradebook.csv","r")
content=hand.read()
lines=content.split("\n")
head=lines[0].split(",")
part1={}
for i in range(len(lines)-3):
    strs=lines[i+1].split(",")
    innerdict={}
    for j in range(len(strs)-1):
        innerdict[head[j+1]]=strs[j+1]
    part1[strs[0]]=innerdict
print("PART 1")
print(part1,"\n")
part2={}
for i in range(len(head)-1):
    innerdict={}
    strs1=lines[-2].split(",")
    strs2 = lines[-1].split(",")
    part2[head[i+1]]={strs1[0]:strs1[i+1],strs2[0]:strs2[i+1]}
print("PART 2")
print(part2,"\n")
def student_average(student_name):
    avg=0
    scores=list(map(float,part1[student_name].values()))
    for i in range(len(head)-1):
        values=list(map(float,list(part2.values())[i].values()))
        avg+=scores[i]*values[0]*100/values[1]
    return avg
print("PART 3")
for i in range(len(lines)-3):
    strs = lines[i + 1].split(",")
    print(strs[0]+" :",student_average(strs[0]))
def assn_average(assn_name):
    maxx=float(list(dict(part2[assn_name]).values())[1])
    avg=0
    for i in range(len(lines)-3):
        avg+=float(dict(list(part1.values())[i])[assn_name])
    return avg*100/(len(lines)-3)/maxx
print("\nPART 4")
for i in range(len(head)-1):
    print(head[i+1]+" :",assn_average(head[i+1]))
print("\nPART 5")
def format_gradebook():
    strs = lines[0].split(",")
    result="{:9}".format(strs[0])
    total=lines[-1].split(",")
    for j in range(len(strs) - 1):
        result += "{:>12}".format(strs[j + 1])
    result+="{:>12}".format("Grade")+"\n"+'{:_<69}'.format("")+"\n"
    for i in range(len(lines)-3):
        strs=lines[i+1].split(",")
        line="{:9}".format(strs[0])
        for j in range(len(strs)-1):
            line+="{:>12}".format(str(round(float(strs[j+1])*100/float(total[j+1]),1))+"%")
        line+="{:>12}".format(str(round(student_average(strs[0]),1))+"%")
        line+="\n"
        result+=line
    result +='{:_<69}'.format("") + "\n"
    result += "{:9}".format("Average")
    strs = lines[0].split(",")
    avg_grage=0
    for i in range(len(head)-1):
        result += "{:>12}".format(str(round(assn_average(strs[i+1]), 1)) + "%")
    for i in range(len(lines) - 3):
        strs = lines[i + 1].split(",")
        avg_grage+=student_average(strs[0])
    result+="{:>12}".format(str(round(avg_grage/6,1))+"%")
    return result
print(format_gradebook())





