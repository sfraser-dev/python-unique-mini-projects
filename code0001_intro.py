import random
import code001_pi_module

if __name__ == "__main__":
    """Main function."""

    # count occurances in a list
    name="Fredd"
    the_len = len(name)
    print(f"the length of {name} is {the_len}")
    print(f"number of occurances of letter 'd' = {name.count('d')}")

    # in-built random module
    rand_int = random.randint(1, 10)
    print(f"rand int = {rand_int}")

    # my own module
    print(f"pi = {code001_pi_module.pi}")

    # list
    my_list = ["a", "b", "c", "d"]
    print(my_list[::-1])
    print(my_list[0])
    print(my_list[-1])

    # list append, insert, pop, (extend, +), remove, count
    my_list2 = [1, 2, 3]

    my_list2.append(4)
    print(my_list2)

    my_list2.insert(0, 100)
    print(my_list2)

    my_list2.pop(1)
    print(my_list2)

    my_list2.extend([10,20,30])
    print(my_list2)
    my_list3 = my_list2+[22,33,33,33,44]
    print(my_list3)

    my_list3.remove(22)
    print(my_list3)

    print(my_list3.count(33))

    print(my_list3.index(100))

    # split and join
    my_str1 = "I am here"
    my_list4 = my_str1.split()
    print(my_list4)
    print(",".join(my_str1.split()))

    # for loops
    # "foreach"
    for x in "pooplop":
    # for x in [2,4,6,8]:
        print(f"x={x}")
    # "for"
    the_total = 0
    for x in range (1, 101):    # 1 to 100
        the_total += x
    print(f"the total is {the_total}")
    # "enumerate" (atuto generate the index)
    for index,val in enumerate("pooplop"):
        print(f"{index}: {val}")

    # fizzbuzz
    target = 15
    for x in range(1,target+1):
        if x%3==0 and x%5==0:
            print(f"{x}: fizzbuzz")
        elif x%3==0:
            print(f"{x}: fizz")
        elif x%5==0:
            print(f"{x}: buzz")
        else:
            print(f"{x}")

    my_list5 = [11,22,33,44]
    print(my_list5[0:2])

    # dictionary, {"key":"value"}, items are the keys and values
    # keys must be immutable, ie: string, numbers (int, float, complex), or tuples
    my_dict = {"Color": "Yellow", "Number": 4, "Name": "John", 200.5: "2-tonne", (3,4):"hi"}
    for key in my_dict.keys():
        print(f"{key}")
    for val in my_dict.values():
        print(f"{val}")
    for key,val in my_dict.items():
        print(f"{key} : {val}")

    # change the value of the "Color" key ("Color" key already exists)
    my_dict["Color"] = "Green"
    # add a "fire" key with value "starter"
    my_dict["fire"] = "starter"
    # add a 1 key with value 8
    my_dict[1]=8
    print(my_dict)

# title case
my_name = "jACk fUNnyMAn bLAcK"
print(my_name.title())

# limit number of decimal places
a = 3.45678
b = 100.34785378957349873987459
print(f"{a:.2f}")
print(f"{b:.5f}")

# get dictionary value for the given key - if not present, return 100
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 100))