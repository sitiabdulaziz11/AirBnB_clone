# # import my_math/abs.py x
# # import my_math/abs x
# # import my_math.abs.py x
# import my_math.abs  #correct

# # but to use the function:
# my_math.abs.my_abs(x) # not friendly

# from my_math.abs import my_abs #friendly
# # now you can use your function like tha:
# my_abs(x)

# from my_math.functions.add import my_add

# from my_math.functions import *
# print(add.my_add(1, 3))
# print(mul.my_mul(4, 2))
# print(div.my_div(10, 2))

from my_math.positive import is_positive
print(is_positive(89))
print(is_positive(-89))
print(is_positive(333))
