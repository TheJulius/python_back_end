from src.leilao.dominio import Usuario, Leilao
import pytest

from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def julio():
    return Usuario("Julio", 100.0)

@pytest.fixture
def leilao():
    return Leilao("Celular")

def test_deve_subtrair_valor_da_carterira_do_usuario_quando_este_propor_um_lance(julio,leilao):
    julio.propoe_lance(leilao, 50.0)

    assert julio.carteira == 50.0


def test_deve_permitir_propor_lances_quando_o_valor_e_menor_que_o_valor_da_carteira(julio,leilao):
    julio.propoe_lance(leilao, 1.0)
    assert julio.carteira == 99.0


def test_deve_permitir_quando_o_valor_e_igual_ao_valor_da_carteira(julio,leilao):
    julio.propoe_lance(leilao, 100.0)
    assert julio.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(julio,leilao):
    with pytest.raises(LanceInvalido):
        julio.propoe_lance(leilao, 200.0)