from random import randint
from collections import Counter
Ring = ["Blank",{"Opp","Strife"},"Opp",{"Success","Strife"},"Success",{"ExpSuccess","Strife"}]
Skill = ["Blank","Blank","Opp","Opp","Opp",{"Success","Strife"},{"Success","Strife"},"Success","Success",{"Success","Opp"},{"ExpSuccess","Strife"},"ExpSuccess"]
#Q: Likelihood of TN2 success with 2 Opps
#RingLevel = raw_input("Please input the ring level: ")
#SkillLevel = raw_input("Please input the skill level: ")
#TN = raw_input("Please input the TN: ")
RingLevel = 3
SkillLevel = 1
TN = 1
Rolls = 100
output=[]
def countList(lst, x):
    return sum(x in item for item in lst)

#generate a dataset of random rolls
for i in range(0,Rolls) :
    x = Ring[randint(0,5)]
    s = Skill[randint(0,11)]
    output.append(x)
    output.append(s)


#return number of rolls with N success
print(countList(output, "Success"))



