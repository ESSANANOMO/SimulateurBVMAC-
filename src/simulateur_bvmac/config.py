"""Paramètres globaux de configuration pour le simulateur."""

from dataclasses import dataclass


@dataclass
class SimulationConfig:
    """Paramètres de simulation du modèle BVMAC."""

    horizon: int = 365
    taux_croissance: float = 0.02
    seuil_reaction: float = 0.5
    valeur_initiale: float = 100.0

    @property
    def description(self) -> str:
        return (
            f"Simulation sur {self.horizon} périodes, "
            f"taux={self.taux_croissance}, "
            f"seuil={self.seuil_reaction}, "
            f"valeur_initiale={self.valeur_initiale}"
        )
