from flask import Flask, render_template, jsonify, request
import random
import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder
from datamanager import *
from financiallogic import *

app = Flask(__name__)

jsonPath = "./history.json"

# Generate random data for the graph
# def generate_data():
#     return [random.randint(1, 10) for _ in range(6)]

@app.route('/')
def button_page():
    beverages = get_history_prices()

    # Render the page with six buttons
    return render_template('buttons.html', beverages=beverages)

@app.route('/graph')
def graph_page():
    # timestamps aus json laden
    timestamps = get_timestamps()

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

    # aktuelle Preise zusammenfassen
    latestPrices = [
        {
            "name": beverage["name"],
            "price": beverage["prices"][-1]
        }
        for beverage in beverages
    ]



    # Pass the graph data to the template
    return render_template('graph.html', graph_json=graph_json, prices=latestPrices, config=config)


# @app.route('/update_graph', methods=['GET'])
# def update_graph():
#     # Generate new data for 6 lines
#     traces = []
#     for i in range(6):
#         variables = generate_data()  # Each line gets its own random set of data
        
#         # Create a line chart using Plotly
#         line = go.Scatter(
#             x=list(range(len(variables))),
#             y=variables,
#             mode='lines+markers',
#             name=f'Line {i+1}',  # Give each line a name for better visualization
#             line=dict(width=2),
#             marker=dict(size=4)
#         )
#         traces.append(line)

#     graph_json = json.dumps(traces, cls=PlotlyJSONEncoder)
#     return jsonify(graph_json=graph_json)

@app.route('/process_input', methods=['POST'])
def process_input():
    # Handle input from the button page
    user_input = request.form.get('user_input')  # Assuming there is an input field in buttons.html
    # You can use the input to call functions from financiallogic or datamanager
    result = process_user_input(user_input)  # Replace with your actual processing logic
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
