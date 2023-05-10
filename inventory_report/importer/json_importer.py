from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.endswith(".json"):
            with open(file_name, mode="r", encoding="utf8") as json_file:
                return json.load(json_file)
        raise ValueError("Arquivo inválido")
