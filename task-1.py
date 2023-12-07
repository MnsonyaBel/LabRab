numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sm_num = sum(numbers[:4])# TODO заменить значение пропущенного элемента средним арифметическим
sm_num_2 = sum(numbers[5:])
len_ = len(numbers)
sum_all = (sm_num + sm_num_2)/len_

numbers[4] = sum_all

print("Измененный список:", numbers)
