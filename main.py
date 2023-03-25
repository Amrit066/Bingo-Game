import random
"""WELCOME TO BINGO BOARD GAME PRO"""
dict1={}
dict2={}

#Initializing dict2
dict2["1"]="1"
dict2["2"]="2"
dict2["3"]="3"
dict2["4"]="4"
dict2["5"]="5"
dict2["6"]="6"
dict2["7"]="7"
dict2["8"]="8"
dict2["9"]="9"
dict2["10"]="10"
dict2["11"]="11"
dict2["12"]="12"
dict2["13"]="13"
dict2["14"]="14"
dict2["15"]="15"
dict2["16"]="16"
dict2["17"]="17"
dict2["18"]="18"
dict2["19"]="19"
dict2["20"]="20"
dict2["21"]="21"
dict2["22"]="22"
dict2["23"]="23"
dict2["24"]="24"
dict2["25"]="25"

#Initializing dict1
dict1["1"]="*"
dict1["2"]="*"
dict1["3"]="*"
dict1["4"]="*"
dict1["5"]="*"
dict1["6"]="*"
dict1["7"]="*"
dict1["8"]="*"
dict1["9"]="*"
dict1["10"]="*"
dict1["11"]="*"
dict1["12"]="*"
dict1["13"]="*"
dict1["14"]="*"
dict1["15"]="*"
dict1["16"]="*"
dict1["17"]="*"
dict1["18"]="*"
dict1["19"]="*"
dict1["20"]="*"
dict1["21"]="*"
dict1["22"]="*"
dict1["23"]="*"
dict1["24"]="*"
dict1["25"]="*"

str1=""
str2=""
str3=""
flag="n"
values=[]
num=1
i=1




def board_1():
  print ("\t___________________________________")
  print ("\t|  "+dict1["1"]+"   |  "+dict1["2"]+"   |  "+dict1["3"]+"   |  "+dict1["4"]+"   |  "+dict1["5"]+"   |")
  print ("\t|______|______|______|______|______|")
  print ("\t|  "+dict1["6"]+"   |  "+dict1["7"]+"   |  "+dict1["8"]+"   |  "+dict1["9"]+"   |  "+dict1["10"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict1["11"]+"   |  "+dict1["12"]+"  |  "+dict1["13"]+"  |  "+dict1["14"]+"  |  "+dict1["15"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict1["16"]+"   |  "+dict1["17"]+"  |  "+dict1["18"]+"  |  "+dict1["19"]+"  |  "+dict1["20"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict1["21"]+"   |  "+dict1["22"]+"  |  "+dict1["23"]+"  |  "+dict1["24"]+"  |  "+dict1["25"]+"  |")
  print ("\t|______|______|______|______|______|")

def board_2():
  print ("\t___________________________________")
  print ("\t|  "+dict2["1"]+"   |  "+dict2["2"]+"   |  "+dict2["3"]+"   |  "+dict2["4"]+"   |  "+dict2["5"]+"   |")
  print ("\t|______|______|______|______|______|")
  print ("\t|  "+dict2["6"]+"   |  "+dict2["7"]+"   |  "+dict2["8"]+"   |  "+dict2["9"]+"   |  "+dict2["10"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict2["11"]+"   |  "+dict2["12"]+"  |  "+dict2["13"]+"  |  "+dict2["14"]+"  |  "+dict2["15"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict2["16"]+"   |  "+dict2["17"]+"  |  "+dict2["18"]+"  |  "+dict2["19"]+"  |  "+dict2["20"]+"  |")
  print ("\t|______|______|______|______|______|")
  print ("\t| "+dict2["21"]+"   |  "+dict2["22"]+"  |  "+dict2["23"]+"  |  "+dict2["24"]+"  |  "+dict2["25"]+"  |")
  print ("\t|______|______|______|______|______|")

def check():
  if((dict1["1"]==dict1["2"]) and (dict1["2"]==dict1["3"]) and (dict1["3"]==dict1["4"]) and (dict["4"]==dict["5"])):
    return (1)
  if((dict1["6"]==dict1["7"]) and (dict1["7"]==dict1["8"]) and (dict1["8"]==dict1["9"]) and (dict["9"]==dict["10"])):
    return (1)
  if((dict1["11"]==dict1["12"]) and (dict1["12"]==dict1["13"]) and (dict1["13"]==dict1["14"]) and (dict["14"]==dict["15"])):
    return (1)
  if((dict1["16"]==dict1["17"]) and (dict1["17"]==dict1["18"]) and (dict1["18"]==dict1["19"]) and (dict["19"]==dict["20"])):
    return (1)
  if((dict1["21"]==dict1["22"]) and (dict1["22"]==dict1["23"]) and (dict1["23"]==dict1["24"]) and (dict["24"]==dict["25"])):
    return (1)
  if((dict1["1"]==dict1["6"]) and (dict1["6"]==dict1["11"]) and (dict1["11"]==dict1["16"]) and (dict["16"]==dict["21"])):
    return (1)
  if((dict1["2"]==dict1["7"]) and (dict1["7"]==dict1["12"]) and (dict1["12"]==dict1["17"]) and (dict["17"]==dict["22"])):
    return (1)
  if((dict1["3"]==dict1["8"]) and (dict1["8"]==dict1["13"]) and (dict1["13"]==dict1["18"]) and (dict["18"]==dict["23"])):
    return (1)
  if((dict1["4"]==dict1["9"]) and (dict1["9"]==dict1["14"]) and (dict1["14"]==dict1["19"]) and (dict["19"]==dict["25"])):
    return (1)
  if((dict1["5"]==dict1["10"]) and (dict1["10"]==dict1["15"]) and (dict1["15"]==dict1["20"]) and (dict["20"]==dict["25"])):
    return (1)
  if((dict1["1"]==dict1["7"]) and (dict1["7"]==dict1["13"]) and (dict1["13"]==dict1["19"]) and (dict["19"]==dict["25"])):
    return (1)
  if((dict1["5"]==dict1["9"]) and (dict1["9"]==dict1["13"]) and (dict1["13"]==dict1["17"]) and (dict["17"]==dict["21"])):
    return (1)

def cell_values():
  while(len(values)!=25):
    num=random.randrange(1,26)
    if(num not in values):
      values.append(num)

cell_values()


for each in values:
      str1=str(i)
      str2=str(each)
      dict1[str1]=str2
      i=i+1

while(flag=="n"):
  print("Original B-Board:")
  board_2()
  print("Actual B-Board:")
  board_1()
  str1=input("Enter cell no whoose value you want to delete from Original B-Board: \n ")
  dict1[str1]= "0"
  if(check()):
    print("Hurray!!! You Won! 👍")
    break
  flag1=input("Want to quit(choose-'y/n):")
  if(flag1=="y"):
    print("You missed the chance to win 😟")