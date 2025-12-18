"""
Instagram Data Collection
Coleta de dados públicos do Instagram.
"""

import os
import requests
import re
import json
from typing import Optional


def instagram_profile_public(username: str) -> dict:
    """
    Coleta dados públicos de perfil Instagram.
    Não requer API key - usa dados públicos.
    
    NOTA: Instagram pode bloquear requests frequentes.
    Use com moderação.
    """
    url = f"https://www.instagram.com/{username}/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return {"username": username, "error": "Perfil não encontrado"}
        
        if response.status_code != 200:
            return {"username": username, "error": f"Status {response.status_code}"}
        
        html = response.text
        
        # Tentar extrair dados do meta tags
        followers_match = re.search(r'"edge_followed_by":\{"count":(\d+)\}', html)
        following_match = re.search(r'"edge_follow":\{"count":(\d+)\}', html)
        posts_match = re.search(r'"edge_owner_to_timeline_media":\{"count":(\d+)', html)
        
        # Meta description tem formato: "X Followers, Y Following, Z Posts"
        meta_match = re.search(r'content="([\d,\.KMkm]+)\s*Followers', html)
        
        # Nome e bio
        name_match = re.search(r'"full_name":"([^"]*)"', html)
        bio_match = re.search(r'"biography":"([^"]*)"', html)
        
        # Verificado
        verified_match = re.search(r'"is_verified":(true|false)', html)
        
        # Business
        business_match = re.search(r'"is_business_account":(true|false)', html)
        
        return {
            "username": username,
            "url": url,
            "followers": int(followers_match.group(1)) if followers_match else None,
            "following": int(following_match.group(1)) if following_match else None,
            "posts": int(posts_match.group(1)) if posts_match else None,
            "full_name": name_match.group(1) if name_match else None,
            "bio": bio_match.group(1).encode().decode('unicode_escape') if bio_match else None,
            "is_verified": verified_match.group(1) == "true" if verified_match else None,
            "is_business": business_match.group(1) == "true" if business_match else None,
            "note": "Dados podem estar incompletos (proteção do Instagram)"
        }
        
    except requests.RequestException as e:
        return {"username": username, "error": str(e)}


def instagram_profile(username: str) -> dict:
    """
    Wrapper principal para coleta de perfil Instagram.
    Tenta API primeiro, depois fallback para scraping público.
    """
    # Por agora, usa apenas método público
    # TODO: Implementar via Meta Graph API quando disponível
    return instagram_profile_public(username)


def format_instagram_report(data: dict) -> str:
    """
    Formata dados do Instagram para relatório.
    """
    if "error" in data:
        return f"Erro: {data['error']}"
    
    lines = [
        f"@{data['username']}",
        f"  Nome: {data.get('full_name', 'N/A')}",
        f"  Followers: {data.get('followers', 'N/A'):,}" if data.get('followers') else "  Followers: N/A",
        f"  Following: {data.get('following', 'N/A'):,}" if data.get('following') else "  Following: N/A",
        f"  Posts: {data.get('posts', 'N/A'):,}" if data.get('posts') else "  Posts: N/A",
        f"  Verificado: {'Sim' if data.get('is_verified') else 'Não'}",
        f"  Business: {'Sim' if data.get('is_business') else 'Não'}"
    ]
    
    return "\n".join(lines)


if __name__ == "__main__":
    print("[>] Testando Instagram...")
    
    profiles = ["punkcrossfit"]
    
    for username in profiles:
        print(f"\n[>] @{username}")
        data = instagram_profile(username)
        
        if "error" in data:
            print(f"    [!] {data['error']}")
        else:
            print(format_instagram_report(data))
