"""
Google Search via Serper API
https://serper.dev/
"""

import os
import requests
from typing import Optional

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_URL = "https://google.serper.dev/search"


def google_search(query: str, num_results: int = 10) -> dict:
    """
    Busca no Google via Serper API.
    
    Args:
        query: Termo de busca
        num_results: Número de resultados (max 100)
    
    Returns:
        dict com resultados ou erro
    """
    if not SERPER_API_KEY:
        return {"error": "SERPER_API_KEY não configurada", "results": []}
    
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "q": query,
        "num": num_results,
        "gl": "br",  # Brasil
        "hl": "pt-br"  # Português
    }
    
    try:
        response = requests.post(SERPER_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e), "results": []}


def google_presence(entity: str) -> dict:
    """
    Analisa presença no Google de uma entidade.
    
    Returns:
        dict com métricas de presença
    """
    results = google_search(entity, num_results=20)
    
    if "error" in results and results.get("results") == []:
        return results
    
    organic = results.get("organic", [])
    knowledge_graph = results.get("knowledgeGraph", {})
    local_results = results.get("places", [])
    
    # Análise de domínios
    domains = {}
    for item in organic:
        link = item.get("link", "")
        domain = link.split("/")[2] if "://" in link else ""
        domains[domain] = domains.get(domain, 0) + 1
    
    return {
        "query": entity,
        "total_organic": len(organic),
        "has_knowledge_graph": bool(knowledge_graph),
        "knowledge_graph_title": knowledge_graph.get("title", ""),
        "local_results": len(local_results),
        "top_domains": dict(sorted(domains.items(), key=lambda x: -x[1])[:5]),
        "top_results": [
            {
                "title": r.get("title"),
                "link": r.get("link"),
                "position": r.get("position")
            }
            for r in organic[:5]
        ]
    }


def google_maps_search(business: str, location: str = "Goiânia") -> dict:
    """
    Busca local no Google Maps via Serper.
    """
    if not SERPER_API_KEY:
        return {"error": "SERPER_API_KEY não configurada"}
    
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "q": f"{business} {location}",
        "type": "places",
        "gl": "br",
        "hl": "pt-br"
    }
    
    try:
        response = requests.post(
            "https://google.serper.dev/places",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        
        places = data.get("places", [])
        return {
            "query": f"{business} {location}",
            "total_places": len(places),
            "places": [
                {
                    "title": p.get("title"),
                    "address": p.get("address"),
                    "rating": p.get("rating"),
                    "reviews": p.get("reviews"),
                    "type": p.get("type"),
                    "phone": p.get("phone"),
                    "website": p.get("website")
                }
                for p in places
            ]
        }
    except requests.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Teste rápido
    from dotenv import load_dotenv
    load_dotenv()
    
    print("[>] Testando Google Search...")
    result = google_presence("Punk Crossfit Goiânia")
    
    if "error" in result and not result.get("top_results"):
        print(f"[!] {result['error']}")
    else:
        print(f"[+] Resultados orgânicos: {result['total_organic']}")
        print(f"[+] Knowledge Graph: {result['has_knowledge_graph']}")
        print(f"[+] Locais: {result['local_results']}")
        print(f"[+] Top domínios: {result['top_domains']}")
