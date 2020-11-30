from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return doc_cpf(documento)
        elif len(documento) == 14:
            return doc_cnpj(documento)
        else:
            raise ValueError("Quantidade de digitos invalida!!")

class doc_cpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Invalido!!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        valida_cpf = CPF()
        return valida_cpf.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class doc_cnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Invalido!!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
