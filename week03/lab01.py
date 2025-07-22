age = int(input("Enter age: "))
if 0 <= age <= 12:
   print(f"age = {age}: You are a Child")
elif 13 <= age <= 19:
   print(f"age = {age}: You are a Teenager")
elif 20 <= age <= 59:
   print(f"age = {age}: You are an Adult")
else:
   print(f"age = {age}: You are a Senior")