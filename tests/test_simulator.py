"""Tests de base pour le simulateur."""

from simulateur_bvmac.simulator import calculate_scenario
from simulateur_bvmac.models import ScenarioSimulation


def test_calcul_scenario_produit_des_resultats():
    scenario = ScenarioSimulation(horizon=5, valeur_initiale=100.0, taux_croissance=0.02, seuil_reaction=0.5)
    resultat = calculate_scenario(scenario)

    assert len(resultat.temps) == 5
    assert len(resultat.valeurs) == 5
    assert resultat.valeurs[0] > 100.0
    assert resultat.valeurs[-1] > resultat.valeurs[0]
