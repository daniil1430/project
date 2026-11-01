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