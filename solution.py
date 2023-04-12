import pandas as pd
import numpy as np
#from scipy.stats import ks_2samp
from scipy.stats import kstest


chat_id = 808572568 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=0.06
    stat, p_value = kstest(x, y)
    return p_value < alpha # Ваш ответ, True или False
