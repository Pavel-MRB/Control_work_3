def card_number(num):
    asterisks='************'
    num=str(num)
    return asterisks+num[-4:]

print(card_number(int(input('Please, input the number of credit card:\n'))))