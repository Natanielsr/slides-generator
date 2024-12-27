from src.music_list import MusicList
from src.presentation_generator import PresentationGenerator

FONT_SIZE = 42

if __name__ == "__main__":

    musics = MusicList().get_music_list()

    insert_title : bool = False
    
    slideGen = PresentationGenerator(musics, FONT_SIZE, insert_title)
    slideGen.generate_presentation_slides()
    slideGen.save_presentation_file()