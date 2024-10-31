from enum import Enum


class GetPlanSimphonyByIdMode(str, Enum):
    OPEN = "open"
    STRICT = "strict"

    def __str__(self) -> str:
        return str(self.value)
