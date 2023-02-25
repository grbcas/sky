books = {
   "Саймон Сингх": "Книга шифров",
   "Брюс Шнайер": "Практическая криптография",
   "Нил Стивенсон": "Криптономикон",
   "Дэвид Кан": "Взломщики кодов",
   "Альбрехт Бойтельспахер": "Криптология",
}

print('-\nКниги:', *books.values(), sep='\n')
print('-\nАвторы:', *books, sep='\n')
print('-\nБиблиотека:')
# for key, val in books.items():
#     print(key, val, sep=' - ')

print('-\nБиблиотека:', [print(key, val, sep=' - ') for key, val in books.items()], sep='\n')