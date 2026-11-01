from abc import ABC, abstractmethod
from typing import Dict, Type, List
import csv
import json
import xml.etree.ElementTree as ET


class IParser(ABC):
    @abstractmethod
    def parse(self, content: str) -> List[dict]:
        pass

_registry: Dict[str, Type[IParser]] = {}

def register(format_name: str):
    def decorator(my_class):
        _registry[format_name] = my_class
        return my_class
    return decorator

@register("CSV")
class CSVParser(IParser):
    def parse(self, content: str) -> List[dict]:
        return list(csv.DictReader(content.strip().splitlines()))


@register("JSON")
class JSONParser(IParser):
    def parse(self, content: str) -> List[dict]:
        data = json.loads(content)
        return data if isinstance(data, list) else [data]


@register("XML")
class XMLParser(IParser):
    def parse(self, content: str) -> List[dict]:
        root = ET.fromstring(content)
        return [dict(elem.attrib) for elem in root.findall('.//transaction')]


def detect_format(content: str) -> str:
    content = content.strip()
    if content.startswith('{') or content.startswith('['):
        return "JSON"
    if content.startswith('<'):
        return "XML"
    if ',' in content.split('\n')[0]:
        return "CSV"
    raise ValueError(f"Неизвестный формат")


def import_statement(content: str) -> List[dict]:
    format_name = detect_format(content)
    if format_name not in _registry:
        raise ValueError(f"Нет парсера для {format_name}")
    return _registry[format_name]().parse(content)

if __name__ == "__main__":
    csv_data = "date,amount\n2024-01-01,1000\n2024-01-02,-500"
    print("CSV:", import_statement(csv_data))

    json_data = '[{"date": "2024-01-01", "amount": 1000}]'
    print("JSON:", import_statement(json_data))

    xml_data = '<transactions><transaction date="2024-01-01" amount="1000"/></transactions>'
    print("XML:", import_statement(xml_data))