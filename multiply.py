#creating a list of multiplication tables from 1 to 5 and printing each table in the list.
for i in range(1, 6):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")