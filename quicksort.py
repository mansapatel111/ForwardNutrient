import pandas as pd

def quick_sort(meal_list):
    if len(meal_list) <= 1:
        return meal_list

    pivot = meal_list[-1]
    less = []
    greater = []

    for item in meal_list[:-1]:
        if item[1] <= pivot[1]:
            less.append(item)
        else:
            greater.append(item)

    sorted_less = quick_sort(less)
    sorted_greater = quick_sort(greater)

    return sorted_less + [pivot] + sorted_greater



def quick_main(user_r, course, priority, high_low):
    # Main script logic goes here
    rest = pd.read_excel("data/ms_annual_data_2022.xlsx")
    restaurants = {}
    counter = 0
    for index, row in rest.iterrows():
        r = row['restaurant']
        category, food_name = row['food_category'], row['item_name']
        calories, fat, cholesterol, sodium, carbs, fiber, sugar, protein = (
            row['calories'], row['total_fat'], row['cholesterol'], row['sodium'],
            row['carbohydrates'], row['dietary_fiber'], row['sugar'], row['protein']
        )
        item = {food_name: [("calories", calories), ('fat', fat), ('cholesterol', cholesterol),
                            ('sodium', sodium), ('carbs', carbs), ('fiber', fiber),
                            ('sugar', sugar), ('protein', protein)]}
        if r not in restaurants:
            curr_dict = {category: item}
            restaurants[r] = curr_dict
        else:
            if category not in restaurants[r]:
                restaurants[r][category] = item
            else:
                restaurants[r][category][food_name] = [("calories", calories), ('fat', fat),
                                                       ('cholesterol', cholesterol),
                                                       ('sodium', sodium), ('carbs', carbs), ('fiber', fiber),
                                                       ('sugar', sugar), ('protein', protein)]

    #following code initializes a meal_list with meal name and nutrition value as a tuple
    meal_list = []
    curr_dict = restaurants[user_r]

    if course in curr_dict:
        items = curr_dict[course]

        for food_name, nutrition_facts in items.items():
            val = None
            for metric, metric_val in nutrition_facts:
                if metric == priority:
                    value = metric_val
                    break
            if value is not None:
                meal_list.append((food_name, value))
 
    meal_list = quick_sort(meal_list)
    
    #makes vector for top 5 or bottom 5
    if high_low == 'Low':
        bottom_5 = []
        for i in range(5):
            bottom_5.append(meal_list[i][0])
            bottom_5.append(meal_list[i][1])
        result = bottom_5
    else:
        top_5 = []
        for i in range(-1, -6, -1):
            top_5.append(meal_list[i][0])
            top_5.append(meal_list[i][1])
        result = top_5
    
    result = top_nutrient_facts(result, user_r, course, restaurants, priority)
    return result

def top_nutrient_facts(result_vector, user_r, course, restaurants, priority):
    nutrients = []
    
    curr_dict = restaurants.get(user_r, {})
    course_items = curr_dict.get(course, {})

    for i in range(0, len(result_vector), 2):  
        meal_name = result_vector[i]
        nutrients.append(meal_name)
        
        if meal_name in course_items:
            nutrient_facts = course_items[meal_name]
            for nutrient, value in nutrient_facts:
                nutrients.append(value)

    return nutrients





# Ensure the script runs only if executed directly
#if __name__ == "__main__":
#   print(quick_main("Dairy Queen", "Desserts", "protein", "high"))

