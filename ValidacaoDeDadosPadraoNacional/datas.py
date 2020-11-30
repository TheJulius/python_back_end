from datetime import datetime, timedelta

class datas:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastrp(self):
        meses_do_ano = ["janeiro", "fevereiro", "marco",
                        "abril", "maio", "junho", "julho",
                        "agosto", "setembro", "outubro",
                        "novembro", "dezembro1"
                        ]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = ["segunda", "terca", "quarta",
                            "quinta", "sexta", "sabado",
                            "domingo"
                            ]
        dia_semana = datetime.weekday()
        return dia_semana_lista[dia_semana]

    def formata_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30))- self.momento_cadastro
        return tempo_cadastro