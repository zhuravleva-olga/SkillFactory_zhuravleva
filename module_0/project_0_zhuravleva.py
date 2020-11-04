#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
number = np.random.randint(1,101)    # загадали число
print ("Загадано число от 1 до 100")


def game_core(number):
    '''Называем число из середины диапазона, потом изменяем границы диапазона поиска в зависимости от того, больше оно или меньше нужного.
       Снова называем число из середины нового диапазона. Функция возвращает число попыток'''
    count = 1
    start = 1
    end = 101
    predict = int((start+end)/2)
    while number != predict:
        count+=1
        if number > predict: 
            start = predict+1
            predict = int((start+end)/2)
        elif number < predict: 
            end = predict
            predict = int((start+end)/2)
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# Проверяем
score_game(game_core)


# In[ ]:




