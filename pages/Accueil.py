import dash


#from dataclasses import dataclass
#from tokenize import group
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__, path='/', name='Accueil',order=1) 

#%%

LOGO = "../assets/table.jpeg"

#%%

layout = html.Div([
   # html.Img(src="https://images.pexels.com/photos/8353802/pexels-photo-8353802.jpeg",height="500px",width="1000",style={'opacity': 0.33}),
    html.Div([
        html.P("hidden text",style={'font-size':2,'visibility': 'hidden'}),
        html.P("Bienvenu !",
               style={'color': '#191970', 'text-decoration': 'none','background-color': '#8c8c8c','margin':'10px 0px 0px 740px','padding':'0px 100px 30px 30px','width':'400px','height':'35px',
                                                                  'font-style': 'bold','text-align':'left','opacity': '0.70','font-size':22}),
       
        
        html.P(["Vous êtes sur la page d'accueil de notre application dash qu'est crée à base de la bibliothèque dash en python ,l'objectif de cet application est visualisé une dataset(plus de 6400 lignes et 13 colonnes consernant le classement mondial des universités QS .",
               html.Br(),html.Br(),"On y affiche des informations telles que la distribution des universités dans chaque region,la meilleur université dans chaque année,l'évolution de nombre de faculté et le nombre des étudiantes internes selon les années et d'autre informations. ",html.Br(),html.Br(),"les graphes utilisées dans cette application dash sont :",html.Br(),"1.Bar chart",html.Br(), "2.Pie chart ",html.Br(),
               "3.Line chart",html.Br()," 4.Sunburst chart",html.Br(),"5.Area chart",html.Br(),"6.Treemap chart",html.Br(),"vous pouvez accéder à page 1 de notre dash-app via la bare de navigation ou en cliquant directement ci-dessous",html.Br(),html.A('Accès a Dash app..',href="/General",style={'color':'red','font-size':'20'})],             
               style={'color': '	white','background-color': 'grey' ,'opacity': '0.60', 'text-align':'auto','marginBottom': 0, 'marginTop': 10, 'marginRight': 0, 'marginLeft': 740,'padding':'7px 0px 10px 30px','width':'500px','height':'490px'}),
       # html.P(["vous pouvez accéder à page 1 de notre dash-app via la bare de navigation ou en cliquant directement ci-dessous",html.Br(),html.A('Accès a Dash app..',href="/Page1")])
        
        ],
    ),
       
    
   # html.Div([html.Img(src=LOGO,style={'opacity': 1})
        
            # ])
            #html.A('Accès a Dash app..',href="/Page1" ,style={'color': 'blue', 'text-decoration': 'none','background-color': 'white','margin':'0px 0px 0px 740px','padding':'0px 200px 10px 30px','width':'700px','height':'200px',
                                                              # 'font-style': 'italic','text-align':'left','opacity': '0.70'}),
        ],style={'background-image':'url(https://images.pexels.com/photos/8353802/pexels-photo-8353802.jpeg)','background-repeat': 'no-repeat',#'margin':'2S00px 4S00px 0px 740px'
                 'background-position': 'auto',
                 'background-size': '1500px 1000px',#'1500px 650px'
                 #'opacity' :'0.50',
                 'height':'600px'
                  })
#%%

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

