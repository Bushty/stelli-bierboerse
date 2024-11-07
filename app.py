from flask import Flask, render_template, jsonify, request
import random
import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder
from datamanager import *
from financiallogic import *

app = Flask(__name__)

jsonPath = "./history.json"

@app.route('/')
def button_page():
    # timestamps aus json laden
    timestamps = get_history_timestamps()

    # preise aus json laden
    beverages = get_history_prices()

    # config aus json laden
    config = get_config()

    lines = []
    for beverage in beverages:
        line = go.Scatter(
            x = timestamps,                     # X-axis as a sequence of numbers
            y = beverage['prices'],
            mode = 'lines+markers',             # Display both lines and markers
            line = dict(width=2), # Set line color to blue and line width
            marker = dict(size=4),              # Set marker size for points on the line
            name = beverage['name']
        )
        lines += [line]

    graph_json = json.dumps(lines, cls=PlotlyJSONEncoder)

    return render_template('buttons.html', graph_json=graph_json, prices=get_current_prices(), config=config)

@app.route('/graph')
def graph_page():    
    # timestamps aus json laden
    timestamps = get_history_timestamps()

    # preise aus json laden
    beverages = get_history_prices()

    # config aus json laden
    config = get_config()

    # daten älter als 2h raus schneiden
    latest_n = int(config["show_history_h"] / config["intervall_s"])

    if(len(timestamps) > latest_n):
        timestamps = timestamps[-latest_n:]
        beverages = beverages[-latest_n:]

    lines = []
    for beverage in beverages:
        line = go.Scatter(
            x = timestamps,
            y = beverage['prices'],
            mode = 'lines+markers',             # Display both lines and markers
            line = dict(width=2),
            marker = dict(size=4),              # Set marker size for points on the line
            name = beverage['name']
        )
        lines += [line]

    xaxis_range = [timestamps[0], timestamps[-1]]

    layout = dict(
        title="Zeit",
        xaxis=dict(
            showticklabels=True,
            dtick=3
        ),
        yaxis_title="Preis"
    )

    # Create the graph JSON object with layout included
    graph_json = json.dumps({
        'data': lines,
        'layout': layout
    }, cls=PlotlyJSONEncoder)
    
    return render_template('graph.html', graph_json=graph_json, prices=get_current_prices(), config=config)

@app.route('/process_investment', methods=['POST'])
def process_investment():
    handle_sales(request.get_json())

    return "success"

if __name__ == '__main__':
    app.run(debug=True)
