import time
import pyaudio
import keyboard
from pygame import mixer
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from observer.observers import Observer, SubjectObservers


class SongModel:
    def __init__(self, name, duration, keybind, path) -> None:
        self.name = name
        self.duration = duration
        self.keybind = keybind
        self.path = path
        self.bgimage_path = "view/build/assets/frame0/card/image_1.png"
        self.mode = 0

    def __str__(self) -> str:
        return f"{self.name}:{self.duration}:{self.keybind}:{self.path}:"


class MediaPlayerModel(Observer):
    def __init__(self, observable=None, dics_songs={}) -> None:
        self.subject = SubjectObservers()
        self.dic_songs = dics_songs
        self.observable = observable
        self.mode = 0
        mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

        keyboard.add_hotkey('ctrl + m', self.changeMode)
        # self.getAudioDevices(self)

    def playSong(self, songName: str):
        if songName in self.dic_songs and self.mode == 0:
            mixer.music.load(self.dic_songs[songName].path)
            mixer.music.set_volume(0.6)
            mixer.music.play()

    def pauseSong(self):
        mixer.music.pause()

    def resumeSong(self):
        mixer.music.unpause()

    def removeKeyBind(self, songName) -> bool:
        if self.dic_songs[songName].keybind:
            keyboard.remove_hotkey(self.dic_songs[songName].keybind)
            return True
        return False

    def deleteSong(self, songName):
        self.removeKeyBind(songName)
        self.dic_songs.pop(songName)
        self.observable.notifyAllObservers()

    def createKeyBind(self, key, function, songName):
        self.removeKeyBind(songName)

        self.dic_songs[songName].keybind = key.upper()
        keyboard.add_hotkey(key.upper(), function)
        self.subject.notifyAllObservers()

    def addMusic(self, path):
        songInfo = self.get_music_info(path)
        songModel = SongModel(songInfo[1], songInfo[0], "", path)
        self.dic_songs[songModel.name] = songModel

        self.observable.notifyAllObservers()

        return songModel

    # carregar os sons persisitidos no arquivo
    def loadSong(self, listSongModel):
        for songName in listSongModel:
            self.dic_songs[songName] = listSongModel[songName]
            if self.dic_songs[songName].keybind:
                keyboard.add_hotkey(
                    self.dic_songs[songName].keybind,
                    lambda songName=songName: self.playSong(
                        self.dic_songs[songName].name
                    ),
                )

        # Pause (p)
        keyboard.add_hotkey(
            "p",
            lambda songName=songName: self.pauseSong(),
        )

        # Resume(r))
        keyboard.add_hotkey(
            "r",
            lambda songName=songName: self.resumeSong(),
        )

    def get_dic_songs(self):
        return self.dic_songs

    def get_music_info(self, file_path: str):
        try:
            if file_path.lower().endswith(".mp3"):
                audio = MP3(file_path)
            elif file_path.lower().endswith(".wav"):
                audio = WAVE(file_path)
            else:
                # equivalente ao 'throw' do java
                raise ValueError("Formato de arquivo de áudio não suportado.")

            duration_in_seconds = audio.info.length
            title = file_path.split("/")

            return duration_in_seconds, title[-1]
        except Exception as e:
            print("Erro ao obter informações do arquivo de áudio:", str(e))
            return None, None

    def changeMode(self):
        self.mode = 0 if self.mode == 1 else 1

        path = (
            "assets\\button_on1.mp3" if self.mode == 0 else "assets\\button_off_1.wav"
        )

        mixer.music.load(path)
        mixer.music.set_volume(1.0)
        mixer.music.play()

        self.observable.notifyAllObservers(self.mode)

    def getMode(self):
        return self.mode

    def getAudioDevices(self, teste):
        # Inicialize o PyAudio
        pa = pyaudio.PyAudio()

        # Obtenha o número de dispositivos disponíveis
        num_devices = pa.get_device_count()
        print(f"Número de dispositivos disponíveis: {num_devices}")

        # Liste todos os dispositivos disponíveis
        for i in range(num_devices):
            device_info = pa.get_device_info_by_index(i)
            print(f"Dispositivo {i}: {device_info['name']}")

        # Encerre o PyAudio
        pa.terminate()

    def update(self, Mode=None):
        pass
