from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

julio = Usuario("Julio")
eva = Usuario("Eva")

lance_do_julio = Lance(julio, 100)
lance_da_eva = Lance(eva, 150)

leilao = Leilao("celular")

leilao.lances.append(lance_da_eva)
leilao.lances.append(lance_do_julio)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome}, de um lance de {lance.valor}")

avaliador = Avaliador()

avaliador.avalia(leilao)

print(f"O menor lance foi de: {avaliador.menor_lance}. E o maior lance foi de: {avaliador.maior_lance}")