import math
#网上抄来的
#没完全看懂
#只知道有这个库，不知道定积分是啥

import numpy as np
import scipy.integrate as si  # numpy求定积分用

def f(x):
    y = 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)
    return y 
# 3. numpy直接求定积分的API
# 利用quad求定积分，给出函数f,积分下限和积分上限[a,b]，返回值为(积分值,最大误差)
print('积分', si.quad(f, 0, math.pi/2))
