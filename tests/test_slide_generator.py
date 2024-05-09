import pytest
from src.presentation_generator import PresentationGenerator

def test_create_music():
    lyric = "stanza1\n\nstanza2"
    result = PresentationGenerator([])._separate_stanzas(lyric)

    expected = ["stanza1","stanza2"]

    assert expected == result

