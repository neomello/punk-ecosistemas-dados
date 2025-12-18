"""
PUNK Ecosistemas - Google Search

Não é precisão científica.
É sinal de visibilidade.
"""

import requests
from bs4 import BeautifulSoup


def google_presence(query: str):
    """Retorna quantidade de resultados visíveis para a query."""
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    results = soup.select("div.g")
    return len(results)
