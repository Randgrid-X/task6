immutable_var = 'dog', 5.5, 'fish', 7, 'bird', False
print('Неизменяемый кортеж: ', (immutable_var))

mutable_var = ['dog', 5.5, 'fish', 7, 'bird', False]
print('Изменяемый список:', (mutable_var))
mutable_var[2] = 'octopus'
mutable_var[-1] = True
print('Изменённый список:', (mutable_var))

immutable_var = 'dog', 5.5, 'fish', 7, 'bird', False
print(type(immutable_var))
immutable_var[1]=1024 # кортеж не поддерживает обращение по элементам
print(immutable_var)
