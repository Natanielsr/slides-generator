from typing import List
from pptx import Presentation
from src.music import Music
from src.slide_generator import SlideGenerator
from src.slide_data import SlideData

class PresentationGenerator:

    def __init__(self, musics: List[Music], font_size: int): 
        if not isinstance(font_size, int) or font_size <= 0:
            raise ValueError("font_size must be a positive integer")
        if not all(isinstance(music, Music) for music in musics):
            raise TypeError("musics parameter must be a list of Music objects")
        self.__FONT_SIZE = font_size     
        self.__musics = musics  
        self.__presentation = Presentation()
        self.__slide_layout = self.__presentation.slide_layouts[1]

    def generate_presentation_slides(self):
        print("Generating presentation slides...")
        for music in self.__musics:
            self._generate_music_slides(music)
            self.add_blank_slide()

        print("Presentation Slides generated with Success!")
        return self.__presentation
    
    def add_blank_slide(self):
        self.__presentation.slides.add_slide(self.__presentation.slide_layouts[0])

    def save_presentation_file(self, file_name="slides.pptx"):
        print("Saving file...")
        self.__presentation.save(file_name)
        print("Presentation file "+file_name+" saved with Success!")

    def _generate_music_slides(self, music : Music):
        try:
            stanzas = self._separate_stanzas(music.lyrics)
            for stanza in stanzas:
                slide = SlideData(
                    self.__FONT_SIZE,
                    music.title,
                    stanza)
            
                slideGen = SlideGenerator(self.__presentation, self.__slide_layout, slide)
                slideGen.create_stanza_slide()
        except Exception as e:
            print(f"Error generating slides for music {music.title}: {str(e)}")

    def _separate_stanzas(self, lyric):
        return lyric.strip().split('\n\n')
    
    
    



    
    
    
    