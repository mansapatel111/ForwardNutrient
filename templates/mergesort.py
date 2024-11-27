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
print(dict(list(restaurants.items())[:5]))


#restaurant, category
restaurant_input, category_input, nutrition_input = "Dairy Queen", "Desserts", "protein"
food_items = []
for food_name, food_info in restaurants[restaurant_input][category_input].items():
    nutrition = next(value for n, value in food_info if n == nutrition_input)
    food_items.append((food_name, nutrition))

def merge(arr, left, mid, right):
    leftSize = mid - left + 1
    rightSize = right - mid

    leftArr = [0] * leftSize
    rightArr = [0] * rightSize

    for i in range(leftSize):
        leftArr[i] = arr[left + i]
    for j in range(rightSize):
        rightArr[j] = arr[mid + 1 + j]

    leftPtr = 0
    rightPtr = 0
    mergedPtr = left

    while(leftPtr < leftSize and rightPtr < rightSize):
        if(leftArr[leftPtr][1] <= rightArr[rightPtr][1]):
            arr[mergedPtr] = leftArr[leftPtr]
            leftPtr += 1
        else:
            arr[mergedPtr] = rightArr[rightPtr]
            rightPtr += 1
        mergedPtr += 1

    while(leftPtr < leftSize):
        arr[mergedPtr] = leftArr[leftPtr]
        mergedPtr += 1
        leftPtr += 1
    
    while(rightPtr < rightSize):
        arr[mergedPtr] = rightArr[rightPtr]
        mergedPtr += 1
        rightPtr += 1

def mergeSort(rests, start, end):
    if(start < end):
        middle = (start + end) // 2
        mergeSort(rests, start, middle)
        mergeSort(rests, middle + 1, end)
        merge(rests, start, middle, end)

mergeSort(food_items, 0, len(food_items) - 1)
print(food_items)