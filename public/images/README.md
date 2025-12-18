# Estrutura de Imagens

As imagens foram organizadas por categorias para facilitar a manutenção e uso no projeto.

## 📁 Estrutura de Diretórios

```
public/images/
├── logo/              # Logos da marca
├── galeria/           # Imagens da galeria principal
├── unidades/          # Imagens das unidades (Marista, Jardim Goiás, Eldorado)
├── modalidades/       # Imagens das modalidades (CrossFit, Musculação, HYROX, Kids)
├── sobre/            # Imagens da seção "Sobre a Punk"
└── outros/            # Imagens diversas (não categorizadas)
```

## 📋 Conteúdo por Diretório

### `logo/`
- `01-Punk_CROSSFIT_LOGO-new-orag.png` - Logo principal
- `Crossfit-Logo.png` - Logo CrossFit
- `LOGO-EURO-AZUL-768x332.png` - Logo Euro Azul

### `galeria/`
17 imagens da galeria principal do site:
- `2017-10-25-PHOTO-00000026.png`
- `JFE_6423.png`
- `IMG_0247-1.png`
- `DSC07759.png`
- `FLW08322.png`
- `IMG_0215-1.png`
- `IMG_4086-1.png`
- `IMG_4093-1.png`
- `DSC03600.png`
- `JFE_0069.png`
- `FLW02625.png`
- `IMG_0043.png`
- `DSC07647.png`
- `DSC04041.png`
- `DSC03606.png`
- `DSC_2245.png`
- `DSC_0991.png`

### `unidades/`
- `Marista.jpg` - Unidade Marista
- `Jardim-Goias.jpg` - Unidade Jardim Goiás
- `Eldorado.jpg` - Unidade Eldorado
- `FACHADA.jpg` - Fachada de uma das unidades

### `modalidades/`
- `FLW08934.png` - CrossFit
- `MockUp1-1.png` - Musculação
- `MockUp2-1.png` - HYROX
- `MockUp3-1.png` - Crossfit Kids
- `MockUp4.png` - Outra modalidade

### `sobre/`
- `PUNK-CROSSFIT.jpg` - Imagem principal sobre a Punk
- `JFE_9891.jpg` - Estrutura
- `JFE_9892.jpg` - Comunidade
- `DSC_0851-qujwbw2sprvkknn1l75jkdu4am3ttanlrjqf55a4u8.png` - Imagem da seção "Acreditamos"

## 🔗 Uso no Componente React

Todas as imagens são referenciadas usando caminhos relativos a partir de `/images/`:

```tsx
// Logo
<Image src="/images/logo/01-Punk_CROSSFIT_LOGO-new-orag.png" ... />

// Galeria
<Image src="/images/galeria/DSC07759.png" ... />

// Unidades
<Image src="/images/unidades/Marista.jpg" ... />

// Modalidades
<Image src="/images/modalidades/FLW08934.png" ... />
```

## 📝 Notas

- Todas as imagens foram baixadas do site original usando o script `downloadMedia.js`
- As imagens estão otimizadas para uso com Next.js Image component
- Para adicionar novas imagens, coloque-as no diretório apropriado e atualize o componente React

