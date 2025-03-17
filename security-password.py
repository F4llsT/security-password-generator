import random #importando a biblioteca de randomização

print("Bem-vindo ao seu gerador de senha pessoal!") #título inicial

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$_&*()/1234567890" 
#alfabeto maiúsculo e minúsculo, além de alguns símbolos e números para a randomização

numero = int(input("Qual é o número de senhas que você deseja criar? "))
quantidade = int(input("Qual é o número de caracteres que você deseja para cada senha? "))
#requisição de valores sobre o número de senhas que o usuário deseja criar  
#e o número de caracteres destas.

