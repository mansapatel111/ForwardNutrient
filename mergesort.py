import pandas as pd

#performs the merge sort algorithm based on user selections
    
#makes a vector of tuples with a food item and a nutrient value of food items under a chosen category for a chosen restaurant that are going to be sorted based on what the user is looking for
#e.g. user chooses The Cheesecake Factory, Desserts, and calories so the vector is tuples of desserts from that restaurant with their corresponding calories
def mergeFunction(restaurant_input, category_input, criteria_input, level_input):
    rest = pd.read_excel("data/ms_annual_data_2022.xlsx")

    restaurants = {}
    counter = 0
    for index, row in rest.iterrows():
        if pd.isna(row[criteria_input]):
            continue

        r = row['restaurant']
        category, food_name, calories, fat, cholesterol, sodium, carbs, fiber, sugar, protein = row['food_category'], row['item_name'], row['calories'], row['total_fat'], row['cholesterol'], row['sodium'], row['carbohydrates'], row['dietary_fiber'], row['sugar'], row['protein']
        
        if pd.isna(row['calories']): calories = "no value"
        if pd.isna(row['total_fat']): fat = "no value"
        if pd.isna(row['cholesterol']): cholesterol = "no value"
        if pd.isna(row['sodium']): sodium = "no value"
        if pd.isna(row['carbohydrates']): carbs = "no value"
        if pd.isna(row['dietary_fiber']): fiber = "no value"
        if pd.isna(row['sugar']): sugar = "no value"
        if pd.isna(row['protein']): protein = "no value"

        item = {food_name: [("calories", calories), ("total_fat", fat), ("cholesterol", cholesterol), ("sodium", sodium), ("carbohydrates", carbs), ("dietary_fiber", fiber), ("sugar", sugar), ("protein", protein)]}
        if r not in restaurants:
            curr_dict = {category: item}
            restaurants[r] = curr_dict
        else:
            if category not in restaurants[r]:
                restaurants[r][category] = item
            else:
                restaurants[r][category][food_name] = [("calories", calories), ("total_fat", fat), ("cholesterol", cholesterol), ("sodium", sodium), ("carbohydrates", carbs), ("dietary_fiber", fiber), ("sugar", sugar), ("protein", protein)]
        

    if restaurant_input not in restaurants:
        return "error: criteria not found in restaurant"
    #returns an error string if the restaurant doesn't have that category of food
    if category_input not in restaurants[restaurant_input]:
        return "error: category not found"

    food_items = []
    for food_name, food_info in restaurants[restaurant_input][category_input].items():
        nutrition = next(value for n, value in food_info if n == criteria_input)
        food_items.append((food_name, nutrition))
    #sorts the food_items vector with the merge sort algorithm
    mergeSort(food_items, 0, len(food_items) - 1)

    #makes a vector of the highest 5 or lowest 5 foods in the inputted nutrition and returns it
    leveledFoods = []
    if(level_input == "Low"):
        h = 0
        while h < 5 and len(food_items) > h:
            leveledFoods.append(food_items[h][0])
            leveledFoods.append(food_items[h][1])
            h += 1
    if(level_input == "High"):
        d = len(food_items) - 1
        counter = 0
        while d >= 0 and counter < 5:
            leveledFoods.append(food_items[d][0])
            leveledFoods.append(food_items[d][1])
            d -= 1
            counter += 1
    r = retrieveAllNutrients(restaurants, leveledFoods, restaurant_input, category_input, criteria_input, level_input)
    return r

#merge and mergeSort logic from Discussion 8 - Sorting slides 11 and 12
#part of the merge sort where it merges two sections of the main vector
def merge(arr, left, mid, right):
    #creates two smaller vectors representing left and right halves based on the parameter values
    leftSize = mid - left + 1
    rightSize = right - mid
    leftArr = [0] * leftSize
    rightArr = [0] * rightSize
    for i in range(leftSize):
        leftArr[i] = arr[left + i]
    for j in range(rightSize):
        rightArr[j] = arr[mid + 1 + j]

    #pointers that keep track of current index in both vectors
    leftPtr = 0
    rightPtr = 0
    mergedPtr = left

    #merges the two vectors into the original vector so that section is now in order
    while(leftPtr < leftSize and rightPtr < rightSize):
        if(leftArr[leftPtr][1] <= rightArr[rightPtr][1]):
            arr[mergedPtr] = leftArr[leftPtr]
            leftPtr += 1
        else:
            arr[mergedPtr] = rightArr[rightPtr]
            rightPtr += 1
        mergedPtr += 1

    #if there's leftover elements in the left vector, puts them in the original vector
    while(leftPtr < leftSize):
        arr[mergedPtr] = leftArr[leftPtr]
        mergedPtr += 1
        leftPtr += 1

    #if there's leftover elements in the left vector, puts them in the original vector
    while(rightPtr < rightSize):
        arr[mergedPtr] = rightArr[rightPtr]
        mergedPtr += 1
        rightPtr += 1

#sorts the left and right sections of the 'rests' vector recursively resulting in a sorted final vector
def mergeSort(rests, start, end):
    if(start < end):
        middle = (start + end) // 2
        mergeSort(rests, start, middle)
        mergeSort(rests, middle + 1, end)
        merge(rests, start, middle, end)

def retrieveAllNutrients(restaurants, top_foods, restaurant_input, category_input, criteria_input, level_input):
    all_foods = restaurants[restaurant_input][category_input]
    curr_food_index = 0
    curr_ind = 0
    while(curr_ind < len(top_foods) - 1):
        del top_foods[curr_ind + 1]
        for j in range(len(all_foods[top_foods[curr_food_index]])):
            top_foods.insert(curr_ind + 1, all_foods[top_foods[curr_food_index]][j][1])
            curr_ind += 1
        curr_ind += 1
        curr_food_index = curr_ind
    return top_foods
