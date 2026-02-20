# 1. Import necessary libraries

# 2. Define the list of characters allowed in the password

# 3. Ask the user for the password length

# 4. Generate the password

# 5. Print the result

import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation
length = int(input("Enter password length:"))
password = "" .join(random.choices(all_characters, k=length))

print(password)





