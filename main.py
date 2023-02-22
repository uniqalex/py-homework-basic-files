with open('files/recipes.txt', encoding="utf8") as file:
    recipes = {}
    for line in file:
        dish = line.strip()
        ingredient_amount = int(file.readline())

        ingredients = []
        for i in range(ingredient_amount):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            quantity = int(quantity)
            ingredients.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure
                 }
            )
        recipes[dish] = ingredients
        file.readline()

#Test task 1
print(recipes)


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in recipes:
            dish_parts = recipes[dish]
            for part in dish_parts:
                if part['ingredient_name'] in result:
                    #если этот ингридиент уже есть в result, значит он был добавлен в рамках другого блюда и /
                    #\ нам необходимо к его кол-ву прибавить увеличенное кол-во ингридиента от текущего блюда
                    result[part['ingredient_name']]['quantity'] += part['quantity'] * person_count
                else:
                    result[part['ingredient_name']] = {'measure': part['measure'],
                                                      'quantity': part['quantity'] * person_count}
        else:
            print(f'Указанное блюда {dish} отсутствует в кулинарной книге recipe')
            return
    return result

#Test task 2 !!! я добавил оливье.
res = get_shop_list_by_dishes(['Запеченный картофель', 'Оливье'], 3)
print(res)

