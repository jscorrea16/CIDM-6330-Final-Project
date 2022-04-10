from re import M
import pytest

from pestslib.pests import DiagnosticTesting, Pest, PestObservation, Illness


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


def test_can_create_illness():
    # arrange
    # act
    illness = Illness("West Nile Virus")
    # asset
    assert str(illness) == "West Nile Virus"


def test_can_create_diagnostic_testing():
    # arrange
    # act
    diagnostictesting = DiagnosticTesting(
        "Cerebrospinal fluid", "Immunoglobulin Mu", "Positive", "3/25/2022")
    # assert
    assert str(
        diagnostictesting) == "Cerebrospinal fluid - Immunoglobulin Mu - Positive - 3/25/2022"
