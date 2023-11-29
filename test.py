vlans = {'Название в системе': ['Воронеж', 'Minsk', ['Volhov', 'Volhov-2'], 'SPB']}

for i in range(len(vlans['Название в системе'])):
    if type(vlans['Название в системе'][i]) is list:
        f = vlans['Название в системе'][i]
        vlans['Название в системе'].pop(i)
        vlans['Название в системе'].insert(i, ', '.join(f))
print(vlans)