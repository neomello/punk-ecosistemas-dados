"""
PUNK Ecosistemas - Instagram

Isso sozinho já impressiona.
Nota: Requer login para evitar rate limiting.
"""

import instaloader


def instagram_profile(username: str):
    """Retorna métricas básicas do perfil."""
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)

        return {
            "followers": profile.followers,
            "posts": profile.mediacount,
            "engagement_hint": "high" if profile.followers > 5000 else "medium"
        }
    except Exception as e:
        return {
            "error": "Instagram requer login ou rate limited",
            "hint": "Coletar dados manualmente por enquanto",
            "url": f"https://instagram.com/{username}"
        }
