# How we built this site

## Mkdocs

## Theme

### Scheme Colors

1. Make sure that ```pallette:``` is under ```theme:``.
2. Make sure that ```scheme: default``` is under ```palette:```
3. Make sure that ```primary: blue``` and ```accent: orange``` is under ```scheme:```

```yaml
theme:
  name: material
  logo: img/code-savvy-logo.png
  favicon: img/favicon.ico
  include_sidebar: true
  features:
    - content.code.copy
    - navigation.expand
    - navigation.path
    - navigation.prune
    - navigation.indexes
    - toc.follow
    - navigation.top
    # this adds the prev and next icons in the footer
    - navigation.footer
  palette:
    - scheme: default
      primary: blue
      accent: orange
```

## Social

```yaml
  - social:
    cards_layout: default/variant
```