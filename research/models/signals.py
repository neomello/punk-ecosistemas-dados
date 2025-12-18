"""
PUNK Ecosistemas - Modelo de Sinal

Simples. Legível. Mostrável.
"""

from dataclasses import dataclass


@dataclass
class Signal:
    source: str
    metric: str
    value: str
    observation: str
