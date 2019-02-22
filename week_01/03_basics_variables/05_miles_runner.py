'''
If a runner runs 12 kilometers in 30 minutes and 30 seconds.
What is his/her average speed in miles per hour. (Tip: 1 mile = 1.6 km)

'''
# so a runner can do 12 kilos in 30.5 minutes
# convert to number of miles in that amount of time
distance_miles = 12/1.6
print(distance_miles)
# so how many miles per minute?
miles_per_minute = distance_miles/30.5
print(miles_per_minute)
mph = miles_per_minute * 60
print(round(mph,2))
print(f'The average spped of the runner is {mph} miles per hour')

# therefore the runner runs at .25 * 60 miles or 14.75 mph per

