"""Logique du simulateur BVMAC."""

from __future__ import annotations

from simulateur_bvmac.config import SimulationConfig
from simulateur_bvmac.models import ResultatSimulation, ScenarioSimulation


def calculate_scenario(scenario: ScenarioSimulation | None = None) -> ResultatSimulation:
    """Calcule un scénario simple de simulation."""
    if scenario is None:
        scenario = ScenarioSimulation()

    configuration = SimulationConfig(
        horizon=scenario.horizon,
        taux_croissance=scenario.taux_croissance,
        seuil_reaction=scenario.seuil_reaction,
        valeur_initiale=scenario.valeur_initiale,
    )

    resultat = ResultatSimulation()
    valeur_courante = configuration.valeur_initiale

    for periode in range(configuration.horizon):
        variation = configuration.taux_croissance * valeur_courante
        if valeur_courante > configuration.seuil_reaction * 100:
            variation *= 0.9

        valeur_courante += variation
        resultat.ajouter(float(periode), float(valeur_courante))

    return resultat


def run_simulation() -> ResultatSimulation:
    """Lance une simulation avec un scénario de base."""
    scenario = ScenarioSimulation(nom="scenario_base")
    resultat = calculate_scenario(scenario)

    print(f"Scénario: {scenario.nom}")
    print(f"Valeur initiale: {scenario.valeur_initiale}")
    print(f"Taux de croissance: {scenario.taux_croissance}")
    print(f"Seuil de réaction: {scenario.seuil_reaction}")
    print(f"Nombre de points: {len(resultat.temps)}")
    print(f"Dernière valeur: {resultat.valeurs[-1]:.2f}")

    return resultat
