# À revoir — ordre de travail

> Version charte : [`README.html`](README.html) · Checklist : [`pbs-wbs-dod-a-revoir.html`](pbs-wbs-dod-a-revoir.html)

## Contenu de ce dossier

| Élément | Rôle |
| --- | --- |
| **`mvp-pbs/`** | PBS, WBS, DoD — chaque `.md` a son `.html` charte au même emplacement |
| **`pbs-wbs-dod-a-revoir.md`** | Checklist avec liens MD + HTML |
| **`plan-de-communication/`** | Plan com (HTML + PDF) en cours de relecture |

## Processus

1. **Relire** les docs (fond dans `.md`, mise en forme dans `.html`).
2. **Regénérer les HTML** après modification MD : `python scripts/generate-a-revoir-html.py`
3. **Charte** — CSS : [`../2-en-cours/charte-graphique/flowlearn-document.css`](../2-en-cours/charte-graphique/flowlearn-document.css)
4. **Archivage** → [`../4-termine/`](../4-termine/) quand la version est figée.

Index global : [`../../00-guide-lecture.md`](../../00-guide-lecture.md)
