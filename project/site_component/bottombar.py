# encoding: utf-8
# Version: V1.0
# Date: 2022.07.20
# Author: wzyjsha@163.com

from config.path import *
from site_component.style import *
from site_component.dash_modules import *


bottom_content = html.P(style={"margin-bottom": "0px"}, children=
    'Copyright © 2022 | Young'
)



def make_bottombar():

    bottombar = [
        dbc.Row(align="center", justify="center", children=[bottom_content])
    ]

    return bottombar
