import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality

datastore=""
def get_postscount_and_posts(json_file,timestamp1,timestamp2):
 with open(json_file) as f:
   datastore = json.load(f)
#print(datastore) 
 i=0
 print("11111111111111111111111111111!!!!!1111")
 checkdate_list=[]
 judging_function=[]
 lifestyle=[]
 perceiving_function=[]
 type_indicator_analyzer=[]
 count_of_posts=0
 str_to_return=""
 scores=[]
 intro_extro=[]
 len_datastore=len(datastore)
 while(i<len(datastore)) :
   try: 
    string_for_api_calls=datastore[i]["data"][0]["post"]
    #print("post is")
    #print(string_for_api_calls)
    time_stamp=datastore[i]["timestamp"]
    #print(time_stamp)
    #timestamp1 = "Dec 12 2019"
    #timestamp2 = "Jan 15 2020"
    check = datetime.fromtimestamp(time_stamp)
    print(check)
    t1 = datetime.strptime(timestamp1, "%b %d %Y")
    t2 = datetime.strptime(timestamp2, "%b %d %Y")
    t1date=t1.date()
    t2date=t2.date()
    checkdate=check.date()
    print("222222222222222222222222222222222222222")
    if checkdate>t1date:
        print("Inside t1")
        if checkdate<t2date:
            print("Inside t2")
            s1 = checkdate.strftime("%m/%d/%Y")
            print("s1:", s1)
            checkdate_list.append(s1)
            #print(checkdate_list)
            count_of_posts=count_of_posts+1
            #print("count",count_of_posts)
            #str_to_return=str_to_return+"."+string_for_api_calls
            str_to_return=string_for_api_calls
            print(type(str_to_return))
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            scores.append(json.loads(return_scores_from_text_only.ret_scores_res(str_to_return)))
            print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
            print("in am in try for personality appending in scores")
            
            intro_extro.append((personality.intro_extro(str_to_return))) 
            print(intro_extro)
            print("333333333333333333333333333333333333333333333333333333333333333333333")
            
            judging_function.append((personality.judging_function(str_to_return)))
            lifestyle.append((personality.lifestyle(str_to_return)))
            perceiving_function.append((personality.perceiving_function(str_to_return)))
            type_indicator_analyzer.append((personality.type_indicator_analyzer(str_to_return)))
            
   except:
       #print("inside exception")
       pass
   i+=1
   #print(checkdate_list)
 print("44444444444444444444444444444444444444444")
 dictp={}
 for eachelem in checkdate_list:
     post_c=0
     if checkdate_list.count(eachelem)>1:
         dictp['post_c_associated_with'+eachelem]=checkdate_list.count(eachelem)

 print("dictionary associated with post count is")
 print(dictp)
 print(scores)
 print("**"*64)    
 print("Into-Extro")
 print(intro_extro)
 print("--"*64)
 print("judging function")
 print(judging_function)
 print("--"*64)
 print("lifestyle")
 print(lifestyle)
 print("--"*64)
 print("perceiving function")
 print(perceiving_function)
 print("--"*64)
 print("type_indicator_analyzer")
 print(type_indicator_analyzer)
 print("**"*64)
 #print(len(str_to_return))
 #print(count_of_posts)
 
 return count_of_posts,str_to_return,checkdate_list,scores,dictp,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer
 
def intro_extro_func(scores):
    intro=[]
    extro=[]
    for i in scores:
        x=(i['Extraversion'])
        intro.append(x)
        y=(i['Introversion'])
        extro.append(y)
    #print("INTRO")
    #print(intro)
    #print("EXTRO")
    #print(extro)
    return intro,extro


def judging_func(scores):
    feeling=[]
    thinking=[]
    for i in scores:
        x=(i['Feeling'])
        feeling.append(x)
        y=(i['Thinking'])
        thinking.append(y)
    #print("Feeling")
    #print(feeling)
    #print("Thinking")
    #print(feeling)
    return feeling,thinking

def lifestyle_func(scores):
    judging=[]
    perceiving=[]
    for i in scores:
        x=(i['Judging'])
        judging.append(x)
        y=(i['Perceiving'])
        perceiving.append(y)
    #print("judging")
    #print(judging)
    #print("perceiving")
    #print(perceiving)
    return judging,perceiving

def perceiving_func(scores):
    sensing=[]
    intuition=[]
    for i in scores:
        x=(i['Sensing'])
        sensing.append(x)
        y=(i['iNtuition'])
        intuition.append(y)
    #print("sensing")
    #print(sensing)
    #print("intuition")
    #print(intuition)
    return sensing,intuition


def type_indicator_analyze_func(scores):
    x=['ENFJ','ENFP','ENTJ','ENTP','ESFJ','ESFP','ESTJ','ESTP','INFJ','INFP','INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP']
    #ENFJ,ENFP,ENTJ,ENTP,ESFJ,ESFP,ESTJ,ESTP,INFJ,INFP,INTJ,INTP,ISFJ,ISFP,ISTJ,ISTP=([] for i in range(16))
    df=pd.DataFrame(scores)
    compile_list=[df[i].tolist() for i in x]
    # for i in x:
        
    #     i=df[i].tolist()
    #     compile_list.append(i)
        
    #     return compile_list
    #print(compile_list)
    return compile
    
        

def novelty_score(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['novelty_score'])
            #print('*'*60)
            li.append(x)       
        except:
            print("Exception")

    print("Novelty Score")
    print(li)
    return li

def text_standard(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['text_standard'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Text Standard Score")        
    print(li)
    return li

def novelty_ratio(scores):
    old_li=[]
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['novelty_ratio'])
            #print('*'*60)
            old_li.append(x)
        except:
            print("Exception")
    print("Novelty Ratio Score")
    print(old_li)
    return old_li

def readability_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['readability_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Readability Index")
    print(li)
    return li

def flesch(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['flesch'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Flesch Score")
    print(li)
    return li

def smog_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['smog_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Smog Index")
    print(li)
    return li

def kincaid(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['kincaid'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Kincaid")
    print(li)
    return li

def coleman_liau(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['coleman_liau'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Coleman Liau")
    print(li)
    return li

def readability_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['readability_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Readability Index")
    print(li)
    return li

def dae_chall(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['dae_chall'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Dae Chall")
    print(li)
    return li

def linsear_write(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['linsear_write'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Linsear Write")
    print(li)
    return li

def gunning_fog(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['gunning_fog'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Gunning Fog")
    print(li)
    return li

def post_count(date):
    """
    Input=Date list
    Output=PostCount and vivid dates from the date list
    """
    date_copy=date
    final_date_list = list(dict.fromkeys(date_copy))
    post_count=[]
    for i in final_date_list:
        count=date.count(i)
        post_count.append(count)
    return final_date_list,post_count
#flesch(scores)
#novelty_score(scores)
#novelty_ratio(scores)
#smog_index(scores)
#text_standard(scores)
#kincaid(scores)
#coleman_liau(scores)
#readability_index(scores)
#dae_chall(scores)
#linsear_write(scores)
#gunning_fog(scores)
