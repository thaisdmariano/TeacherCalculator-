#Bibliotecas ultilizadas

import streamlit as st
import pandas as pd

#Criar funções de carregamento de dados


st.title("Calculadora do Professor")

st.write("Olá Bem-Vindo a calculadora do Professor")
st.write("Por favor siga as instruções a seguir")

FT = st.number_input("Insira a nota do Forum Temático:", min_value=0.0, max_value=20.0)
EX = st.number_input("Insira a nota dos Exercícios:", min_value=0.0, max_value=20.0)
SIS = st.number_input("Insira a nota da Sistematização:", min_value=0.0, max_value=20.0)
AD = st.number_input("Insira a nota da Avaliação da Disciplina:", min_value=0.0, max_value=40.0)

NOTA = FT + EX + SIS + AD
st.write("Nota: ", NOTA)

if NOTA >= 50:
  st.write("Seu aluno(a) foi Aprovado")
else:
  st.write("Seu aluno(a) foi Reprovado")

#Preparar as visualizações

#Criar interface do programa


