'''
In the U.S., if there is:
    - One person who is born every 6 seconds
    - One person who dies every 12 seconds
    - One person who immigrates every 40 seconds

Write the necessary code to display the total population
for the next 3 years (without a leap year).
Let's say the current population is 380,123,456.

'''
a = 380123456
seconds_in_three_years = (60 * 60 * 24 * 365) * 3
born = int(seconds_in_three_years/6)
dies = int(seconds_in_three_years/12)
immigrate = int(seconds_in_three_years/40)
total = a + born + immigrate - dies
print(type(total))
print(f'The total population in the US in three years will be {total:,d} people.')
