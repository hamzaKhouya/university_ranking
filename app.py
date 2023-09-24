import dash
import dash_bootstrap_components as dbc
from dash import Dash, html

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR])
server = app.server
#%%
LOGO = "./assets/qs.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("World Universities Ranking", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/Accueil",
                style={"textDecoration": "none"},
            ),
            dbc.Nav(
                [
                  dbc.Col(dbc.NavItem(dbc.NavLink(page["name"], href=page["path"], style={'color': 'white'})))
                    for page in dash.page_registry.values()
                ]),
        
        ]
    ),
    color="#cc7a00",
    dark=True,
)

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container
    ],
    fluid=False,
    style={'background-color': 'black'}
)
#%%%

if __name__ == "__main__":
    app.run(debug=True)
