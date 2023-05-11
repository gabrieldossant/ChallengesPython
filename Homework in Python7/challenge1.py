email = input("Entre com seu E-mail: ")
dominio = ""

dividir = email.split("@")
dominio = dividir[-1]
print(f"Domínio: http://{dominio}")