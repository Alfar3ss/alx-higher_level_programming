def print_list_integer(my_list=[]):
    for item in my_list:
        print("{:d}".format(item))

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
