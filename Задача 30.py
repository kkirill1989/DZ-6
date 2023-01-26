#Пользователь вводит число N
#Затем он вводит личные данные (имя и возраст) своих N друзей.
#Создайте список friends и добавьте в него N словарей с ключами name и age
#Найдите самого младшего из друзей и выведите его имя.

N = int(input())
dict_list = []
min_age = 1000
min_name = ''
for _ in range(N):
    name = input()
    age = int(input())
    if age < min_age:
        min_age = age
        min_name = name
    dict_list.append({'name': name, 'age':age})
print(min_name)        
    