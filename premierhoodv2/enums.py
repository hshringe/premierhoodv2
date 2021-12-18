from enum import Enum

class EnumWithChoices(Enum):
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class StockType(EnumWithChoices):
    INFLUENCE = "Influence"
    CREATIVITY = "Creativity"
    IMPACT = "Impact"

