# bounce.py
#
# Exercise 1.5

bound_cnt = 0
height = 100
while bound_cnt < 10 :
    height = height * (3/5)
    print(bound_cnt + 1, round(height, 4))
    bound_cnt = bound_cnt +1 
