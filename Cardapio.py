import os

os.system("Cls")

 # Menu.
print("""
=============MENU==================     
Codigo       prato           valor       
1         Picanha            25,00    
2         Lasanha            20,0
3         Strogonof          18,00
4         Bife acebolado     15,00
5         Pão com ovo        5,00
""")
codigo = int(input("Digite o numero de seu prato:"))

match codigo:
   case 1:
       print("Picanha           25,00")
   case 2:
       print("Lasanha        20,00")
   case 3:
       print("Strogonof      18,00")
   case 4:
       print("Bife acebolado 15,00")
   case 5:
        print("Pão com ovo   5,00")                