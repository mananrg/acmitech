import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
#from getpostsfromjson import
import getpostsfromjson
from getpostsfromjson import post_count,text_standard,novelty_score,novelty_ratio
from plotly.subplots import make_subplots


pjson_file='your_posts_1.json'
ptimestamp1 = "Dec 12 2019"
ptimestamp2 = "Jan 15 2020"

pcount,ppostconcat,pcheckdate_list,scores,dictp=getpostsfromjson.get_postscount_and_posts(pjson_file,ptimestamp1,ptimestamp2)
novelty_score_list=novelty_score(scores)
novelty_ratio_list=novelty_ratio(scores)*1000
print("Novelty Ratio")
print(novelty_ratio_list)
print("Checkdate_List")
print(len(pcheckdate_list))
print(len(novelty_score_list))
print(len(novelty_ratio_list))
#novelty_ratio_list=novelty_ratio(scores)
#finaldatelist,post_count= post_count(pcheckdate_list)
#print(len(post_count))
#child_post_count=[1,3,2,1,1,2,0,1,1,2,2,1,0,1,2]
#parents_score=[2.2,5.2,13,3.3,4.6,5,7.2,8,4.7,2.8,4.1,6.6,8.1,3,4.1]
#child_score=[2.6,3.4,1.1,5.3,2.6,6,2.6,4,5,3.7,6.8,5.52,4.1,5,3.1]
#teach_post_count=[5,2,3,2,4]
#teach_score=[4,6,12,2,5]
#novelty_ratio=[0.3,0.2,0.6,1,0.4]
#labels=[10,24,30,45,15]
#post_count=[2,4,1,3,2,4,1,4,3,2,4,1,5,2,1,1,2,3]
#no_of_days=[2,4,6,8,10]

np.random.seed(42)
x_random=np.arange(13)
y_random=np.random.randn(100)
x0=go.Scatter(x=pcheckdate_list,y=novelty_score_list,mode='markers+lines',line_shape='spline',name='Novelty Score',marker=dict(color='blue'))

#x0=go.Scatter(x=pcheckdate_list,y=(x_random**2),mode='markers+lines',line_shape='spline',name='Parents Post Count',marker=dict(color='blue'))
x1=go.Scatter(x=pcheckdate_list,y=novelty_ratio_list,mode='markers+lines',line_shape='spline',name='Novelty Ratio[0-1000]')
#x2=go.Scatter(x=finaldatelist,y=child_post_count,mode='markers+lines',line_shape='spline',name='Children Post Count')
#x3=go.Scatter(x=finaldatelist,y=child_score,mode='markers+lines',line_shape='spline',name='Childrens post readability score')
#x4=go.Scatter(x=finaldatelist,y=teach_post_count,mode='markers+lines',line_shape='spline',name='Teacher Post Count')
#x5=go.Scatter(x=finaldatelist,y=teach_score,mode='markers+lines',line_shape='spline',name='Readability score[0-13]')
#x6=go.Scatter(x=finaldatelist,y=novelty_ratio,mode='markers+lines',line_shape='spline',name='Novelty Score[0-1]')
#x7=go.Scatter(x=no_of_days,y=post_count,mode='markers+lines',line_shape='spline',name='Post Count')
#x8=go.Scatter(x=no_of_days,y=labels,mode='markers+lines',line_shape='spline',name='Violent label count')

app=dash.Dash()
app.layout=html.Div([
    html.Div([dcc.Graph(id='Plot',figure={
    'data':[x0,x1],
    
    'layout':go.Layout(title='Plot',xaxis=dict(title='No of Days'),yaxis=dict(title="Novelty Score"))

    }
    )])
    ])
"""

app.layout=html.Div([
   html.Div([
       dcc.Graph(
          figure={
              'data':[x0]
              }
           )
       ]),
   html.Div([
        dcc.Graph(
          figure={
              'data':[x0]
              }
           )

       ])   
    ])
"""
if __name__=='__main__':
    app.run_server(host='0.0.0.0',port=6008)
