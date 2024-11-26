from pptx import Presentation
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches
from pptx.dml.color import RGBColor
from src.slide_data import SlideData
from src.font_size_calculation import FontSizeCalculation

class SlideGenerator:
    def __init__(self, presentation, slide_layout, slide : SlideData):
        self.__presentation = presentation
        self.__slide_layout = slide_layout
        self.__slide = slide
        self.__slide_pptx = self.__presentation.slides.add_slide(self.__slide_layout)
        self.__title_shape = self.__slide_pptx.shapes.title
        self.__content_shape = self.get_content_shape()
        self.__font_size = Pt(self.__slide.FONT_SIZE)

        fsc = FontSizeCalculation()
        sfs = fsc.calcular_tamanho_fonte(slide.stanza)
        self.__stanza_font_size = Pt(sfs)

    def create_stanza_slide(self):
        self._set_slide_title()
        self._format_slide_title()
        self._set_slide_content()
        self._format_slide_content()

    def _set_slide_title(self):
        self.__title_shape.text = self.__slide.title

    def _format_slide_title(self):
        title_font = self.__title_shape.text_frame.paragraphs[0].font
        title_font.bold = True
        title_font.size = self.__font_size

    def _set_slide_content(self):
        self.__content_shape.text = self.__slide.stanza

    def get_content_shape(self):
        return self.__slide_pptx.placeholders[1]

    def _format_slide_content(self):
        text_frame = self.__content_shape.text_frame
        for p in text_frame.paragraphs:
            p.font.size = self.__stanza_font_size
            p.level = 0 # Define o nível da lista (0 para nível superior)
            p.alignment = PP_ALIGN.CENTER
            p.font.color.rgb = RGBColor(0, 0, 0)

            # Remover os marcadores ou números
            p.bullet = None  # Remove marcadores ou números
            p.bullet_style = None  # Adicionalmente, tente remover o estilo de marcador (para números ou marcadores)