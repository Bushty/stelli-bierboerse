from flask import Flask, render_template, jsonify, request
import random
import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder
from datamanager import *
from financiallogic import *

app = Flask(__name__)

# Generate random data for the graph
def generate_data():
    return [random.randint(1, 10) for _ in range(6)]

@app.route('/')
def button_page():
    # Render the page with six buttons
    return render_template('buttons.html')

@app.route('/graph')
def graph_page():
    # Render the graph page initially without data
    variables = [generate_data() for _ in range(6)]
    traces = []
    for i, var in enumerate(variables):
        line = go.Scatter(
            x=list(range(len(var))),
            y=var,
            mode='lines+markers',
            name=f'Line {i+1}',  # Give each line a name
            line=dict(width=2),
            marker=dict(size=4)
        )
        traces.append(line)

    graph_json = json.dumps(traces, cls=PlotlyJSONEncoder)
    return render_template('graph.html', graph_json=graph_json)

@app.route('/update_graph', methods=['GET'])
def update_graph():
    # Generate new data for 6 lines
    traces = []
    for i in range(6):
        variables = generate_data()  # Each line gets its own random set of data
        
        # Create a line chart using Plotly
        line = go.Scatter(
            x=list(range(len(variables))),
            y=variables,
            mode='lines+markers',
            name=f'Line {i+1}',  # Give each line a name for better visualization
            line=dict(width=2),
            marker=dict(size=4)
        )
        traces.append(line)

    graph_json = json.dumps(traces, cls=PlotlyJSONEncoder)
    return jsonify(graph_json=graph_json)

@app.route('/process_input', methods=['POST'])
def process_input():
    # Handle input from the button page
    user_input = request.form.get('user_input')  # Assuming there is an input field in buttons.html
    # You can use the input to call functions from financiallogic or datamanager
    result = process_user_input(user_input)  # Replace with your actual processing logic
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
