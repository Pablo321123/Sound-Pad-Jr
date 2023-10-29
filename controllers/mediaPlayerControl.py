import time
from pygame import mixer
from model.mediaPlayerModel import SongModel
from tkinter import filedialog


class MediaPlayerControl:
    def __init__(self, view, model, fileControl) -> None:
        self.view = view
        self.model = model
        self.fileControl = fileControl

    def play(self, songName):
        self.model.playSong(songName)
        # self.model.playSong("audio/o-sonho-do-Hexa-está-adiado.wav")
        # self.model.createKeyBind(
        #     "k", lambda: self.model.playSong("audio/o-sonho-do-Hexa-está-adiado.wav")
        # )

    def pause(self):
        self.model.pauseSong()

    def resume(self):
        self.model.resumeSong()

    def deleteSong(self, songName):
        self.model.deleteSong(songName)

    def createKeyBind(self, key, songName):
        self.model.createKeyBind(key, lambda: self.model.playSong(songName), songName)

    def open_choose_file_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Selecione uma música",
            filetypes=(
                ("Arquivos de Música", "*.mp3;*.wav"),
                ("Todos os arquivos", "*.*"),
            ),
        )
        return file_path

    def addMusic(self):
        path = self.open_choose_file_dialog()

        if path:
            songModel = [self.model.addMusic(path)]
        else:
            print("Caminho inválido")
        # self.model.createKeyBind(
        #     songModel[0].keybind, lambda: self.model.playSong(songModel.name)
        # )

    """1 - Carrega os dados persistidos no arquivo de texto"""
    """2 - Retorna as musicas ja carregadas no sistema"""

    def loadSong(self, listSongModel=None):
        if listSongModel:
            self.model.loadSong(listSongModel)
        else:
            return self.model.get_dic_songs()

    # persisitir sons já adicionados
    def persistAddedSongs(self):
        self.fileControl.saveInFile(self.model.get_dic_songs())

    def changeMode(self):
        """Mode 0: Song"""
        """ Mode 1: Txt  """

        self.model.changeMode()

    def getMode(self):
        return self.model.getMode()
