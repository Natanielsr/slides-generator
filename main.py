from src.music_list import MusicList
from src.presentation_generator import PresentationGenerator


if __name__ == "__main__":

    musics = MusicList().create_music_list()
    
    slideGen = PresentationGenerator(musics)
    slideGen.generate_presentation_slides()
    slideGen.save_presentation_file()

    
    
