def fizz_buzz(number):
    while number == type(int):
        for n in number:
            if n % 3 == 0 and n % 5 == 0:
                print( 'Fizz Buzz' )
            if n % 3 == 0:
                print( 'Fizz' )
            if n % 5 == 0:
                print( 'Buzz' )
            else:
                print(str(n))
        return str(number)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
