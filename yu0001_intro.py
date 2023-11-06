import random
import yu0001_pi_module

name="steww"
the_len = len(name)
print(f"the length of {name} is {the_len}")
print(f"number of occurances of letter 'w' = {name.count('w')}")

# n-built random module
rand_int = random.randint(1, 10)
print(f"rand int = {rand_int}")

# my own module
print(f"pi = {yu0001_pi_module.pi}")

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