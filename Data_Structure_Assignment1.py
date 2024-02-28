def distribute_chocolates_iterative(chocolates, students): #    Distributes chocolates iteratively to students.
    #chocolates (list): A list of tuples representing chocolates.
    #Each tuple contains (weight, price, type, ID).
    #students (list): A list of student names.
    i = 0
    for student in students:
        if i < len(chocolates):
            print(
                f"Student: {student}, Chocolate: (weight: {chocolates[i][0]} gm, price: {chocolates[i][1]} AED, "
                f"Type: {chocolates[i][2]}, ID: {chocolates[i][3]})")
            i += 1
        else:
            print("No more chocolates to distribute.")
            break


# Recursive approach
def distribute_chocolates_recursive(chocolates, students): #    Distributes chocolates recursively to students.
    #chocolates (list): A list of tuples representing chocolates.
    #Each tuple contains (weight, price, type, ID).
    #students (list): A list of student names.
    if not chocolates or not students:
        return
    print(
        f"Student: {students[0]}, Chocolate: (weight: {chocolates[0][0]} gm, price: {chocolates[0][1]} AED, Type: {chocolates[0][2]},"
        f"ID: {chocolates[0][3]})")
    distribute_chocolates_recursive(chocolates[1:], students[1:])

# Test cases
chocolates = [
        (20, 5, "Milk", "001"),
        (10, 8, "Dark", "002"),
        (15, 6, "White", "003"),
        (7, 4, "Peanut butter chocolate", "005")  # New chocolate
    ]
students = [
        "Dana",
        "Fatima",
        "Sara"
    ]
    # Test iterative approach
print("Iterative Approach:")
distribute_chocolates_iterative(chocolates, students)
    # Test recursive approach
print("\nRecursive Approach:")
distribute_chocolates_recursive(chocolates, students)

print()
def test_sorting():
    # Define test data
    chocolates = [
        (20, 5, "Milk", "001"),
        (10, 8, "Dark", "002"),
        (15, 6, "White", "003"),
        (7, 4, "Peanut butter chocolate", "005")  # New chocolate
    ]
    # Define students with associated numbers
    students = [
        ("Dana", 1),
        ("Fatima", 2),
        ("Sara", 3)
    ]
    # Sort chocolates by weight
chocolates_sorted_by_weight = sorted(chocolates, key=lambda x: x[0])

# Sort chocolates by price
chocolates_sorted_by_price = sorted(chocolates, key=lambda x: x[1])

# Display sorted chocolates with associated student details
print("Chocolates sorted by weight:")
for chocolate, student in zip(chocolates_sorted_by_weight, students):
    print(f"Student: {student[0]}, Chocolate: (weight: {chocolate[0]} gm, price: {chocolate[1]} AED, "
          f"Type: {chocolate[2]}, ID: {chocolate[3]})")

print("\nChocolates sorted by price:")
for chocolate, student in zip(chocolates_sorted_by_price, students):
    print(f"Student: {student[0]}, Chocolate: (weight: {chocolate[0]} gm, price: {chocolate[1]} AED, "
          f"Type: {chocolate[2]}, ID: {chocolate[3]})")
print()


def search_chocolate(chocolates, criteria, value):#Searches for a chocolate based on specified criteria and value.
    #chocolates (list): List of chocolate data (weight, price, type, ID).
    #criteria (str): The search criteria ('price' or 'weight').
    #value (float): The value to search for (price or weight).
    #Returns:tuple or None: A tuple representing the found chocolate (weight, price, type, ID),
    #or None if no chocolate matches the criteria.
    for chocolate in chocolates:
        if criteria == 'price' and chocolate[1] == value:
            return chocolate
        elif criteria == 'weight' and chocolate[0] == value:
            return chocolate
    return None


# Test searching for chocolate
print("\nSearching for chocolate with price 5 AED:")
result = search_chocolate(chocolates_sorted_by_price, 'price', 5)
if result:
    print(
        f"Found chocolate: Student: {students[chocolates.index(result)][0]}, Chocolate: (weight: {result[0]} gm, price: {result[1]} AED, "
        f"Type: {result[2]}, ID: {result[3]})")
else:
    print("Chocolate not found.")

# Test searching for chocolate by weight
print("\nSearching for chocolate with weight 15 gm:")
result = search_chocolate(chocolates_sorted_by_weight, 'weight', 15)
if result:
    print(
        f"Found chocolate: Student: {students[chocolates.index(result)][0]}, Chocolate: (weight: {result[0]} gm, price: {result[1]} AED, "
        f"Type: {result[2]}, ID: {result[3]})")
else:
    print("Chocolate not found.")


