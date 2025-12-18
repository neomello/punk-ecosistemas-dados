# ◈ PUNK Branding Guidelines

> Padrões visuais e técnicos para manter consistência no ecossistema PUNK.

---

## ◇ Paleta de Cores

### CSS Variables (Site Atual)

```css
:root {
  --site-bg-color: #FFF;
  --site-text-color: #777777;
  --site-heading-color: #040404;
  --site-accent-color: #040404;
  --site-accent-color-2: #000000;
  --site-border-color: #ebebeb;
  --site-link-color: #292929;
  --site-link-hover-color: #040404;
}
```

### Mapeamento Tailwind

| Uso | Classe Tailwind | Hex |
|-----|-----------------|-----|
| Background | `bg-white` | `#FFF` |
| Texto | `text-gray-600` | `#777777` |
| Headings | `text-gray-900` | `#040404` |
| Accent | `text-black`, `bg-black` | `#000000` |
| Borders | `border-gray-200` | `#ebebeb` |
| Links | `text-gray-800` | `#292929` |

### Cores da Marca PUNK

| Elemento | Cor | Uso |
|----------|-----|-----|
| **Primária** | `#FF6B00` (Laranja) | Highlights, CTAs, destaque |
| **Secundária** | `#000000` (Preto) | Backgrounds, borders, text |
| **Destaque** | `#1a1a1a` (Preto suave) | Subgrupos, containers |
| **Erro** | `#FF0000` (Vermelho) | Bloqueios, rejeições |

---

## ◎ Breakpoints Responsivos

| Dispositivo | Tamanho | Tailwind |
|-------------|---------|----------|
| Mobile | < 768px | `sm:` (padrão) |
| Tablet | 768px - 1024px | `md:` |
| Desktop | > 1024px | `lg:` e `xl:` |

---

## ⧉ Bibliotecas Sugeridas

| Biblioteca | Uso |
|------------|-----|
| **Framer Motion** | Animações complexas |
| **Swiper.js** | Carrosséis (se necessário) |
| **React Icons** | Ícones (WhatsApp, redes sociais) |
| **Next.js Image** | Otimização de imagens |

---

## ◬ Pontos de Atenção

### Mídia

| Elemento | Implementação |
|----------|---------------|
| Vídeo de fundo | `next-video` ou iframe do YouTube |
| Imagens | Next.js `Image` com `placeholder="blur"` |
| Hotspots | Posicionamento absoluto + tooltips |

### Componentes

| Elemento | Implementação |
|----------|---------------|
| Cards expansivos | Estado React para controlar expansão |
| Animações de texto | Framer Motion ou CSS puro |
| Menu mobile | Toggle com estado React |

---

## ⬡ Convenções de Código

### Princípios

- ◉ **Mobile-first approach** — Começar pelo mobile
- ◉ **Componentes funcionais** — Usar hooks
- ◉ **DRY** — Don't Repeat Yourself
- ◉ **TypeScript** — Opcional, mas recomendado
- ◉ **PascalCase** — Para componentes React

### Estrutura de Componentes

```tsx
// ◉ Correto
const CardUnidade = ({ nome, imagem }: CardUnidadeProps) => {
  return (
    <div className="bg-black text-white">
      {/* ... */}
    </div>
  );
};

// ✗ Evitar
function card_unidade(props) {
  // ...
}
```

---

## ◇ Tipografia

### Fontes Disponíveis

| Fonte | Peso | Uso |
|-------|------|-----|
| **Blender Pro Bold** | 700 | Títulos, CTAs |
| **Blender Pro Medium** | 500 | Subtítulos, destaques |

### Localização

```
public/fonts/
├── Blender-Pro-Bold.ttf
└── Blender-Pro-Medium.ttf
```

---

<div align="center">

**Soberania Digital em Preto e Laranja**

<sub>Ø((Ø))</sub>

</div>
