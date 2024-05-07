from src.music_list import MusicList
from src.slide_generator import SlideGenerator


if __name__ == "__main__":

    musics = MusicList().create_music_list()
    
    slideGen = SlideGenerator(musics)
    slideGen.generate_presentation_file()

    
    
