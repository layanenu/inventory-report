from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        report = SimpleReport.generate(data)
        report += "\nProdutos estocados por empresa:\n"
        companies = Counter([item["nome_da_empresa"] for item in data])
        for company, quantity in companies.items():
            report += f"- {company}: {quantity}\n"
        return report
