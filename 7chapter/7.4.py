prompt='please enter the burden:' 
prompt+="\n(Enter 'quit'when you are finished.)"
while True:
    burnden_sheet=input(prompt)

    if burnden_sheet=='quit':
        break
    else:
        print(f"I'd like to add this burnden {burnden_sheet}!")
