from flask import Flask, render_template, request, jsonify
import pandas as pd
from quicksort import quick_main
from mergesort import mergeFunction
app = Flask(__name__)

data = pd.read_excel('data/ms_annual_data_2022.xlsx')

@app.route('/')
def home():
    return render_template('pyshow.html')

@app.route('/sort', methods=['POST'])
@app.route('/sort', methods=['POST'])
def sort_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    restaurant = data.get('restaurant', '')
    category = data.get('category', '')
    criteria = data.get('criteria', '')
    level = data.get('level', '')
    sorting = data.get('sorting', '')

    if not restaurant or not category or not criteria or not level:
        return jsonify({'error': 'Missing data fields'}), 400

    if sorting == 'Quick': 
        sorted_data = quick_main(restaurant, category, criteria, level)
    else:
        sorted_data = mergeFunction(restaurant, category, criteria, level)
    # print(quicksort.quick_main(restaurant, category, criteria, level))

    # print(message)
    
    
    
    return jsonify(sorted_data)

if __name__ == '__main__':
    app.run(debug=True)

