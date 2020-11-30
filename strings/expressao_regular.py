import re

email_1 = "Meu numero e 1234-1234"
email_2 = "Fale comigo em 12341234 esse e o meu telefone"
email_3 = "12341234 e o meu celular 1234-1234"

padrao = "[0-9]{4,5}[-]?[0-9]{4}"

retorno = re.findall(padrao, email_3)
print(retorno)
