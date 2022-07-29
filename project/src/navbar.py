import pymysql
import pandas as pd

import dash_html_components as html
import dash_bootstrap_components as dbc

# from config import navbar_file, APP_TITLE, LOGO
APP_TITLE = 'Home'
navbar_file = r"C:\\Users\\zachary\\Desktop\\dash-template\\project\\resources\\navbar.xlsx"
LOGO = r'C:\\Users\\zachary\\Desktop\\dash-template\\project\\resources\\logo\\UM.png'


def query_db(database, username, password, hostname, port, query):
    """
    Input: database, username, passward, hostname: str
    Output: pd.Dataframe with display all columns
    """

    connection = pymysql.connect(db=database, user=username, password=password, host=hostname, port=port)
    with connection:
        with connection.cursor(pymysql.cursor.DictCursor) as cursor:  # return query containing fields
            cursor.execute(query)
            query_result = pd.DataFrame(cursor.fetchall())
    
    pd.set_option('display.max_columns', None)  # set to display all columns
    
    return query_result


def get_navbar_dropdowns(navbar_file):
    
    df_nav = pd.read_excel(navbar_file)
    df_nav = df_nav[df_nav.is_deleted == 0]
    nav_item_list = []
    df_nav = df_nav.sort_values('order_level1')

    for lv1 in df_nav.level_1.unique():
        df_lv1 = df_nav[df_nav.level_1 == lv1]
        if (df_lv1.shape[0]==1) &  (df_lv1.iloc[0]['single_item']==1):
            nav_item_list.append([
                dbc.NavItem(dbc.NavLink(
                    children=df_lv1.iloc[0]['level_1'], href=df_lv1.iloc[0]['link'], external_link=True))
            ])
        else:
            df_lv1 = df_lv1.sort_values('order_level2')
            dropdown_children = [dbc.DropdownMenuItem(lv1, header=True)]

            for idx, r in df_lv1.iterrows():
                dropdown_children.append(dbc.DropdownMenuItem(
                    children=r['level_2'], href=r['link'], external_link=True))
            nav_item_list.append([
                dbc.DropdownMenu(children=dropdown_children, nav=True, in_navbar=True, label=lv1, right=False)
            ])

    return nav_item_list


def make_navbar():

    nav_dropdown_func = get_navbar_dropdowns(navbar_file)
    nav_item_lists = []
    for n in nav_dropdown_func:
        nav_item_lists = nav_item_lists + n

    return dbc.Navbar(
        children=dbc.Container([
            html.A(
                dbc.Row(
                    [dbc.Col(html.Img(src=LOGO, height="30px"), width={'size': 5})],
                    align='center',
                    no_gutters=True,
                ), href="/",  # 电击logo跳转的地址
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                id="navbar-collapse",
                children=[
                    dbc.Col(dbc.NavbarBrand(APP_TITLE, className="ml-4"), width={'size': 3}),
                    dbc.Nav(nav_item_lists, className="ml-auto", navbar=True)
                ],
                navbar=True,
                style=dict(color="#c9170a")
            )
        ], fluid=True),
        tag='nav',
        dark=True,
        fixed="top",
        expand='lg',
        color="#c9170a",
        style={"border": 'none'}
    )


# navvar = make_navbar()











