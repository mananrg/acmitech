import pandas as pd
from getpostsfromjson import get_postscount_and_posts,flesch,novelty_score,novelty_ratio,smog_index,text_standard,kincaid,coleman_liau,readability_index,dae_chall,linsear_write,gunning_fog
from getpostsfromjson import type_indicator_analyze_func,intro_extro_func,judging_func,lifestyle_func,perceiving_func
from vikash.app import json_file_session

username="Achin"
json_file_session='your_posts_1.json'
timestamp1 = "Nov 12 2019"
timestamp2 = "Jan 15 2020"

print("\nCalling get postcount and posts.............\n")
if json_file_session:
    count,postconcat,checkdate_list,scores,dictp,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer=get_postscount_and_posts(json_file_session,timestamp1,timestamp2)
print('\nProcessing the data.......\n')

scores_dict = {'Introvert': intro_extro_func(intro_extro)[0] , 'Extrovert':intro_extro_func(intro_extro)[1],
        'Judging': judging_func(judging_function)[0],'Perceiving':judging_func(judging_function)[1],
        'Feeling':lifestyle_func(lifestyle)[0],'Thinking':lifestyle_func(lifestyle)[1],
        'Sensing':perceiving_func(perceiving_function)[0],'Intuition':perceiving_func(perceiving_function)[1],
        'Flesch':flesch(scores),'Novelty Score':novelty_score(scores),'Novelty Ratio':novelty_ratio(scores),
        'Smog':smog_index(scores),'Kincaid':kincaid(scores),'Coleman':coleman_liau(scores),'Readability':readability_index(scores),
        'Dae Chall':dae_chall(scores),'Linsear Write':linsear_write(scores),'Gunning Fog':gunning_fog(scores)
        }

print('\nConverting into dataframe......\n')
df = pd.DataFrame(scores_dict)


print("************************************************************************************************************** \n")
print(df)
print("\n**************************************************************************************************************")


print('Converting into csv.......')
#os.chdir('data_score/')
df.to_excel('/var/www/html/data_score/'+username + '.xlsx',index=False)
print('You can now download the data at /var/www/html/data_score/'+ username)

