from src.music import Music
from src.file_reader import FileReader
from src.utils.format import Format
class MusicList:

    def __init__(self):
        self.__file_reader = FileReader()
        self._txt_files_name = self.__file_reader.get_files_name()
        
    def get_music_list(self):
        return self._create_music_list()

    def _create_music_list(self):
        musics = []

        if(self._txt_files_name is None):
            return musics
        
        for file_name in self._txt_files_name:   
            title = Format.remove_ext_name(file_name)
            content = self.__file_reader.read_content_file(file_name)      
            music = self._create_music(title, content)
            musics.append(music)

        return musics
    
    
    def _create_music(self, title, content):
        return Music(title, content)