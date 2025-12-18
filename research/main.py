#!/usr/bin/env python3
"""
PUNK Ecosistemas - Research

Coleta de sinais. Entrega real.
"""

from sources.google import google_presence
from sources.instagram import instagram_profile
from sources.website import website_status

print("[*] Iniciando pesquisa PUNK CROSSFIT\n")

# Google
print("[>] Google...")
google_hits = google_presence("Punk Crossfit Goiânia")
print(f"    Resultados: {google_hits}\n")

# Instagram
print("[>] Instagram...")
instagram = instagram_profile("punkcrossfit")
print(f"    {instagram}\n")

# Website
print("[>] Website...")
site = website_status("https://www.punkeldorado.com.br")
print(f"    {site}\n")

# Resumo
print("─" * 40)
print("[+] Coleta finalizada")
print("[i] Edite output/report.md com os dados")
