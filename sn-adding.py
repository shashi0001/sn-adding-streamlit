import streamlit as st

st.title("Fun Adding App for Toddlers")
st.write("Let's add two numbers together!")

# Ask for the first number
first_number = st.number_input("Enter the first number:", step=1)

# Ask for the second number
second_number = st.number_input("Enter the second number:", step=1)

# Calculate the sum
if st.button("Add"):
    result = first_number + second_number
    st.write(f"The sum is: {result}")
st.write("Hurray you got the answer👍")
