from pizza import make_pizza as mp
# 使用as给函数指定别名
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers')


import pizza as p
# 使用as给模块指定别名
p.make_pizza(14, 'extra cheese')


from pizza import * #导入模块中的所有函数