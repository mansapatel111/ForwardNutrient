import pandas as pd
rest = pd.read_excel("C:/Users/vikyc/Documents/ms_annual_data_2022.xlsx")
rest.head()


restaurants = {}
counter = 0
for index, row in rest.iterrows():
    r = row['restaurant']
    category, food_name, calories, fat, cholesterol, sodium, carbs, fiber, sugar, protein = row['food_category'], row['item_name'], row['calories'], row['total_fat'], row['cholesterol'], row['sodium'], row['carbohydrates'], row['dietary_fiber'], row['sugar'], row['protein']
    item = {food_name: [("calories", calories), ("fat", fat), ("cholesterol", cholesterol), ("sodium", sodium), ("carbs", carbs), ("fiber", fiber), ("sugar", sugar), ("protein", protein)]}
    if r not in restaurants:
        curr_dict = {category: item}
        restaurants[r] = curr_dict
    else:
        if category not in restaurants[r]:
            restaurants[r][category] = item
        else:
            restaurants[r][category][food_name] = [("calories", calories), ("fat", fat), ("cholesterol", cholesterol), ("sodium", sodium), ("carbs", carbs), ("fiber", fiber), ("sugar", sugar), ("protein", protein)]
#print(dict(list(restaurants.items())[:5]))


#performs the merge sort algorithm based on user selections
#def merge_sort_setup(restaurant_input, category_input, nutrition_input):
    #restaurant_input, category_input, nutrition_input = "Dairy Queen", "Desserts", "protein"
    
#makes a vector of tuples with a food item and a nutrient value of food items under a chosen category for a chosen restaurant that are going to be sorted based on what the user is looking for
#e.g. user chooses The Cheesecake Factory, Desserts, and calories so the vector is tuples of desserts from that restaurant with their corresponding calories
def mergeFunction(restaurant_input, category_input, nutrition_input, level):
    food_items = []
    for food_name, food_info in restaurants[restaurant_input][category_input].items():
        nutrition = next(value for n, value in food_info if n == nutrition_input)
        food_items.append((food_name, nutrition))
    #sorts the food_items vector with the merge sort algorithm
    mergeSort(food_items, 0, len(food_items) - 1)

    #makes a vector of the highest 5 or lowest 5 foods in the inputted nutrition and returns it
    leveledFoods = []
    if(level == "low"):
        for a in range(5):
            leveledFoods.append(food_items[a][0])
            leveledFoods.append(food_items[a][1])
    if(level == "high"):
        for b in range(-1, -6, -1):
            leveledFoods.append(food_items[b][0])
            leveledFoods.append(food_items[b][1])
    return leveledFoods

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

def retrieveAllNutrients(top_foods, restaurant_input, category_input):
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
        
            
#sorts the food_items vector in ascending order using a merge sort algorithm
restaurant_input, category_input, nutrition_input = "Dairy Queen", "Desserts", "calories"
retrieveAllNutrients(mergeFunction(restaurant_input, category_input, nutrition_input, "low"), restaurant_input, category_input)
