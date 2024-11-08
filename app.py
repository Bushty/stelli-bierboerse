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
    return render_template('buttons.html', data=get_history_data(), config=get_config())

@app.route('/getData')
def getData():
    return get_history_data()

@app.route('/graph')
def graph_page():    
    return render_template('graph.html', config=get_config())

@app.route('/process_investment', methods=['POST'])
def process_investment():
    handle_sales(request.get_json())

    return "success"

if __name__ == '__main__':
    app.run(debug=True)
