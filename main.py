for x in range(1, 200):
 
    fizz = not x % 3
    buzz = not x % 5
 
    if fizz and buzz :
        print("FizzBuzz")
    elif fizz:
        print("Fizz")
        print("Buzz")
    else:
        print("Rien du tout")
