import streamlit as st
import random
import string

# 1. Title and Description
st.title("🔐 Secure Password Generator")
st.write("Generate strong passwords instantly.")

# 2. The Slider (User Input)
length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# 3. The Options (Checkbox)
use_digits = st.checkbox("Include Numbers (0-9)", value=True)
use_special = st.checkbox("Include Symbols (!@#$)", value=True)

# 4. The Logic (Inside the Button)
if st.button("Generate Password"):
    # Start with just letters
    characters = string.ascii_letters
    
    # Add numbers if checked
    if use_digits:
        characters += string.digits
        
    # Add symbols if checked
    if use_special:
        characters += string.punctuation

    # generate the password
    password = "".join(random.choices(characters, k=length))

    # 5. Display the result
    st.success("Your password is:")
    st.code(password)
    