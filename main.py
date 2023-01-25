cook_book = {}

with open('recipes.txt', 'rt', encoding='utf-8') as recipt:
    
    for i in recipt:
        dish_name = i.strip( )
        amount_of_ingredients = int(recipt.readline())
        amout = []
        for f in range(amount_of_ingredients):
            amo = recipt.readline()
            ingredient_name, quantity, measure = amo.strip().split(' | ')
            amout.append({
                'ingredient_name' : ingredient_name,
                'quantity' : int(quantity),
                'measure' : measure

            })
            dep = {dish_name: amout}
        recipt.readline()
        cook_book.update(dep)
        
        cook_book[dish_name] = amout
print(f'cook_book = {cook_book}\n')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                del [new_shop_list_item['ingredient_name']]
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
                del [new_shop_list_item['ingredient_name']]

    return shop_list

print(get_shop_list_by_dishes(['Омлет'], 2))
print()

import os
path = os.getcwd()
name_folder = "task"
all_path = os.path.join(path,name_folder)
list_of_contains = os.listdir(all_path)
dict_1= {}
dict_2 = {}

for i in list_of_contains:
    name = os.path.join(all_path,i)
    
    with open(name, encoding="utf-8") as file:
        lines_of_files = file.readlines()
        contain = []
        len_contain = len(lines_of_files)
        for line in lines_of_files:
            contain.append(line)
        dict_1[i] = contain
        dict_2[i] = len_contain

list_in_the_end = sorted(dict_2.items(), key=lambda item: item[1])
end_dict = dict(list_in_the_end)
list_of_sorted = list(end_dict.keys())

for i in list_of_sorted:
    n = 1
    path = os.getcwd()
    name_folder = "task"
    all_path = os.path.join(path, name_folder,i)
    print(i)
    
    with open(all_path, encoding="utf - 8") as file:
        all_lines = file.readlines()
        final_list = []
        for a in all_lines:
            print(f'Строка номер {n}\n{a}\n')
            n += 1
