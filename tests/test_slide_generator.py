import pytest
import os
from src.presentation_generator import PresentationGenerator
from src.music import Music

FONT_SIZE = 42
def test_create_music():
    lyric = "stanza1\n\nstanza2"
    result = PresentationGenerator([], FONT_SIZE)._separate_stanzas(lyric)

    expected = ["stanza1","stanza2"]

    assert expected == result

def test_create_presentation():
    music = Music("title", "content")
    musics = [music]
    prsGen = PresentationGenerator(musics, FONT_SIZE)
    presentation = prsGen.generate_presentation_slides()

    slide = presentation.slides[0]
    assert slide.shapes.title.text == "title"
    assert slide.placeholders[1].text == "content"

    file_name = "test.pptx"
    prsGen.save_presentation_file(file_name)

    assert os.path.exists(file_name)
    
    os.remove(file_name)


