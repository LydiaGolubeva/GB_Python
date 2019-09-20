#Голубева Лидия Ильинична
# Задание-1:
def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    stpn =  number*degree
    result = int(stpn)
    knres = stpn-result
    if not (abs(knres) < 0.5):
        if result>0: result+=1
        else: result-=1
        return result/degree
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
def lucky_ticket(ticket_number):
    if (len(str(ticket_number)) != 6) or (type(ticket_number) is not int):
        return 'Некорректный номер билета'
    else:
        ticket_number1 = list(str(ticket_number))
    sum1 = int(ticket_number1[0]) + int(ticket_number1[1]) + int(ticket_number1[2])
    sum2 = int(ticket_number1[3]) + int(ticket_number1[4]) + int(ticket_number1[5])


    if sum1 == sum2:
        return 'Билет %s счастливый' % ticket_number
    else:
        return 'Билет %s несчастливый' % ticket_number
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
