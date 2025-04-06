# mortgage.py
#
# Exercise 1.7

principal = 500000
fixed_rate = 0.05
paymemt = 2684.11
total_paid = 0.0

while principal > 0 :
    principal = principal * (1 + fixed_rate/12) - paymemt
    total_paid = total_paid + paymemt

print('Total paid', total_paid)
