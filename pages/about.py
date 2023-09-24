# # Importation Librairies

# In[1]:

import pandas as pd
import dash


import plotly.express as px
from dash import Dash, dcc, html, Input, Output,callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

#app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


dash.register_page(__name__,name='Général',path='/General',order=2)

#%%%

data = pd.read_csv("./data/qs_university_ranking.csv",sep=";" )


countries = sorted(data['Pays'].unique())
regions = sorted(data['Region'].unique())
years = sorted(data['Annee'].unique())
types = sorted(data['type'].unique())

#%%



dropdowns = dbc.Row(
                [
                dbc.Col(dcc.Dropdown(id='selectyear',
                            options=[{'label': x, 'value': x} for x in years],
                            placeholder="Select a year...",
                            multi=False,
                            style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#e8eceb'})),
                dbc.Col(dcc.Dropdown(id='selectregion',
                             options=[{'label': x, 'value': x} for x in regions],
                             placeholder="Select a region...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#e8eceb'})),
                dbc.Col(dcc.Dropdown(id='selectcountry',
                             options=[{'label': x, 'value': x} for x in countries],
                             placeholder="Select an Country...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#e8eceb'})),
                dbc.Col(dcc.Dropdown(id='selecttype',
                             options=[{'label': i, 'value': i} for i in types],
                             placeholder="Select a type...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#e8eceb'}))
                ]
            , style={"color" : "#191970"})

card0 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description: "),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
        ),
        width={'size': 12, "order": 1})
    ]
)



graphes0 = dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph0'),
               width={'size': 12, "order": 1}, 
               style = {'border-style': 'hidden', #'border-color': 'gray'
                        'margin':'2px 0px 0px 0px'}
                )])

card1 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description: "),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
        ),
        width={'size': 12, "order": 1})
    ]
)



graphes4 = dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph8'),
               width={'size': 12, "order": 1}, 
               style = {'border-style': 'hidden', #'border-color': 'gray'
                        'margin':'2px 0px 0px 0px'}
                )])
#########################
card2 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description: "),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3', 'margin-top': '10px'}
        ),
        width={'size': 12, "order": 1})
    ]
)
graphes5= dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph9'),
               width={'size': 12, "order": 1}, 
               style = {'border-style': 'hidden', #'border-color': 'gray'
                        'margin':'2px 0px 0px 0px'}
                )])

#%%

layout = html.Div(children=[dropdowns,card0,graphes0,card1,graphes4,card2,graphes5])

#%%

@callback(
    [Output('grph0', 'figure'),
     Output('grph8', 'figure'),
    Output('grph9', 'figure') 
    ],
    [Input('selectyear','value'),
     Input('selectregion', 'value'),
    Input('selectcountry', 'value'),
    Input('selecttype', 'value')])

def update_graph(selected_year, selected_region, selected_country, selected_type):
    df = data
    if selected_year != None:
        df = df.loc[df['Annee']== selected_year]

        
    ##############
    if selected_region != None:
        df = df.loc[df["Region"] == selected_region]
  
    #####
    
    if selected_country != None:
        df = df[df['Pays'] == selected_country]

        
    #####
    if selected_type !=None:
        df = df.loc[df['type'] == selected_type]
        
    scatter = df.groupby(['Latitude','Longitude','Universite','Taille'])['type'].count().reset_index()
    mapsc = px.scatter_mapbox(scatter, lat="Latitude", lon="Longitude",color='Taille', hover_name="Universite",size='type',
                              size_max =10,color_continuous_scale=px.colors.cyclical.IceFire, zoom=5, height=600)
    mapsc = mapsc.update_layout(mapbox_style="open-street-map")
    
    #####
    table = df.iloc[:10]
    fig6 = go.Figure(data=[go.Table(
        columnwidth = [10,40,20,20],
    header=dict(values=list([ '<b>Classement</b>','<b>Nom Université</b>', '<b>Score</b>','<b>Année</b>', '<b>Pays</b>']),
                fill_color='#cc7a00',
                align='center'),
    cells=dict(values=[table.Classement,table.Universite, table.score, table.Annee, table.Pays],
               fill_color='lavender',
               height = 20,
               align='center'))
])
    fig6.update_layout(title= 
                       {
                            'text' : 'Liste des 10 premières Université',
                             'x' : 0.5,
                            'y':0.95,  
                           'xanchor': 'center',
                           'yanchor': 'top'

                      })
   
    
    
    
    
    ##########################
    
    df8=df.groupby(['Ville','Pays','Region'])['Universite'].count().reset_index().rename(columns={'Universite':"number of Universities"})
    fig7=px.treemap(df8,path=[px.Constant("word"),'Region','Pays','Ville'],color="number of Universities",color_continuous_scale='orRd',)
    fig7.update_layout(
        margin = dict(t=50, l=25, r=25, b=25),
        title= {
            'text' : 'the distribution of universities by city in each region',
             'x' : 0.45,
             'y':0.95,
             'xanchor': 'center',
             'yanchor': 'top'

                      })
    ###########################
    
    
    return mapsc,fig6,fig7
                     
# #%%

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)
