from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(file_name, type_file):
        file_types = {
            "csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter
        }
        if type_file == "simples":
            verify_type = file_name.split(".")[1]
            report = SimpleReport.generate(
                file_types[verify_type].import_data(file_name)
            )
            return report
        if type_file == "completo":
            verify_type = file_name.split(".")[1]
            report = CompleteReport.generate(
                file_types[verify_type].import_data(file_name)
            )
            return report
