# encoding: utf-8
# Version: V1.1
# Date: 2022.07.20
# Author: wzyjsha@163.com


from config.path import *
from site_component.style import *
from site_component.dash_modules import *


# ----------Config the Navbar Information---------- #
LOGO = 'assets/logo/Plotly_Dash_logo.png'
BRAND_HOME = 'Brand'

# Navbar Item, Sequence: Left → Right
NAV_1 = {"Name": "Home  ", "Link": "/"}
NAV_2 = {"Name": "About  ", "Link": "/about/"}
# NAV_3 = {"Name": "", "Link": ""}
# NAV_4 = {"Name": "", "Link": ""}
# NAV_5 = {"Name": "", "Link": ""}

# ------------------------------------------------- # 


def make_navbar():

    navbar = dbc.Navbar(
        dbc.Container(style={"justify-content": "space-between"}, children =[
            html.A(
                dbc.Row(className="g-0", align="center", children=[
                    dbc.Col(html.Img(src=LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand(BRAND_HOME, className="ms-2", style={"font-size": "1.4em"})),
                ]),
                href="/",
                style={"text-decoration": "none"},
            ),
            dbc.Nav(style={"padding": "0px", "margin": "0px"}, justified=True,children=[
                dbc.NavItem(dbc.NavLink(NAV_1['Name'], href=NAV_1['Link'], style=navitem_style, external_link=True)),
                dbc.NavItem(dbc.NavLink(NAV_2['Name'], href=NAV_2['Link'], style=navitem_style, external_link=True)),
                # dbc.DropdownMenu(label="Dropdown", nav=True, style=navitem_style, children=[
                #     dbc.DropdownMenuItem("Item 1"), 
                #     dbc.DropdownMenuItem("Item 2")
                # ]),
            ]),
            html.Span(style={"padding-left": "9rem"} ,children=[
                html.A(html.Img(src=IconLinkedin, height='13px'), href="https://www.linkedin.com/", style=badge_navbar_style),
                html.A(html.Img(src=IconGithub, height='13px'), href="https://github.com/", style=badge_navbar_style), 
                html.A(html.Img(src=IconEmail, height='13px'), href="mailto:wzyjsha@163.com", style=badge_navbar_style),
            ]),
        ]),
        color="primary", 
        dark=True,
        fixed="top"
    )

    return navbar


""" The Usage of make_navbar Function

dbc.Row(id='navbar')

@app.callback(
    dd.Output('navbar', 'children'),
    dd.Input('navbar', 'id')
)
def update_navbar(n):
    nanvar = make_navbar()
    return nanvar
"""
