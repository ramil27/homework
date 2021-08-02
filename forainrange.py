# Цыклы
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(6):
# 	if languages[i] == lang1:
# 		print('yes')
# 	else:
# 		print('no')



# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# lang = 'php'
# label = False
# for i in languages:
# 	if i == lang:
# 		print(f'Да, {lang} is in list of languages')
# 		break

# if lang in languages:
# 		print(f'Да, {lang} is in list of languages')




# a = 7
# res = a
# for i in range(5):
# 	res = res * a
# print(res)

# res = a ** 6
# print(res)


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i, item in enumerate(languages):
# 	print(i + 1, item)



# for i in list(range(1, 11)):
#     print(i, end=', ')
# for i in list(reversed (range(1, 10))):
#     print(i, end=', ')

# for i in range(-9, 9):
# 	print(10 - abs(i), end=', ')
# print(10)



# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# a = names
# a[::2]

# print(a[::2])




# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# a = names
# a[::2]

# print(a[1:14:2])





# Stroki
# a = 'python'
# print(a.upper())



# a = 'qwertyuio'
# b = 'erererere'
# print(a.lower(), b.upper())


# a = bool(' ')
# print(a)



# a = input('ведите символ?: ')
# b = 'GitHub'
# print(a.join(b))



# a = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
# print(a.replace('е', '3'))



# a = input('Ваше имя?: ')
# b = int(input('Ваш возраст?: '))
# c = input('Ваш любимый фильм?: ')
# print('Здраствуйте, классный фильм!')




# a = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
# b = a.split()
# print(len(b))



# a = 'Самые важные собЫтия в миРе инфосека за сентябрь'
# b = ('|'.join(a))
# print(b)



# a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
# print(a.upper())



# a = ('aassss', 12, 3.5, True)
# print(a[0:5])


# a = []
# a.append(3)
# a.append('hello')
# print(a)



# a = ('Максат','Лязат','Данияр','Айбек','Атай')
# print(a)



# a = ('Максат','Лязат','Данияр')
# print(a[0:3])




# a = ('ssddsdsd', 15, 3.6, True,['bfbfb'])
# print(a)





# names = ['Максат','Лязат','Данияр','Айбек','Атай']
# a = (' ')
# b = a.join(names)
# print(b)




# names1 = ['Максат']
# names2 = ['Лязат']
# names3 = names1 + names2
# print(names3)



# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'oskar',]
# a = names.count('Jack')
# print(a)




# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'oskar',]
# a = names.remove('oskar')
# print(a, names)



# names = ['Ramil','1989','Python']
# a = (' ')
# b = a.join(names)
# print(b)




# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# a = pythonList.pop(6)
# print(pythonList)




# from functools import reduce
# numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
# print(reduce(lambda x, y: x*y, numbers))





# a = 'Lamborgini 17 4456 2020 Paris USA 11 23'
# b = []
# c = []
# for i in a:
# 		if i.isnumeric():
# 				b.append(int(i))
# 		else:
# 				c.append(i)
# 				print(b, '\n', c)





# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# a = print(pythonList[0:3])