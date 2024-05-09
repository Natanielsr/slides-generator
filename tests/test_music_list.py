import pytest
from src.music_list import MusicList
from src.music import Music
from src.utils.format import Format

def test_remove_ext():
    file_name = '1 - Refrão Orante.txt'
    result = Format.remove_ext_name(file_name)

    expected = '1 - Refrão Orante'

    assert expected == result

def test_create_music():
    expected = Music('title', 'content')
    result = MusicList()._create_music('title', 'content')

    assert expected == result