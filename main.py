import streamlit as st
st.title("Largest among three numbers")

n1 = st.number_input("Enter number 1")
n2 = st.number_input("Enter number 2")
n2 = st.number_input("Enter number 3")
flag = st.button("Largest Number")

def largest_number(a,b,c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c
    

if flag:
  x = largest_number(n1,n2,n3)
  st.write("The Largest Number is: ", x)
