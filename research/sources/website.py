"""
PUNK Ecosistemas - Website Status

Simples e direto.
"""

import requests


def website_status(url: str):
    """Verifica se o site está acessível."""
    try:
        r = requests.get(url, timeout=5)
        return {
            "status": r.status_code,
            "reachable": True
        }
    except:
        return {
            "status": None,
            "reachable": False
        }
