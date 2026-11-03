"""Fonctions de visualisation des résultats de simulation."""

from __future__ import annotations

from typing import Sequence


def afficher_resultat(temps: Sequence[float], valeurs: Sequence[float]) -> None:
    """Affiche des informations simples sur les résultats."""
    if not temps or not valeurs:
        raise ValueError("Les listes de résultats sont vides.")

    print("Séquence de simulation")
    print("Temps | Valeur")
    for t, valeur in zip(temps, valeurs):
        print(f"{t:>5.1f} | {valeur:>10.2f}")
