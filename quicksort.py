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



def main():
    # Main script logic goes here
    rest = pd.read_excel("C:/Users/pvano/Downloads/ms_annual_data_2022.xlsx")
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

    # what restaurant are you eating at?
    user_r = input("What restaurant are you eating at today?")
    course = input("What course are you looking for?")
    priority = input("Please select your number one nutrition priority?")
    high_low = input(f"Do you want your food item to be high or low in {priority}?")
    # take in user input and ask if their priority is high or low measurement and which factor is most important to them

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

    quick_sort(meal_list)

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    main()





