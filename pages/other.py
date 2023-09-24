# # Importation Librairies

# In[1]:

import pandas as pd
import dash


#from dataclasses import dataclass
#from tokenize import group
import plotly.express as px
from dash import Dash, dcc, html, Input, Output,callback
import dash_bootstrap_components as dbc

#app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__,name='Autres', path='/autres')

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
                                    "background-color": '#FFFFF0'})),
                dbc.Col(dcc.Dropdown(id='selectregion',
                             options=[{'label': x, 'value': x} for x in regions],
                             placeholder="Select a region...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#FFFFF0'})),
                dbc.Col(dcc.Dropdown(id='selectcountry',
                             options=[{'label': x, 'value': x} for x in countries],
                             placeholder="Select an Country...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#FFFFF0'})),
                dbc.Col(dcc.Dropdown(id='selecttype',
                             options=[{'label': i, 'value': i} for i in types],
                             placeholder="Select a type...",
                             multi=False,
                             style={"margin": "10px 10px 10px 0px",
                                    "background-color": '#FFFFF0'}))
                ]
            , style={"color" : "#191970"})

cards1 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description : L'objectif de ce figure est déterminé le pourcentage des universités selon le nombre des étudiants internationals dans chacune."),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
        ),
        width={'size': 6, "order": 1},
        ),
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description : Le but de ce graphe est affiché les trois universités qui sont classées parmis les premières dans chaque annee. "),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
            # className="mb-3 border border-secondary",
        ),
        width={'size': 6, "order": 1},
        )
    ]
)

graphes3 = dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph4'),
               width={'size': 6, "order": 1}, 
               style = {'border-style': 'hidden',#, 'border-color': 'gray'
                         'margin':'2px 0px 0px 0px' }
                ),
               dbc.Col(dcc.Graph(id = 'grph5'),
               width={'size': 6, "order": 2}, 
               style = {'border-style': 'hidden',#, 'border-color': 'gray'
                         'margin':'2px 0px 0px 0px' }
                )])
#########################
cards2 = dbc.Row(
    [
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description : L'objectif de ce graphe est décri l'évolution de nombre des facultés dans chaque région au cours des années."),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
        ),
        width={'size': 6, "order": 1},
        ),
      dbc.Col(
        dbc.Card(
            dbc.CardBody("Description : Le but de ce graphe est présenté les différents tailles et les différents niveaux de qualité de recherche  chaque université.  "),
            style={"background-color": '#f7f2ef', 'border-color': '#f7dfb3'}
            # className="mb-3 border border-secondary",
        ),
        width={'size': 6, "order": 1},
        )
    ],style={"margin-top": '10px'}
)

graphes4= dbc.Row([
               dbc.Col(dcc.Graph(id = 'grph6'),
               width={'size': 6, "order": 1}, 
               style = {'border-style': 'hidden', #'border-color': 'gray'
                         'margin':'2px 0px 0px 0px' }),
    
              dbc.Col(dcc.Graph(id = 'grph7'),
              width={'size': 6, "order": 2},
              style = {'border-style': 'hidden', #'border-color': 'gray'
                       'margin':'2px 0px 0px 0px'})
              ]
    )

#%%

layout = html.Div(children=[dropdowns,cards1,graphes3,cards2,graphes4])

#%%

@callback(
    [Output('grph4', 'figure'),
    Output('grph5', 'figure'),
     Output('grph6', 'figure'),
     Output('grph7', 'figure')
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
    df4 = df.groupby(['Region','Annee'])['Nbr faculte'].sum().reset_index()
    fig4=px.area(df4, x='Annee',y='Nbr faculte', color='Region',markers=True,color_discrete_sequence=px.colors.sequential.Plasma)
    fig4.update_layout(title= 
                      {
                          'text' : 'Nombre des Facultés par Années et Region',
                          'x' : 0.5,
                          'y':0.95,
                          'xanchor': 'center',
                          'yanchor': 'top'
                                                                  
                      })
    
    df5 = df.groupby(['Region','Recherche qualite','Taille']).count().reset_index()
    fig5 = px.sunburst(df5,path=['Region','Recherche qualite','Taille'],names="Universite",template = 'plotly_white',
                     
                   color_discrete_sequence=['#800020','#EDDDE1','#AD5C71',
                                            '#FF00FF','#CA97A4','brown']
                                            )
                 # hover_name="Region"
    fig5.update_layout(title= 
                      {
                           'text' : 'La taille et la Qualité de Recherche par Region',
                            'x' : 0.5,
                            'y':0.95,
                            'xanchor': 'center',
                            'yanchor': 'top'

                      })
    ###########################
    df6 = df.sort_values(['score','Annee'],ascending=False).groupby(['Annee']).head(3).reset_index()
    fig6 = px.bar(df6, x = 'Annee', y='score', color='Classement',orientation='v',barmode='group',hover_data=['Universite','Classement'],#color_discrete_sequence=px.colors.sequential.RdBu
               color_discrete_sequence= px.colors.sequential.Plasma_r   )
    fig6.update_layout(title= 
                      {
                           'text' : 'Classement des universités par Années et Rgions',
                            'x' : 0.5,
                            'y':0.95,
                            'xanchor': 'center',
                            'yanchor': 'top'

                      })
    
    df7 = df.groupby(['Effectif International','Region'])['Universite'].count().reset_index()
    fig7 = px.pie(df7, values= 'Universite', names = 'Effectif International',hole=.3,color_discrete_sequence=px.colors.sequential.amp)
    fig7.update_layout(title= 
                      {
                           'text' : 'Effectif des étudiants Internationals',
                            'x' : 0.5,
                            'y':0.95,
                            'xanchor': 'center',
                            'yanchor': 'top'

                      })
    
    
    return fig7,fig6,fig4,fig5
                     
#%%

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)
