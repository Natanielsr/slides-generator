from pptx import Presentation
from src.music import Music
from src.slides_generator import SlidesGenerator

class PresentationGenerator:

    def __init__(self, musics : Music):      
        self.__musics = musics  
        self.__presentation = Presentation()
        self.__slide_layout = self.__presentation.slide_layouts[1]

    def generate_presentation_slides(self):
        print("Generating presentation slides...")
        for music in self.__musics:
            self._generate_music_slides(music)

        print("Presentation Slides generated with Success!")

        return self.__presentation
        

    def save_presentation_file(self, file_name = "slides.pptx"):
        print("Saving file...")
        self.__presentation.save(file_name)
        print("Presentation file "+file_name+" saved with Success!")
        

    def _generate_music_slides(self, music):
        stanzas = self._separate_stanzas(music.lyrics)
        for stanza in stanzas:
            SlidesGenerator(
                self.__presentation,
                self.__slide_layout
                ).create_stanza_slide(music.title, stanza)
    
    def _separate_stanzas(self, lyric):
        return lyric.strip().split('\n\n')
    
    



    
    
    
    