from flask import Flask, render_template, request, jsonify
import pandas as pd
from quicksort import quick_main
from mergesort import mergeFunction
from mergesort import retrieveAllNutrients
import timeit;
app = Flask(__name__)

data = pd.read_excel('data/ms_annual_data_2022.xlsx')

@app.route('/')
def home():
    return render_template('pyshow.html')


@app.route('/sort', methods=['POST'])
def sort_data():
    data = request.json
    # edge case if no data is provided
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # load data from request

    restaurant = data.get('restaurant', '')
    category = data.get('category', '')
    criteria = data.get('criteria', '')
    level = data.get('level', '')
    sorting = data.get('sorting', '')

    # edge case if missing data fields

    if not restaurant or not category or not criteria or not level:
        return jsonify({'error': 'Missing data fields'}), 400

    # edge case if invalid sorting method

    # Quick Sort

    if sorting == 'Quick': 
        # the timing import to track time
        start_time = timeit.default_timer()
        sorted_data = quick_main(restaurant, category, criteria, level)
        elapsed_time = timeit.default_timer() - start_time
        print(f"Quick Time Elapsed: {elapsed_time}")

    # Merge Sort
    elif sorting == 'Merge':

        start_time = timeit.default_timer()
        sorted_data = mergeFunction(restaurant, category, criteria, level)
        elapsed_time = timeit.default_timer() - start_time
        print(f"Merge Time Elapsed: {elapsed_time}")
        
    # print(quicksort.quick_main(restaurant, category, criteria, level))

  
    
    
    
    return jsonify(sorted_data)

if __name__ == '__main__':
    app.run(debug=True)

