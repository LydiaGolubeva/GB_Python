#Голубева Лидия Ильинична

# Задание-1:
list_1 = [1,2,4,0]
print('list_1:', list_1)
list_2 = list(map(lambda x:x**2, list_1))
print('list_2:', list_2)

# Задание-2:
fruits_1 = ['Apricot', 'Lime', 'Fig', 'Pomegranate', 'Grape']
fruits_2 = ['Grape', 'Apple', 'Pomegranate', 'Melon', 'Лимон', 'Apricot']
result = [i for t in fruits_1 if t in fruits_2]
print(result)

# Задание-3:
list_1 = [-18, 45, 36, 98, 27, 84, 77, 34, 48, 5, -3, 24, 69, -4]
list_2 = [i for i in list_1 if  i >= 0 and i%4 and not i%3]
print(list_2)