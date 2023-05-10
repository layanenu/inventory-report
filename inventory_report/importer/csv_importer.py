from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.endswith(".csv"):
            with open(file_name, mode="r", encoding="utf8") as csv_file:
                file_csv = csv.DictReader(csv_file)
                return [row for row in file_csv]
        raise ValueError("Arquivo inválido")
