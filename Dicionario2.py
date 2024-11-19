produtos = {}
print ("---Cadastre seus produtos:")

while True:
    cod = input("    Digite o código: ")
    if cod == '':
        break
    elif cod in produtos:
        print (f"Este código {cod} já existe")
        
        continue
    preco = float(input("    Digite o preço: "))
    produtos[cod] = preco
    
   

print ("---Fim do cadastro\n")
print ("---Produtos cadastrados---")
for cod in produtos.keys():
    print (f"Produto {cod} --- R$ {produtos[cod]:6.2f}")

