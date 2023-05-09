from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(data):
        today = datetime.today()
        manufacturing_date = min([item["data_de_fabricacao"] for item in data])
        expiration_date = min(
            [
                item["data_de_validade"] for item in data
                if datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
                >= today
            ]
        )
        companies = Counter([item["nome_da_empresa"] for item in data])

        return f"""Data de fabricação mais antiga: {manufacturing_date}
Data de validade mais próxima: {expiration_date}
Empresa com mais produtos: {companies.most_common(1)[0][0]}"""
