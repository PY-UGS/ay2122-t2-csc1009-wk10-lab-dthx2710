# q2b
# convert number into string
def course_name(code):
    switch = {
        "CSC1009": "Object-Oriented Programming",
        "CSC1010": "Computer Networking",
        "CSC1008": "Data Structures & Algorithm",
    }
    return switch.get(code, "Invalid Course Code!")
# If does not match, return "invalid course code"


# main
if __name__ == "__main__":
    a = 0
    print(course_name("CSC1008"))

# q2c
my_list = []

for x in range (66, 103):  # loop 66-102
    if x % 2 > 0:  # if x is odd
        my_list.append(x)

my_list.sort().reverse()  # reverse sorted descending order
print(my_list)
