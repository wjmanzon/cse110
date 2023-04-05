age = int(input("How old are you? "))
age_next_year = age + 1
print(f"On your next birthday, you will be {age_next_year}.")
print()

cartons = int(input("How many egg cartons do you have? "))
eggs = cartons * 12
print(f"You have {eggs} eggs.")
print()

cookies = int(input("How many cookies do you have "))
people = int(input("How many people are there? "))
cookies_per_person = cookies / people
print(f"Each person may have {cookies_per_person:.2f} cookies.")
print()