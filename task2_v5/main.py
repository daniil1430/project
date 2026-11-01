from abc import ABC, abstractmethod
from typing import Dict, Type, List
import csv


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