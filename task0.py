# https://github.com/Thunderbird1698/fizzbuzz.git

for i in range (1,101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FiizBuzz")
    elif(i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
            print(i)