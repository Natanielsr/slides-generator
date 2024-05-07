import pytest
from src.file_reader import FileReader
from src.music import Music


# test_somador.py
def test_files_name():
    expected_list = [
        '1 - Refrão Orante.txt',
        '2 - Canto de Abertura.txt',
        '3 - Ato Penitencial.txt',
        '4 - Hino de Louvor.txt',
        '5 - Primeira Leitura.txt',
        '6 - Salmo.txt',
        '7 - Aclamação ao Evangelho.txt',
        '8 - Ofertório.txt',
        '9 - Santo.txt',
        '10 - Cordeiro de Deus.txt',
        '11 - Comunhão.txt',
        '12 - Final.txt'
    ]

    actual_list = FileReader().get_files_name()

    # Verificar se são iguais
    assert actual_list == expected_list, f"A lista retornada é diferente do esperado: {actual_list}"


def test_read_file():
    expected = "Jesus, tu és a luz dos olhos meus\nJesus, brilhe esta luz nos passos meus seguindo os teus"

    content = FileReader().read_file('1 - Refrão Orante.txt')

    assert expected == content

def test_remove_ext():
    file_name = '1 - Refrão Orante.txt'
    result = FileReader().remove_ext_name(file_name)

    expected = '1 - Refrão Orante'

    assert expected == result

def test_create_music():
    expected = Music('title', 'content')
    result = FileReader()._create_music('title', 'content')

    assert expected == result