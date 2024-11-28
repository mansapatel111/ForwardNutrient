from flask import Flask, render_template, request, jsonify
import pandas as pd
from quicksort import quick_main
from mergesort import mergeSort
app = Flask(__name__)

data = pd.read_excel('data/ms_annual_data_2022.xlsx')

@app.route('/')
def home():
    return render_template('pyshow.html')

@app.route('/sort', methods=['POST'])
def sort_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    restaurant = data.get('restaurant', '')
    category = data.get('category', '')
    criteria = data.get('criteria', '')
    level = data.get('level', '')

    if not restaurant or not category or not criteria or not level:
        return jsonify({'error': 'Missing data fields'}), 400

    message = quick_main(restaurant, category, criteria, level)
    # print(quicksort.quick_main(restaurant, category, criteria, level))
    
    print(message)
    
    
    
    return jsonify({'message': message})
if __name__ == '__main__':
    app.run(debug=True)
