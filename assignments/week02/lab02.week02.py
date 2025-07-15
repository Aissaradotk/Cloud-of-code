direction = input("what os your converion direction (1:THB to USD ,2: USD to THB):")
amount = float(input("amount to convert:"))

if direction == "1":
    result = amount / 35.5
    print("Result = ", result)
    print(f"{amount}=/ 35.5 = {result}")

if direction == "2":
    result = amount * 35.5
    print("Rusult = ", result)
    print(f"{amount}/ 35.5={result}")
2