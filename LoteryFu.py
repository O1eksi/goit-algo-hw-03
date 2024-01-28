import random


def data_validation(min, max, quantity):
    """
    This function checks if the input values satisfy the following conditions:
    1. All input values must be integers.
    2. The range limits(minimum and maximum) should not exceed 1000.
    3. The minimum value should be greater than or equal to 1.
    4. The maximum value should be greater than or equal to 1.
    5. The maximum value should not be less than the minimum value.
    6. The quantity should not exceed the number of integers in the specified range.

    If all conditions are met, the function returns True, indicating valid input.
    Otherwise, it returns False.
    """
    numbers = (min, max, quantity)

    # Check if all values are integers
    if not all(isinstance(x, (int)) for x in numbers):
        return False

    # Check if range limits exceed 1000
    elif 1000 < min or 1000 < max:
        return False

    # Check if minimum value is less than 1
    elif 1 > min or 1 > max:
        return False

    # Check if maximum value is less than minimum value
    elif max < min:
        return False

    # Check if quantity exceeds the range size
    elif (max-min)+1 < quantity:
        return False

    # All conditions satisfied, input is valid
    else:
        return True


def get_numbers_ticket(min, max, quantity):

    list_of_luky_numbers = []

    #Parameter validation
    if data_validation(min, max, quantity) == False:
        return list_of_luky_numbers
    
    #Search for lucky numbers
    else:
        while quantity != 0:

            #Number generation
            number = random.randint(min, max)

            #Validation of existing numbers
            if number not in list_of_luky_numbers:
                list_of_luky_numbers.append(number)
                quantity -= 1
            else:
                continue

        return list_of_luky_numbers


print(get_numbers_ticket(15, 17, 2))

