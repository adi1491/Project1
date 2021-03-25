import pickle
import pandas as pd
import webbrowser
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
project_name = "Word Cloud"

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")



def create_app_ui():
    global project_name
    main_layout = dbc.Container(
            
        dbc.Jumbotron(
                [
                 html.Marquee(id='text',children='These are the most used words in the etsy reviews!! ',style = {'width':'100%', 'height':30,'color':'orange'}),    
            html.H1(id = 'heading', children = project_name, className = 'display-3 mb-4',style={}),
                    html.Div([
            html.Img(src = app.get_asset_url('text_cloud.png'))]),
           
            ]
                        
                
                ),
        className = 'mt-4'
        )

    return main_layout


    
def main():
    global app
    global project_name
    
    open_browser()
    app.layout = create_app_ui()
    app.title = project_name
    app.run_server()
    app = None
    project_name = None
if __name__ == '__main__':
    main()