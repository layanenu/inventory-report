from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_name):
        if file_name.endswith(".xml"):
            tree = ET.parse(file_name)
            root = tree.getroot()

            file = []
            for product in root:
                item = {}
                for subproduct in product:
                    item[subproduct.tag] = subproduct.text
                file.append(item)
            return file
        raise ValueError("Arquivo inválido")
