from src.music import Music
from src.file_reader import FileReader
from src.utils.format import Format
class MusicList:

    def __init__(self):
        self.__file_reader = FileReader()
        
    def get_music_list(self):
        txt_files_name = self.__file_reader.get_files_name()
        return self._create_music_list(txt_files_name)

    def _create_music_list(self, txt_files_name):
        musics = []
        
        for file_name in txt_files_name:   
            title = Format.remove_ext_name(file_name)
            content = self.__file_reader.read_content_file(file_name)      
            music = self._create_music(title, content)
            musics.append(music)

        return musics
    
    
    def _create_music(self, title, content):
        return Music(title, content)