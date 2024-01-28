import re

def normalize_phone(phone_number):
    # Remove all non-digit characters except '+'
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Check if the number starts with '+'
    if cleaned_number.startswith('+'):
        # If yes, check if there is the international code '+38' in the number
        if '+38' not in cleaned_number:
            # If not, add it
            cleaned_number = '+38' + cleaned_number[1:]
    else:
        # If the number doesn't start with '+', add '+38'
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

raw_numbers = [
    "067\fhyf\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

