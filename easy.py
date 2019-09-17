#Голубева Лидия Ильинична
# Задача-1:

fruit_list = ["яблоко", "банан", "киви", "арбуз"]
random_list = ["some", "random", "list", "and", 1, 2, 3, 4, 5, 5, 5, 5, "Python", "is", "awesome"]
another_random_list = ["some", "random", 2, 5, "Python"]
initial_list = [3, 66, 7, 45, 25, 6, 88, 143567, 4, 6.8]

def enumerate_and_align(fruit_list):
    for fruit_index, fruit_name in enumerate(fruit_list, start=1):
        print(fruit_index, "{:>10}".format(fruit_name))

# Задача-2:
def remove_repetitions(first_list, second_list):
    print("\nWe will remove doubled items from the first list that are contained in the second.")
    print("The first list is: ", first_list)
    print("The second list is:", second_list)
    first_list = [x for x in first_list if x not in second_list]
    print("Result list is:", first_list)
# Задача-3:
def new_list_by_rule(initial_list):
    print("\nInitial list is:", initial_list)
    new_list = []
    for i in initial_list:
        if i % 2 == 0:
            new_list.append(i / 4)
        else:
            new_list.append(2 * i)
    print("Result list is:", new_list)


if __name__ == "__main__":
    enumerate_and_align(fruit_list)
    remove_repetitions(random_list, another_random_list)
    new_list_by_rule(initial_list)
