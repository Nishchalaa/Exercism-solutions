def is_armstrong_number(number):
    number = str(number)
    count = 0
    for i in number:
        count = count + int(i)**len(number)
        print(count)
    if count == int(number):
        return True
    else:
        return False
        