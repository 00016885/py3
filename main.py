# value = input("enter a number:")
# num = int(value)
# print(num)
# print(bin(num))
# print(oct(num))
# print(hex(num))

# def converter(num, type):
#     print(num)
#     print(type(num))
#
# converter(5, bin)


# counter = 0
# def increment():
#     global counter
#     counter += 1
#
# increment()
# print(counter)
# increment()
# print(counter)
#
#
def login(username, password):
    global is_logged_in

    if username == "admin" and password == "password":
        is_logged_in = True
    else:
        is_logged_in = False
login("admin", "password")
print(is_logged_in)