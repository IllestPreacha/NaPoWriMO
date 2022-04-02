#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random

#number reponds to the amount of syllables needed for the haiku to work
# 5 7 5


with open("ColorSingle.Txt", "r") as Color_1:  #open and read the text file
    C1 = Color_1.read()  #give the file a variable name 
    C1_Used = list(map(str,C1.split())) #individuals words
    
with open("ColorDouble.txt", "r") as Color_2:  #open and read the text file
    C2 = Color_2.read()  #give the file a variable name 
    C2_Used = list(map(str,C2.split())) #individuals words
    
with open("AnimalSingle.Txt", "r") as Animal_1:  #open and read the text file
    A1 = Animal_1.read()  #give the file a variable name 
    A1_Used = list(map(str,A1.split())) #individuals words
    
with open("MovementDouble.Txt", "r") as Movement_2:  #open and read the text file
    M2 = Movement_2.read()  #give the file a variable name 
    M2_Used = list(map(str,M2.split())) #individuals words
    

def eng_haiku():
    print(random.choice(C1_Used).upper() + " " + "with " + random.choice(C2_Used) +  " " + random.choice(A1_Used).upper())
    print(random.choice(M2_Used) + "," + " " + random.choice(M2_Used) + "," + " and " + random.choice(M2_Used))
    print("enjoying their time")
    


# In[7]:


eng_haiku()


# In[28]:


import random

#number reponds to the amount of syllables needed for the haiku to work
# 5 7 5


with open("Colors_French.txt", "r") as CF:  #open and read the text file
    CF = CF.read()  #give the file a variable name 
    CF_Used = list(map(str,CF.split())) #individuals words
    
with open("Animals_French.txt", "r") as AF:  #open and read the text file
    AF = AF.read()  #give the file a variable name 
    AF_Used = list(map(str,AF.split())) #individuals words
    
with open("MovementFrancais.Txt", "r") as MovementF_2:  #open and read the text file
    M2_F = MovementF_2.read()  #give the file a variable name 
    M2F_Used = list(map(str,M2_F.split())) #individuals words
    

def french_haiku():
    animaux = random.choice(AF_Used)
    animaux_les = "les " + random.choice(AF_Used) #could be the same animal as the first line or a different one
    
    print(animaux_les + " " + random.choice(CF_Used) +  " et " + random.choice(CF_Used))
    print(animaux_les + " qui" + " " + random.choice(M2F_Used) + ", " + "" + random.choice(M2F_Used) +  " et " + random.choice(M2F_Used))
    print(animaux_les + " qui sont " + animaux)
    
    


# In[34]:


french_haiku()


# In[ ]:




