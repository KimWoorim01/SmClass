
money = 179870
#50000, 10000, 5000, 1000, 500, 100, 50, 10
# 500 - 1
# 100 - 2
# 50 - 1 
# 10 - 3

five_t = money//50000
money = money%50000

one_t = money//10000
money = money%10000

five = money//5000
money = money%5000

one = money//1000
money = money%1000

f_won = money//500
money = money%500

o_won = money//100
money = money%100

f_ten = money//50
money = money%50

ten = money//10
money = money%10

print("{}, {}, {}, {}, {}, {}, {}, {}".format(five_t, one_t, five, one, f_won, o_won, f_ten, ten))



