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

def test_create_music_list():
    txt_files_name = ['1 - Refrão Orante.txt']
    result = MusicList()._create_music_list(txt_files_name)

    title = '1 - Refrão Orante'
    content = 'Jesus, tu és a luz dos olhos meus\nJesus, brilhe esta luz nos passos meus seguindo os teus'
    expected = Music(title, content)

    assert len(result) > 0
    assert isinstance(result[0], Music)
    assert result[0] == expected

def test_create_music_list_null():
    result = MusicList()._create_music_list(None)

    assert result == []