from controllers.mediaPlayerControl import MediaPlayerControl
from model.mediaPlayerModel import MediaPlayerModel
from view.build.main_view import MainView
from util.editFile import EditFile
from observer.observers import SubjectObservers

if __name__ == "__main__":
    observable = SubjectObservers()

    mv = MainView()
    observable.addObserver(mv)
    mpm = MediaPlayerModel(observable)
    fileControl = EditFile("sons_sound_pad_jr.txt")
    mpc = MediaPlayerControl(mv, mpm, fileControl)

    try:
        mv.startApp(mpc, fileControl)
    except Exception as e:
        with open("log_sound_pad_jr.txt", "w") as file:
            file.write(e.__str__())
