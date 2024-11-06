from flask import Flask, render_template
import random
import plotly.graph_objs as go
import json
from plotly.utils import PlotlyJSONEncoder  # Correct import for JSON encoder

app = Flask(__name__)

PREIS_ANSTIEG_FAKTOR = 1.05
PREIS_ABSTIEG_FAKTOR = 0.95

# Generate random data for the graph
def generate_data():
    return [random.randint(1, 10) for _ in range(6)]

@app.route('/')
def button_page():
    # Render the page with six buttons
    return render_template('buttons.html')

@app.route('/graph')
def graph_page():
    # Generate new data for the graph
    variables = generate_data()
    # Create a bar chart using Plotly
    line = go.Scatter(
        x=list(range(len(variables))),  # X-axis as a sequence of numbers
        y=variables,
        mode='lines+markers',           # Display both lines and markers
        line=dict(color='blue', width=2), # Set line color to blue and line width
        marker=dict(size=4)             # Set marker size for points on the line
    )

    graph_json = json.dumps([line], cls=PlotlyJSONEncoder)
    # Pass the graph data to the template
    return render_template('graph.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(debug=True)


