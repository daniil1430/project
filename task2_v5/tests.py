import unittest
from main import import_statement, _registry, IParser, register


class TestImportStatement(unittest.TestCase):

    def test_csv_import(self):
        csv_data = "date,amount\n2024-01-01,1000\n2024-01-02,500"
        result = import_statement(csv_data)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["date"], "2024-01-01")

    def test_json_import(self):
        json_data = '[{"date": "2024-01-01", "amount": 1000}]'
        result = import_statement(json_data)
        self.assertEqual(len(result), 1)

    def test_xml_import(self):
        xml_data = '<transactions><transaction date="2024-01-01" amount="1000"/></transactions>'
        result = import_statement(xml_data)
        self.assertEqual(len(result), 1)

    def test_unknown_format_error(self):
        with self.assertRaises(ValueError):
            import_statement("просто текст")


class TestRegistry(unittest.TestCase):

    def test_register_new_parser(self):
        @register("TSV")
        class TSVParser(IParser):
            def parse(self, content: str) -> list:
                return [{"format": "TSV", "data": content}]

        self.assertIn("TSV", _registry)

    def test_all_formats_registered(self):
        self.assertIn("CSV", _registry)
        self.assertIn("JSON", _registry)
        self.assertIn("XML", _registry)


if __name__ == "__main__":
    unittest.main()