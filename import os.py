import os

os.system("cls")

primeiro_numero = int(input("Insira seu primeiro numero:"))
segundo_numero = int(input("Insira seu segundo numero:"))
operacao_basica = int(input("Insira qual operaçao matematica voçe ira usar(+ - * /):"))

match operacao_basica:
  case "+":
      print("primeiro_numero + segundo_numero")
  case "-":
      print("primeiro_numero - segundo_numero")
  case "*":
      print("orimeiro_numero * segundo_numero")
  case "/":
      print("primeiro_numero / segundo numero")
  case _:
       print("Opção inválida.") 
       resultado = 0
       
print(f"Resultado: {resultado}")                 