# code by @tusharkhanna

import string
import random
import streamlit as st

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

st.title("Random Password Generator")
password_length = st.slider("Password Length", min_value=8, max_value=32, value=16, step=1)
generated_password = generate_password(password_length)
st.write("Generated Password:", generated_password)
