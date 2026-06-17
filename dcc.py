#Dishonest Capacity Calculator (if-else)

print('Enter TB or GB for the advertised unit:')
unit = input('')

# Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb':
    disc = 1000000000000 / 1099511627776 #discrepancy
elif unit == 'GB' or unit == 'gb':
    disc = 1000000000 / 1073741824

print('Enter the advertised capacity:')
ad_cap = input('')
ad_cap = float(ad_cap)

real_cap = str(round(ad_cap * disc, 2))

print('The actual capacity is ' + real_cap + ' ' + unit)