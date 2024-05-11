from src.music_list import MusicList
from src.presentation_generator import PresentationGenerator

FONT_SIZE = 42

if __name__ == "__main__":

    musics = MusicList().create_music_list()
    
    slideGen = PresentationGenerator(musics, FONT_SIZE)
    slideGen.generate_presentation_slides()
    slideGen.save_presentation_file()

    
    
