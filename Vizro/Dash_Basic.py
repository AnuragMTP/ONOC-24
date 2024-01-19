# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:24:04 2024
@author: anura
Time to learn some Vizro
Vizro is a visualisation library. 
Sitting on top of dash and plotly. 
So learning it is going to start 
with trying dash first.

"""

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

#Getting data
df=pd.read_csv(r'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#Init app
app=Dash(__name__)

#Defining layout
app.layout=html.Div([html.Div(children='Data on browser with buttons'),
                     html.Hr(),
                     dcc.RadioItems(options=['pop','lifeExp','gdpPercap'],value='lifeExp',id='control-item'),
                    dash_table.DataTable(data=df.to_dict('records'),page_size=5),
                    dcc.Graph(figure={},id='control-graph')])

#Controls to build the inertaction
@callback(Output(component_id='control-graph', component_property='figure'),
        Input(component_id='control-item',component_property='value')
        )
def update_graph(col):
    fig=px.histogram(df,x='continent',y=col, histfunc='avg')
    return fig

#Running the app
if __name__ =='__main__':    
    app.run(port=8090,debug=True)