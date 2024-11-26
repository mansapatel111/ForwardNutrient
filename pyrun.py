from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

data = pd.read_excel('data/ms_annual_data_2022.xlsx')

@app.route('/')
def home():
    return render_template('pyshow.html')

# ignore below functions, they are not used in the frontend, but i had them here for testing purposes
@app.route('/sort', methods=['GET'])
def sort_data():
    column = request.args.get('column', 'calories') 
    algorithm = request.args.get('algorithm', 'timsort')  
    if algorithm == 'bubble':
        sorted_data = bubble_sort(data, column) 
    else:
        sorted_data = data.sort_values(by=column).to_dict(orient='records')  

    return jsonify(sorted_data)

def bubble_sort(data, column):
    sorted_data = data.copy()
    for i in range(len(sorted_data)):
        for j in range(0, len(sorted_data) - i - 1):
            if sorted_data[column].iloc[j] > sorted_data[column].iloc[j + 1]:
                sorted_data.iloc[j], sorted_data.iloc[j + 1] = sorted_data.iloc[j + 1], sorted_data.iloc[j]
    return sorted_data.to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
