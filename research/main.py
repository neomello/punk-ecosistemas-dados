#!/usr/bin/env python3
"""
PUNK Ecosistemas - Research
Coleta de sinais. Entrega real.

Usage:
    python main.py              # Executa coleta completa
    python main.py --quick      # Apenas verificação rápida
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Carregar .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from sources.google import google_presence, google_maps_search
from sources.instagram import instagram_profile, format_instagram_report
from sources.website import website_status, website_meta, website_links


def separator(title: str = ""):
    print(f"\n{'─' * 50}")
    if title:
        print(f"  {title}")
        print(f"{'─' * 50}")


def run_research():
    """Executa pesquisa completa."""
    
    print("=" * 50)
    print("  PUNK ECOSISTEMAS - RESEARCH")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)
    
    results = {
        "timestamp": datetime.now().isoformat(),
        "google": {},
        "instagram": {},
        "websites": {},
        "maps": {}
    }
    
    # ─────────────────────────────────────────────────
    # GOOGLE SEARCH
    # ─────────────────────────────────────────────────
    separator("GOOGLE SEARCH")
    
    queries = [
        "Punk Crossfit Goiânia",
        "Punk Crossfit Marista",
        "Punk Crossfit Eldorado",
        "Punk Crossfit Jardim Goiás"
    ]
    
    for query in queries:
        print(f"\n[>] {query}")
        data = google_presence(query)
        
        if "error" in data and not data.get("top_results"):
            print(f"    [!] {data['error']}")
        else:
            print(f"    [+] Resultados: {data.get('total_organic', 0)}")
            print(f"    [+] Knowledge Graph: {'Sim' if data.get('has_knowledge_graph') else 'Não'}")
            if data.get("top_domains"):
                print(f"    [+] Top domínios: {list(data['top_domains'].keys())[:3]}")
        
        results["google"][query] = data
    
    # ─────────────────────────────────────────────────
    # GOOGLE MAPS / PLACES
    # ─────────────────────────────────────────────────
    separator("GOOGLE MAPS")
    
    print("\n[>] Punk Crossfit Goiânia")
    maps_data = google_maps_search("Punk Crossfit", "Goiânia")
    
    if "error" in maps_data:
        print(f"    [!] {maps_data['error']}")
    else:
        print(f"    [+] Locais encontrados: {maps_data.get('total_places', 0)}")
        for place in maps_data.get("places", [])[:4]:
            rating = place.get("rating", "N/A")
            reviews = place.get("reviews", "N/A")
            print(f"    - {place.get('title')}: {rating}★ ({reviews} reviews)")
    
    results["maps"] = maps_data
    
    # ─────────────────────────────────────────────────
    # INSTAGRAM
    # ─────────────────────────────────────────────────
    separator("INSTAGRAM")
    
    profiles = ["punkcrossfit"]
    
    for username in profiles:
        print(f"\n[>] @{username}")
        data = instagram_profile(username)
        
        if "error" in data:
            print(f"    [!] {data['error']}")
        else:
            if data.get("followers"):
                print(f"    [+] Followers: {data['followers']:,}")
            if data.get("posts"):
                print(f"    [+] Posts: {data['posts']:,}")
            print(f"    [+] Business: {'Sim' if data.get('is_business') else 'Não'}")
        
        results["instagram"][username] = data
    
    # ─────────────────────────────────────────────────
    # WEBSITES
    # ─────────────────────────────────────────────────
    separator("WEBSITES")
    
    sites = [
        "https://punkcrossfit.com.br",
        "https://www.punkeldorado.com.br"
    ]
    
    for url in sites:
        print(f"\n[>] {url}")
        
        status = website_status(url)
        if not status.get("ok"):
            print(f"    [!] {status.get('error', 'Erro desconhecido')}")
            results["websites"][url] = {"error": status.get("error")}
            continue
        
        print(f"    [+] Status: {status['status_code']}")
        print(f"    [+] SSL: {'Sim' if status.get('ssl') else 'Não'}")
        print(f"    [+] Response: {status.get('response_time_ms')}ms")
        
        meta = website_meta(url)
        if meta.get("title"):
            print(f"    [+] Title: {meta['title'][:40]}...")
        
        analytics = meta.get("analytics", {})
        print(f"    [+] GA: {'Sim' if analytics.get('google_analytics') else 'Não'}")
        print(f"    [+] GTM: {'Sim' if analytics.get('google_tag_manager') else 'Não'}")
        print(f"    [+] FB Pixel: {'Sim' if analytics.get('facebook_pixel') else 'Não'}")
        
        links = website_links(url)
        social = links.get("social_links", {})
        if social.get("instagram"):
            print(f"    [+] Instagram: {social['instagram'][0]}")
        if social.get("whatsapp"):
            print(f"    [+] WhatsApp: {len(social['whatsapp'])} links")
        
        results["websites"][url] = {
            "status": status,
            "meta": meta,
            "links": links
        }
    
    # ─────────────────────────────────────────────────
    # SALVAR RESULTADOS
    # ─────────────────────────────────────────────────
    separator("SALVANDO")
    
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # JSON completo
    json_path = output_dir / "research_data.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"[+] Dados salvos em: {json_path}")
    
    # ─────────────────────────────────────────────────
    # RESUMO
    # ─────────────────────────────────────────────────
    separator("RESUMO")
    
    print(f"""
    Google Searches: {len(results['google'])}
    Maps Places: {results['maps'].get('total_places', 0)}
    Instagram Profiles: {len(results['instagram'])}
    Websites Analyzed: {len(results['websites'])}
    
    [+] Dados exportados para: output/research_data.json
    [i] Atualize output/report.md com os resultados
    """)
    
    print("─" * 50)
    print("  Coleta finalizada")
    print("─" * 50)
    
    return results


def quick_check():
    """Verificação rápida sem salvar."""
    print("[*] Quick check...")
    
    print("\n[>] Website principal")
    status = website_status("https://punkcrossfit.com.br")
    print(f"    Status: {status.get('status_code')} ({'OK' if status.get('ok') else 'ERRO'})")
    
    print("\n[>] Instagram")
    ig = instagram_profile("punkcrossfit")
    if ig.get("followers"):
        print(f"    @punkcrossfit: {ig['followers']:,} followers")
    else:
        print(f"    @punkcrossfit: {ig.get('error', 'Sem dados')}")
    
    print("\n[+] Quick check finalizado")


if __name__ == "__main__":
    if "--quick" in sys.argv:
        quick_check()
    else:
        run_research()
