login = False

while(not login):
    senha = input()

    if(senha != "2002"):
        print("Senha Invalida")
        login = False
    elif(senha == "2002"):
        print("Acesso Permitido")
        login = True