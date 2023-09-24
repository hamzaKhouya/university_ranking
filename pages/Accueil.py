import dash


#from dataclasses import dataclass
#from tokenize import group
from dash import Dash, html
import dash_bootstrap_components as dbc

#app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__, path='/Accueil', name='Accueil',order=1) 

#%%

LOGO = "../assets/table.jpeg"

#%%

layout = html.Div([
   # html.Img(src="https://images.pexels.com/photos/8353802/pexels-photo-8353802.jpeg",height="500px",width="1000",style={'opacity': 0.33}),
    html.Div([
        html.P("hidden text",style={'font-size':2,'visibility': 'hidden'}),
        html.H1("World university ranking!",
               style={'color': '#191970', 'text-decoration': 'none','margin':'10px 0px 0px 740px','padding':'0px 100px 30px 30px','width':'400px','height':'35px',
                                                                  'font-style': 'bold','text-align':'left','opacity': '0.70','font-size':22})
        ],
    )],
    style={'background-image':'url(https://ik.imagekit.io/s1sp3stox/tr:h-748,w-1584,fo-auto/press-office/news-events/news/2021/06/QS_Ranking_Banner.jpg)','background-repeat': 'no-repeat',#'margin':'2S00px 4S00px 0px 740px'
                 'background-position': 'auto',
                 'background-size': '1500px 1000px',
                 'height':'600px'
                  })
# #%%

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)

