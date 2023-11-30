import streamlit as st

st.title("Bolsonaro vs Lula - UFC")

num1 = st.number_input("Diga o valor da primeira aposta")
num2 = st.number_input("Diga o valor da segunda aposta")

if st.button("Valor total apostado"):
    resultado = num1 + num2
    st.text("Valor apostado:")
    st.text(resultado)