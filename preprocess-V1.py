
# coding: utf-8

# In[1]:


import pandas as pd
import os,re


# In[2]:


dir_path = os.getcwd()
dataf = pd.read_excel(os.path.join(dir_path,'Kishori_Entity_Symptom_etc.xls'))


# In[64]:


# keys = dataf.at[0,'KeyTerms']
# keys


# In[87]:


def proc_keys(keys):
    key_list = re.findall('\((.*?)\)',keys)
#     print("earlier - ",len(key_list))
    '''if(len(key_list) > 10): #take first 10% of the keys
        num = 0.1 * len(key_list)
        num = int(num)
        key_list = key_list[:num]'''
    if(len(key_list) > 10):
        key_list = key_list[:10]
#     print("after - ",len(key_list))
#     print(key_list)
    return key_list

def proc_symptoms(symptoms):
    sym_list = symptoms.lstrip("[]").rstrip("]").split(",")
#     print(len(sym_list[0]))
    if(len(sym_list)==1 and len(sym_list[0])==0):#if condition to check empty symptom
#         print("True")
        sym_list[0]="empty"
    if (len(sym_list) > 10):
        sym_list=sym_list[:10]
#     print(len(sym_list))
#     print(sym_list)
    return sym_list


# In[114]:


# dataf[['KeyTerms','SYMPTOM']]
# for (keys, symptoms) in dataf.itertuples(index=False):
i = 1     #doc number
for keys, symptoms in zip(dataf.KeyTerms, dataf.SYMPTOM): # to run on tuples; each tuple contains a doc info.
    file1 =  'data/'+str(i)+'-keys.csv' 
    file2 = 'data/'+ str(i) +'-edges.csv' 

    with open(file1,'w') as keyFile, open(file2, 'w') as edgeFile: 
        print("doc Number - ",i)
        key_list = proc_keys(str(keys))
#         print("String",symptoms) 
        sym_list = proc_symptoms(symptoms)
        print("#keys:",len(key_list)," #symptoms:",len(sym_list))
        
        j=1                            #key and symptom number in a doc
        
        keyFile.write("id, label, TF\n")
        for each_key in (key_list): # for over each key in a doc
            keyFile.write(str(j))                                 # print key id
            keyFile.write(", ")                                    
            key = each_key.split(",")[0].lstrip("u'").rstrip("'")  
            keyFile.write(key)                                     # write key label
            keyFile.write(", ")                                      
            keyFile.write(each_key.split(",")[1])                   #write term frequency
            keyFile.write("\n")
            j=j+1
        for each_sym in sym_list:
            keyFile.write(str(j))                                 # print key id
            keyFile.write(", ** ")                                    
            keyFile.write(each_sym)                                     # write key label
            keyFile.write(", ")                                      
            keyFile.write("0")                   #write term frequency
            keyFile.write("\n")
            j=j+1
        
        i=i+1
        edgeFile.write("Source, Target\n")
             
        for a in range(len(key_list)):
            for b in range(len(sym_list)):
                print(a+1,(len(key_list))+b+1)
                edgeFile.write(str(a+1))
                edgeFile.write(", ")
                edgeFile.write(str(len(key_list)+b+1))
                edgeFile.write("\n")
    
        print("-------------------------------")
    
#         k.write(keys)
#         s.write(symptoms)
        


# In[42]:


'''import re
line = str([(u'excessive errors', 0.25), (u'flash drive', 0.25), (u'1311a flash drive', 0.25), 
            (u'user responsein', 0.125), (u'click troubleshooting', 0.125), (u'management gui', 0.125), 
            (u'next level', 0.08333333333333333), (u'error event ids', 0.0625), (u'parent topic', 0.0625), 
            (u'error codes', 0.0625)])
# matches = re.findall('( (.*) )', line, re.DOTALL)
# print(matches)
                
print(type(line))
# s[s.find("(")+1:s.find(")")]
k = proc_keys(line)
with open('demo','w') as ff:
    for a in k:
        print(a)
        ff.write(a)
        ff.write("\n")'''

