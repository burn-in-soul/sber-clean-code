from dataclasses import dataclass


@dataclass
class Asset:
    """Актив"""
    name: str

    def __str__(self) -> str:
        return self.name
