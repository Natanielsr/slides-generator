from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from src.slide_data import SlideData
class SlideGenerator:
    def __init__(self, presentation, slide_layout, slide : SlideData):   
        self.__presentation = presentation
        self.__slide_layout = slide_layout
        self.__slide = slide
        self.__slide_pptx = self._add_slide_with_layout()
        
    def create_stanza_slide(self):
        self._set_slide_title()
        self._format_slide_title()

        self._set_slide_content()
        self._format_slide_content()
    
    
    def _add_slide_with_layout(self):
        return self.__presentation.slides.add_slide(self.__slide_layout)
    
    def _set_slide_title(self):
        # Adicionando texto ao título do slide
        title_shape = self.__slide_pptx.shapes.title
        title_shape.text = self.__slide.title
    
    def _format_slide_title(self):
        title_shape = self.__slide_pptx.shapes.title
        title_font = title_shape.text_frame.paragraphs[0].font
        title_font.bold = True
        title_font.size = Pt(self.__slide.FONT_SIZE)

    def _set_slide_content(self):
        # Adicionando texto ao corpo do slide
        content_shape = self.get_content_shape()
        content_shape.text = self.__slide.stanza
        
    def get_content_shape(self):
        return self.__slide_pptx.placeholders[1]
    
    def _format_slide_content(self):
        content_shape = self.get_content_shape()
        text_frame = content_shape.text_frame
        for p in text_frame.paragraphs:
            p.font.size = Pt(self.__slide.FONT_SIZE)
            p.level = 0  # Define o nível de lista como 0
            p.alignment = PP_ALIGN.CENTER  # Alinha o texto ao centro
            p.font.color.rgb = RGBColor(0, 0, 0)  # Define a cor do texto como preto