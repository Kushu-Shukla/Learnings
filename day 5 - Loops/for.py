number = [1, 2, 3, 4, 5]

for item in number: # for loop will iterate through each item in the list
    # the term item here represents each element in the list during each iteration
    # instead of using term item we can use any term like num, n, i, etc, it's basically a variable
    print(item)

i = 0
while i < len(number): # len() function returns the length of the list which is 5 in this case
    # so the while loop will run until i is less than 5
    print(number[i])
    i += 1