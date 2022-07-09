prompt='How old are you?'
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
    ticket_price=int(input(prompt))
    if ticket_price<3:
        print('The price is free.')
    elif ticket_price<12:
        print('The price is 10 dollars!')
    elif ticket_price>=12:
        print('The price is 15 dollars!')
   


        


