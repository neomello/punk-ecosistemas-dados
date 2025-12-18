"""
Website Analysis
Coleta de dados estruturados de sites.
"""

import requests
from typing import Optional
from urllib.parse import urlparse
import re


def website_status(url: str) -> dict:
    """
    Verifica status básico de um website.
    """
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        return {
            "url": url,
            "final_url": response.url,
            "status_code": response.status_code,
            "ok": response.ok,
            "redirected": response.url != url,
            "ssl": response.url.startswith("https"),
            "response_time_ms": int(response.elapsed.total_seconds() * 1000)
        }
    except requests.RequestException as e:
        return {
            "url": url,
            "status_code": 0,
            "ok": False,
            "error": str(e)
        }


def website_meta(url: str) -> dict:
    """
    Extrai meta tags de um website.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        
        # Title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        
        # Meta description
        desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
        description = desc_match.group(1) if desc_match else ""
        
        # OG tags
        og_title_match = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        og_title = og_title_match.group(1) if og_title_match else ""
        
        og_image_match = re.search(r'<meta[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
        og_image = og_image_match.group(1) if og_image_match else ""
        
        # Canonical
        canonical_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', html, re.IGNORECASE)
        canonical = canonical_match.group(1) if canonical_match else ""
        
        # Analytics
        has_ga = "google-analytics.com" in html or "gtag" in html or "UA-" in html or "G-" in html
        has_gtm = "googletagmanager.com" in html
        has_fb_pixel = "facebook.com/tr" in html or "fbq(" in html
        
        return {
            "url": url,
            "title": title,
            "description": description,
            "og_title": og_title,
            "og_image": og_image,
            "canonical": canonical,
            "analytics": {
                "google_analytics": has_ga,
                "google_tag_manager": has_gtm,
                "facebook_pixel": has_fb_pixel
            }
        }
    except requests.RequestException as e:
        return {"url": url, "error": str(e)}


def website_links(url: str) -> dict:
    """
    Extrai links de um website.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        
        # Encontrar todos os links
        links = re.findall(r'href=["\']([^"\']+)["\']', html)
        
        parsed_base = urlparse(url)
        base_domain = parsed_base.netloc
        
        internal = []
        external = []
        social = {
            "instagram": [],
            "facebook": [],
            "youtube": [],
            "twitter": [],
            "linkedin": [],
            "whatsapp": []
        }
        
        for link in links:
            if not link or link.startswith("#") or link.startswith("javascript:"):
                continue
                
            # Normalizar link
            if link.startswith("/"):
                link = f"{parsed_base.scheme}://{base_domain}{link}"
            
            parsed = urlparse(link)
            
            # Classificar
            if "instagram.com" in link:
                social["instagram"].append(link)
            elif "facebook.com" in link:
                social["facebook"].append(link)
            elif "youtube.com" in link or "youtu.be" in link:
                social["youtube"].append(link)
            elif "twitter.com" in link or "x.com" in link:
                social["twitter"].append(link)
            elif "linkedin.com" in link:
                social["linkedin"].append(link)
            elif "wa.me" in link or "whatsapp.com" in link:
                social["whatsapp"].append(link)
            elif parsed.netloc == base_domain:
                if link not in internal:
                    internal.append(link)
            elif parsed.netloc:
                if link not in external:
                    external.append(link)
        
        # Dedupe social
        for key in social:
            social[key] = list(set(social[key]))
        
        return {
            "url": url,
            "internal_links": len(internal),
            "external_links": len(external),
            "social_links": social,
            "top_internal": internal[:10]
        }
    except requests.RequestException as e:
        return {"url": url, "error": str(e)}


def website_full_analysis(url: str) -> dict:
    """
    Análise completa de um website.
    """
    status = website_status(url)
    
    if not status.get("ok"):
        return {"url": url, "error": status.get("error", "Site inacessível")}
    
    meta = website_meta(url)
    links = website_links(url)
    
    return {
        "url": url,
        "status": status,
        "meta": meta,
        "links": links
    }


if __name__ == "__main__":
    print("[>] Testando Website Analysis...")
    
    url = "https://punkcrossfit.com.br"
    
    print(f"\n[>] Status de {url}")
    status = website_status(url)
    print(f"    Status: {status.get('status_code')}")
    print(f"    SSL: {status.get('ssl')}")
    print(f"    Response: {status.get('response_time_ms')}ms")
    
    print(f"\n[>] Meta tags")
    meta = website_meta(url)
    print(f"    Title: {meta.get('title', 'N/A')[:50]}...")
    print(f"    GA: {meta.get('analytics', {}).get('google_analytics')}")
    
    print(f"\n[>] Links")
    links = website_links(url)
    print(f"    Internal: {links.get('internal_links')}")
    print(f"    External: {links.get('external_links')}")
    print(f"    Instagram: {links.get('social_links', {}).get('instagram')}")
