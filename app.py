# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

Sw=[]

Sw.append(pd.read_csv('Sw0.csv'))
Sw.append(pd.read_csv('Sw1.csv'))
Sw.append(pd.read_csv('Sw2.csv'))
Sw.append(pd.read_csv('Sw3.csv'))
Sw.append(pd.read_csv('Sw4.csv'))

for i in range(len(Sw)):
    Sw[i].ControlPosition.loc[Sw[i].ControlPosition == "Links in controle"] = -1
    Sw[i].ControlPosition.loc[Sw[i].ControlPosition == "Rechts in controle"] = 1
    Sw[i].ControlPosition.loc[Sw[i].ControlPosition == "Uit controle"] = 0
    Sw[i].SteeringCommand.loc[Sw[i].SteeringCommand == "Sturing Links"] = -1
    Sw[i].SteeringCommand.loc[Sw[i].SteeringCommand == "Sturing Rechts"] = 1
    Sw[i].SteeringCommand.loc[Sw[i].SteeringCommand == "Sturing Onbekend"] = 0
    Sw[i].MotorCurrent.loc[Sw[i].MotorCurrent == "Motorstroom Actief"] = 1
    Sw[i].MotorCurrent.loc[Sw[i].MotorCurrent == "Geen Motorstroom"] = 0


available_indicators = range(len(Sw))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Label('System'),
            dcc.Dropdown(
                id='Sys',
                options=[{'label': 'Switch ' + str(i), 'value': i} for i in available_indicators],
                value='0'
            ),
            html.Label('Graph Style'),
            dcc.RadioItems(
                id='yaxis_type',
                options=[{'label': i, 'value': i} for i in ['MotorCurrent', 'ControlPosition', 'SteeringCommand']],
                value='MotorCurrent',
                labelStyle={'display': 'inline-block'}
            )            
        ], className="six columns"),

        html.Div([
        dcc.Graph(
        id='main-graph',
        figure={
            'data': [
                go.Scatter(
                    y=[0],
                    x=[0],
                    text=[0],
                    mode='lines+markers',
                    opacity=0.7,
                    marker={
                        'size': 7,
                        'line': {'width': 0.25, 'color': 'white'}
                    },
                    line=dict(shape='hvh')
                ) 
            ],
            'layout': go.Layout(
                xaxis={'type': 'date', 'title': 'Smh'},
                yaxis={'title': 'Plot'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
        ], className="six columns"),
    ], className="row")
])


@app.callback(
    dash.dependencies.Output('main-graph', 'figure'),
    [dash.dependencies.Input('Sys', 'value'),
     dash.dependencies.Input('yaxis_type', 'value')])
def update_graph(Sys, yaxis_type):

    date = str(yaxis_type) + 'Date'
    return {
        'data': [go.Scatter(
            x=Sw[int(Sys)][date].dropna().iloc[:50],
            y=Sw[int(Sys)][yaxis_type].dropna().iloc[:50],
            text=Sw[int(Sys)][yaxis_type].dropna().iloc[:50],
            mode='lines+markers',
            marker={
                'size': 6,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': date,
                'type': 'date'
            },
            yaxis={
                'title': yaxis_type,
                'type': 'linear'
            },
            margin={'l': 40, 'b': 30, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
