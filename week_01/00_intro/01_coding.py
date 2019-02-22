'''
Write the necessary code to display the follow message to the console
Challenge: write code to duplicate the "co-" part
instead of writing it 3 times.

Time for co-co-co-ding.

'''

a = "coding"
b = (((a[0:2]) + "-") * 3) + a[2:6]
c = "Time for " + b
print(c)

#or

print('time for  ' + "co-" * 3 + 'ding')

#or
s = "co-"
coco =""
for i in range(3):
    coco = coco + s
print(coco)
print("Time for " + coco + "ding.")

c = "-"
print("time for " + c.join(["co","co","co"]) + "-ding")

print(f"time for {'co-' * 3}ding")

