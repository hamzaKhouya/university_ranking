import dash 
import pandas as pd
import numpy as np
from dataclasses import dataclass
from tokenize import group
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
data = pd.read_csv("data/data.csv", sep=",")
data = data.loc[data["rank_display"].notnull()]
columns = ['score', 'international_students','city','research_output','type','rank_display','faculty_count','size']
for col in columns:
    data[col].replace(np.nan, data[col].value_counts().idxmax(), inplace=True)
data.drop(columns=['student_faculty_ratio'], inplace=True)
data.rename(columns ={'university' : 'Universite', 'year':'Annee', 'rank_display':"Classement", 
                      'country' : 'Pays', 'city' : 'Ville', 'region':'Region',
                       'research_output' : 'Recherche qualite',
                       'international_students' : 'Nbr etudiant intern', 'size' : 'Taille', 
                      'faculty_count': 'Nbr faculte'}, inplace =True)
data = data.loc[~data["Classement"].str.contains("-")]
for name in ["Nbr faculte","Nbr etudiant intern"]:
    data[name] = data[name].str.replace(',','.')
    data[name]=data[name].astype('float64')
countries = sorted(data['Pays'].unique())
regions = sorted(data['Region'].unique())
years = sorted(data['Annee'].unique())
types = sorted(data['type'].unique())
data['Recherche qualite'] = data['Recherche qualite'].replace(['Very high'],'Very High')


LOGO = "assets/qs.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("World Universities Ranking", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
        ]
    ),
    color="dark",
    dark=True,
)


dropdowns = dbc.Row(
                [
                dbc.Col(dcc.Dropdown(id='selectyear',
                            options=[{'label': x, 'value': x} for x in years],
                            placeholder="Select a year...",
                            multi=False,style={"margin": "10px"})),
                dbc.Col(dcc.Dropdown(id='selectregion',
                             options=[{'label': x, 'value': x} for x in regions],
                             placeholder="Select a region...",
                             multi=False,style={"margin": "10px"})),
                dbc.Col(dcc.Dropdown(id='selectcountry',
                             options=[{'label': x, 'value': x} for x in countries],
                             placeholder="Select an Country...",
                             multi=False,style={"margin": "10px"})),
                dbc.Col(dcc.Dropdown(id='selecttype',
                             options=[{'label': i, 'value': i} for i in types],
                             placeholder="Select a type...",
                             multi=False,style={"margin": "10px"}))
                ]
            )

graphes1 = dbc.Row([dbc.Col(dcc.Graph(id = 'grph1'),width={'size': 4, "order": 1}, 
                                 style = {'border-style': 'solid', 'border-color': 'gray'}),
                       dbc.Col(dcc.Graph(id = 'grph2'),width={'size': 4, "order": 2},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph3'),width={'size': 4, "order": 3},
                               style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph4'),width={'size': 4, "order": 4},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph5'),width={'size': 4, "order": 5},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph6'),width={'size': 4, "order": 6},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph7'),width={'size': 4, "order": 7},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),
                        dbc.Col(dcc.Graph(id = 'grph8'),width={'size': 4, "order": 8},
                              style = {'border-style': 'solid', 'border-color': 'gray'}),])
app.layout = html.Div(children=[navbar,dropdowns,graphes1])

@app.callback(
    [Output('grph1', 'figure'),
    Output('grph2', 'figure'),
    Output('grph3', 'figure'),
    Output('grph4', 'figure'),
    Output('grph5', 'figure'),
    Output('grph6', 'figure'),
    Output('grph7', 'figure'),
    Output('grph8', 'figure')],
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

        
    df1 = df.groupby(['Pays','type'])['Universite'].count().reset_index().rename(columns = {'Universite' : "number of Universities"})
    fig = px.bar(df1, x ='Pays', y = 'number of Universities', color="type", template = 'ggplot2', text_auto=True, title='Number Of Universities By Country',labels={"Pays":"Country","number of Universities":"Number Of Universities","type":"Type"})
    
    df2 = df.groupby('type')['Universite'].count().reset_index().rename(columns = {'Universite' : "valeur"})
    fig1 = px.pie(df2, values = 'valeur', names = 'type', template = 'ggplot2', title='Percentage Of Universities By Type',labels={"valeur":"Number of universities","type":"Type"})
    
    df3 = df.groupby(['Region','type'])['Universite'].count().reset_index().rename(columns = {'Universite' : "number of Universities"})
    fig2 = px.bar(df3, x ='Region', y = 'number of Universities', color='type', template = 'ggplot2', text_auto=True, title='Number Of Universities By Region',labels={"number of Universities":"Number Of Universities","type":"Type"})

    df4 = df.groupby('Recherche qualite')['Universite'].count().reset_index().rename(columns = {'Universite' : "valeur"})
    fig3 = px.pie(df4, values = 'valeur', names = 'Recherche qualite', template = 'ggplot2', title='Percentage Of Universities By Research Output',labels={"valeur":"Number Of Universities","Recherche qualite":"Research Output"})

    df5 = df.groupby('Taille')['Universite'].count().reset_index().rename(columns = {'Universite' : "valeur"})
    fig4 = px.pie(df5, values = 'valeur', names = 'Taille', template = 'ggplot2', title='Percentage Of Universities By Size',labels={"valeur":"Number Of Universities","Taille":"Size"})

    df6 = df.groupby(['Region','type'])['Nbr etudiant intern'].mean().reset_index()
    fig5 = px.bar(df6, x ='Region', y = 'Nbr etudiant intern', color="type", template = 'ggplot2', text_auto=True, title='Number Of International Students By Region',labels={"Nbr etudiant intern":"Number Of International Students","type":"Type"})

    fig6 = px.bar(df, x = 'Universite', y = 'Classement', color="type", template = 'ggplot2', title='Classement Of Universities',labels={"type":"Type","Universite":"University"})

    df7 = df.groupby(['Universite','type'])['Nbr faculte'].mean().reset_index()
    fig7 = px.bar(df7, x ='Universite', y = 'Nbr faculte', color="type", template = 'ggplot2', text_auto=True, title='Faculty Count By University',labels={"Nbr faculte":"Faculty Count","type":"Type","Universite":"University"})

    return fig, fig1, fig2, fig3, fig4, fig5, fig6, fig7

if __name__ == '__main__':
    app.run_server(debug=True)