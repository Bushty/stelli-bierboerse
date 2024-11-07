from flask import Flask, render_template
import random
import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder  # Correct import for JSON encoder

app = Flask(__name__)

PREIS_ANSTIEG_FAKTOR = 1.05
PREIS_ABSTIEG_FAKTOR = 0.95

jsonPath = "./history.json"

# Generate random data for the graph
def generate_data():
    return [random.randint(1, 10) for _ in range(6)]

@app.route('/')
def button_page():
    # Render the page with six buttons
    return render_template('buttons.html')

@app.route('/graph')
def graph_page():
    # load json from file
    with open(jsonPath, 'r') as file:
        data = json.load(file)

    # timestamps aus json laden
    timestamps = data['history']['time']
    # preise aus json laden
    beverages = data['history']['beverages']

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

    # aktuelle Preise zusammenfassen
    latestPrices = [
        {
            "name": beverage["name"],
            "price": max(beverage["prices"])  # Höchster Preis ist der neueste
        }
        for beverage in beverages
    ]

    # Pass the graph data to the template
    return render_template('graph.html', graph_json=graph_json, prices=latestPrices)


if __name__ == '__main__':
    app.run(debug=True)


