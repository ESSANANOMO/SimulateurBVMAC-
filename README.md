# Simulateur BVMAC

Projet de simulation du modèle BVMAC.

## Objectif

Ce projet a pour but de fournir une base de simulation, de calcul et de visualisation pour le modèle BVMAC.

## Structure du projet

- `src/simulateur_bvmac/` : code source principal
- `tests/` : tests unitaires
- `docs/` : documentation technique
- `data/` : jeux de données de démonstration

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Lancement

```bash
python -m simulateur_bvmac
```

## Exemple de sortie

Le simulateur affiche un scénario de base ainsi qu’un ensemble de métriques calculées à partir des paramètres de simulation.

## Développement

- Langage principal : Python
- Bibliothèques principales : NumPy, pandas, matplotlib
- Tests : pytest
