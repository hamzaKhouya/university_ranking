# # Importation Librairies

# In[1]:

import pandas as pd
import dash


#from dataclasses import dataclass
#from tokenize import group
import plotly.express as px
from dash import Dash, dcc, html, Input, Output,callback
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, name='Universités', path='/Universites', order=3)

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
                                    "background-color": 'white'})),
                dbc.Col(dcc.Dropdown(id='selectregion',
                             options=[{'label': x, 'value': x} for x in regions],
                             placeholder="Select a region...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": 'white'})),
                dbc.Col(dcc.Dropdown(id='selectcountry',
                             options=[{'label': x, 'value': x} for x in countries],
                             placeholder="Select an Country...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": 'white'})),
                dbc.Col(dcc.Dropdown(id='selecttype',
                             options=[{'label': i, 'value': i} for i in types],
                             placeholder="Select a type...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": 'white'}))
                ]
            , style={"color" : "#191970"})



############################

graphes1 = dbc.Row([
                   dbc.Col(dcc.Graph(id = 'grph1'),
                   width={'size': 6, "order": 1}, 
                   style = {'border-style': 'hidden',# 'border-color': 'gray'
                            'margin':'2px 0px 0px 0px'}
                    ),
                   dbc.Col(dcc.Graph(id = 'grph2'),
                   width={'size': 6, "order": 2}, 
                   style = {'border-style': 'hidden', #'border-color': 'gray'
                   'margin':'2px 0px 0px 0px'})])
#########################
cards1 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description:Ce figure présente le nombre des universités publiques et privées dans chaque pays. "),
            style={"background-color": '#F8F8F8', 'border-color': '#F8F8F8'}
        ),
        width={'size': 6, "order": 1},
        ),
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description:Ce figure présente l'évolution de nombre des universités selon les années. "),
            style={"background-color": '#F8F8F8', 'border-color': '#F8F8F8'}
            # className="mb-3 border border-secondary",
        ),
        width={'size': 6, "order": 1},
        )
    ]
)

###########################

graphes2 = dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph3'),
               width={'size': 6, "order": 1}, 
               style = {'border-style': 'hidden', #'border-color': 'gray'
                        'margin':'2px 0px 0px 0px'}),
    
              dbc.Col(dcc.Graph(id = 'grph'),
              width={'size': 6, "order": 2},
              style = {'border-style': 'hidden',# 'border-color': 'gray'
                       'margin':'2px 0px 0px 0px'})])
#############################

cards2 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description: Pourcentage des universités selon le nombre des facultés dans chacune"),
            style={"background-color": '#F8F8F8', 'border-color': '#F8F8F8'}
        ),
        width={'size': 6, "order": 1},
        ),
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description:L'objectif de graphe est faire une comparaison entre le nombre des universités publiques et privées dans chaque region "),
            style={"background-color": '#F8F8F8', 'border-color': '#F8F8F8'}
            # className="mb-3 border border-secondary",
        ),
        width={'size': 6, "order": 1},
        )
    ],style={"margin-top": '10px'}
)

#%%

layout = html.Div(children=[dropdowns,cards1,graphes1,cards2,graphes2])

#%%

@callback(
    [Output('grph1', 'figure'),
    Output('grph2', 'figure'),
     Output('grph3', 'figure'),
     Output('grph', 'figure')
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

    #####
    df1 = df.groupby(['Pays','type'])['Universite'].count().reset_index().rename(columns = {'Universite' : "number of Universities"})
    fig = px.bar(df1, x ='Pays', y = 'number of Universities',color='type' ,orientation='v',barmode='overlay',
                  color_discrete_map={'Public':'#B8B387','Private':'orange'},opacity=0.9,#template='plotly_dark'
                  )
    fig.update_layout(title= 
                      {
                          'text' : 'Nombre des Universités par Pays',
                          'x' : 0.5,
                          'y':0.9,
                          'xanchor': 'center',
                          'yanchor': 'top'
                        
                      })
      #####               
    
    df2 = df.groupby(['Annee'])['Universite'].count().reset_index().rename(columns = {'Universite' : "valeur"})
    fig1 = px.pie(df2, values = 'valeur', names = 'Annee',
                 color_discrete_sequence=['orange','#B8B387'])
    
    fig1.update_layout(title= 
                      {
                          'text' : 'Nombre des Universités par Années',
                          'x' : 0.5,
                          'y':0.95,
                          'xanchor': 'center',
                          'yanchor': 'top'
                        
                      })
    
    df3 = df.groupby(['type','Nombre de Facultes'])['Universite'].count().reset_index().rename(columns = {'Universite' : "valeur"})
    fig2 = px.pie(df3, values = 'valeur', names = 'Nombre de Facultes',#template = 'plotly_dark'
                 color_discrete_sequence=['orange','#B8B387'])
    
    fig2.update_layout(title= 
                      {
                          'text' : 'Pourcentage des Universités par Nombre des Facultés',
                          'x' : 0.5,
                          'y':0.95,
                          'xanchor': 'center',
                          'yanchor': 'top'
                        
                      })
    
     
    #####
    
    df4 = df.groupby(['Region','type'])['Universite'].count().reset_index().rename(columns={'Universite':"number of Universities"})
    fig3 = px.bar(df4, x ='Region', y = 'number of Universities', color='type',barmode='group',
                 orientation="v", color_discrete_map={'Public':'#B8B387','Private':'orange'},opacity=0.9,#template='plotly_dark'
                 )
    
    fig3.update_layout(title= 
                      {
                          'text' : 'Nombre des Universités par Region',
                          'x' : 0.5,
                          'y':0.95,
                          'xanchor': 'center',
                          'yanchor': 'top'
                        
                      })
    
    return fig,fig1,fig2,fig3
                     
#%%

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
