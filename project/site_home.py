# encoding: utf-8
# Version: V2022.07.19
# Author: wzyjsha@163.com


from config.config import *
from config.path import *
from site_component.style import *
from site_component.dash_modules import *


app = dash.Dash(__name__, requests_pathname_prefix='/', external_stylesheets=['flatly_bootstrap.min.css'])
app.title = 'Sunshine Home'


app.layout = html.Div([
    dbc.Container(fluid=True, style=bg_home_style, children=[
        dbc.Container(fluid=True, style=textbox_home_style, children=[
            dbc.Row([html.H1("SUNSHINE")], style={"font-family": "Microsoft YaHei UI, 华文隶书, Jokerman, Forte, Segoe Script"}),
            # dbc.Row([html.H3("May You Always Walk In Sunshine, May You Never Want For More.")]),
            dbc.Row([html.Br(), html.Br()]),
            html.Span([
                html.A(html.Img(src=IconLinkedin, height='20px'), href="https://www.linkedin.com/", style=badge_home_style),
                html.A(html.Img(src=IconGithub, height='20px'), href="https://github.com/", style=badge_home_style), 
                html.A(html.Img(src=IconEmail, height='20px'), href="mailto:wzyjsha@163.com", style=badge_home_style), 
            ]),
            dbc.Row([html.Br(), html.Br()]),
            html.Span([
                dbc.Badge("Home", external_link=True, href='/', pill=True, color="danger",style=badge_home_style),
                dbc.Badge("About", external_link=True, href='/about/', pill=True, color="warning",style=badge_home_style),
                # dbc.Badge("About", external_link=True, href='/about/', pill=True, color="info",style=badge_home_style),
            ])
        ])
    ])  
])


if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(host="127.0.0.1", port=8080, debug=True)