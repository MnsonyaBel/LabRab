users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

len_ = int(len(users))
len_2 = len(set(users))

dict_ = { 'Общее количество': len_,
          'Уникальные посещения': len_2
}

print(dict_)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

