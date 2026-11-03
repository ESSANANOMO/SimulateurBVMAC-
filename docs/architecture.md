# Architecture du projet

## Vue d'ensemble

Le projet est structuré comme un simulateur Python modulable, avec une logique de calcul séparée des structures de données et de la visualisation.

## Composants

- `config.py` : paramètres de simulation
- `models.py` : objets métier
- `simulator.py` : moteur central du calcul
- `visualization.py` : affichage et rendu
- `__main__.py` : point d’entrée du programme

## Évolution prévue

1. Ajouter des scénarios plus complexes
2. Ajouter un système d’import/export des résultats
3. Ajouter une interface Streamlit ou FastAPI
4. Ajouter des tests plus fins et des cas de bord
