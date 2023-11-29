number = []
vlans = {'Телефон': ['Телефон 34343434', 'Телефон +789111', 'Телефон']}
number.append(vlans['Телефон'][-1])
vlans['Телефон'].pop(-1)
print(number)