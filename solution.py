import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 399623382 # Ваш chat ID, не меняйте название переменной

def solution(x):
    res = ztest(x1=x, value=500, alternative='larger')
    return res[1] < 0.02


