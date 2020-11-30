from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.eva = Usuario("Eva", 500.0)
        self.lance_da_eva = Lance(self.eva, 150)
        self.leilao = Leilao("celular")

    def test_deve_retornar_o_maior_e_o_menor_de_um_lance_quando_adicionados_em_ordem_crescente(self):

        julio = Usuario("Julio", 500.0)
        lance_do_julio = Lance(julio, 100)

        self.leilao.propoe(lance_do_julio)
        self.leilao.propoe(self.lance_da_eva)

        menor_lance = 100.0
        maior_lance = 150.0

        self.assertEqual(menor_lance, self.leilao.menor_lance) #verifica se o primeiro parametro e igual ao segundo
        self.assertEqual(maior_lance, self.leilao.maior_lance)  # verifica se o primeiro parametro e igual ao segundo

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            julio = Usuario("Julio", 500.0)
            lance_do_julio = Lance(julio, 100)

            self.leilao.propoe(self.lance_da_eva)
            self.leilao.propoe(lance_do_julio)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_da_eva)

        self.assertEqual(150.0, self.leilao.menor_lance)  # verifica se o primeiro parametro e igual ao segundo
        self.assertEqual(150.0, self.leilao.maior_lance)  # verifica se o primeiro parametro e igual ao segundo

    def test_deve_retornar_o_maior_e_o_menor_de_um_lance_quando_o_leilao_tiver_3_lances(self):

        julio = Usuario("Julio", 500.0)
        lance_do_julio = Lance(julio, 100)

        andrey = Usuario("Andrey", 500.0)
        lance_do_andrey = Lance(andrey, 200)

        self.leilao.propoe(self.lance_da_eva)
        self.leilao.propoe(lance_do_julio)
        self.leilao.propoe(lance_do_andrey)

        menor_lance = 100.0
        maior_lance = 200.0

        self.assertEqual(menor_lance, self.leilao.menor_lance)  # verifica se o primeiro parametro e igual ao segundo
        self.assertEqual(maior_lance, self.leilao.maior_lance)  # verifica se o primeiro parametro e igual ao segundo

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):

        self.leilao.propoe(self.lance_da_eva)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):

        julio = Usuario("Julio", 500.0)
        lance_do_julio = Lance(julio, 200)

        self.leilao.propoe(self.lance_da_eva)
        self.leilao.propoe(lance_do_julio)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):

        lance_da_eva200 = Lance(self.eva, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_da_eva)
            self.leilao.propoe(lance_da_eva200)


