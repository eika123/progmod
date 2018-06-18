
user_name = input("what is your name?" + "\n")

print("Hello, " + user_name)

adult_age = 18

user_age = input("what is your age?" + '\n')

# possible implementation
# user_age = eval(user_age)

#better: user_age could be executable code for eval
user_age = int(user_age)

if user_age < 18:
    print("You are not an adult!" + user_name + "!")
else:
    print("You are an adult, " + user_name + "!")
