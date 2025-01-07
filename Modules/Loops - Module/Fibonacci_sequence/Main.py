
num = int (input("Please enter your number "))

_1st_num = 0 
_2nd_num = 1

result = 0

print(_1st_num)
print(_2nd_num)

while num: 

    
    result  = _1st_num + _2nd_num
    
    _1st_num = _2nd_num
    _2nd_num = result
    print(result) 
    num -=1
    



