import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 808572568 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    flag = 0
    ks_stat, p_value = ks_2samp(x, y)

    # сравнение p-value с уровнем значимости
    alpha = 0.06
    if p_value < alpha:
        flag = 1
    return flag # Ваш ответ, True или False
