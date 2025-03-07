def classify_age(age):
    if age < 0:
        print("Invalid age. Age cannot be negative.")
    elif age == 0:
        print("There is no age 0.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teen.")
    elif age <= 64:
        print("You are an adult.")
    else:
        print("You are a senior.")

classify_age(8)
classify_age(15)
classify_age(30)
classify_age(70)
classify_age(-5)
classify_age(0)