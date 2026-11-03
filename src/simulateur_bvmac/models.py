"""Modèles de données utilisés par le simulateur."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ResultatSimulation:
    """Contient les résultats calculés d’une simulation."""

    temps: List[float] = field(default_factory=list)
    valeurs: List[float] = field(default_factory=list)

    def ajouter(self, temps: float, valeur: float) -> None:
        self.temps.append(temps)
        self.valeurs.append(valeur)


@dataclass
class ScenarioSimulation:
    """Scénario de simulation pour le modèle BVMAC."""

    nom: str = "scénario_base"
    horizon: int = 365
    valeur_initiale: float = 100.0
    taux_croissance: float = 0.02
    seuil_reaction: float = 0.5
