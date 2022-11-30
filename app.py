import streamlit as st

st.title('Checking whether number is odd or even')
a = st.number_input('Enter a number')
result = ''
if a % 2 == 0:
  result = 'Odd'
else:
  result = 'Even'
st.write(result)
