import pytest

from pestslib.pests import Pest, PestObservation, MaladyType, ImpactObservation


def test_can_create_pest():
    # arrange
    # act
    pest = Pest("Culex", "pipiens")

    # assert
    assert str(pest) == "Culex - pipiens"


def test_can_create_pest_observation():
    # arrange
    # act    
    pestobservation = PestObservation("Amarillo", "Randall", "3/22/2022")
    # assert
    assert str(pestobservation) == "Amarillo - Randall - 3/22/2022"
