def numero_primo(numero):

    for numero in range (2, numero):
        primo = True

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print(numero)

numero_primo(2001)