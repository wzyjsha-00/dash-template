# encoding: utf-8
# Version: V1.1
# Date: 2022.07.20
# Author: wzyjsha@163.com


from site_component import *
from config.config import *
from site_component.style import *
from site_component.dash_modules import *
from site_component.navbar import make_navbar
from site_component.bottombar import make_bottombar


app = dash.Dash(__name__, requests_pathname_prefix='/about/', external_stylesheets=['bootstrap.min.css'])
app.title = 'About'


content = [
    dbc.Container(
        children=[
            html.H1("Please wrire the content here.")
        ]
    )
]


app.layout = html.Div([
    dbc.Container(fluid=True, id='navbar', style=navbar_box_style),
    dbc.Container(fluid=True, style=bg_normal_style, children=[
        dbc.Container(fluid=True, style=textbox_normal_style, children=[
            # Add Content Here
            dbc.Row(children=content),
            dbc.Row(children=content),
            dbc.Row(children=content),
            dbc.Row(children=content),
            dbc.Row(children=content),
            dbc.Row(children=content),
            dbc.Row(children=content),
        ]),
        dbc.Container(style=bottombar_style, children=make_bottombar())
    ])
])


@app.callback(
    dd.Output('navbar', 'children'),
    dd.Input('navbar', 'id')
)
def update_navbar(n):
    nanvar = make_navbar()
    return nanvar


if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(host="127.0.0.1", port=8080, debug=True)