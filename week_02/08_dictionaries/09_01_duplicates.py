'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.


'''

inputlist = ["a", "b", "c", "c"]


def duplicate_checker(user_list):
    my_dict = {}
    for i in user_list:
        my_dict[i] = 0

    for i in user_list:
        my_dict[i] += 1

    for i in my_dict:
        if my_dict[i] > 1:
            my_dict[i] = True
        else:
            my_dict[i] = False

    return my_dict

print(duplicate_checker(inputlist))




nums = [1,2,3,4,5,6,6,7,9,5,8,9]
#create a set from list
nums_set = set(nums)
#evaluate differences between list and set



if len(set(nums)) == len(nums):
    print("success")

else:
    print("duplicate found")


# for i in nums_set:
#     if i not in nums:
#         print(



# print(nums_set)

# for i in nums:
#     nums_set.append(i)

# def has_duplicates(x):
#     for i in nums:
#         if
#         dict_nums.append(i)
# has_duplicates(nums)
# print(dict_nums)