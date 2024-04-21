import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
import main_window
import settings_window
import moviepy.editor as mp




class settings_ui(QMainWindow):
    path = ""
    def __init__(self):
        super(settings_ui, self).__init__()
        self.ui = settings_window.Ui_SettingsWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_pathselection.clicked.connect(self.get_path)
        

    # путь для сохранения выгрузки (настройки)
    def get_path(self):
        path = QFileDialog.getExistingDirectory(self, "Выберите путь")
        print(path)



class ui(QMainWindow):
    global path
    path = ""

    def __init__(self):
        super(ui, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_upload.clicked.connect(self.upload_file)
        self.ui.pushButton_start.clicked.connect(self.start)
        self.w = None
        self.ui.menu_2.triggered.connect(self.open_settings)
        self.ui.select_path_menu.triggered.connect(self.open_settings)

    def open_settings(self):
        print(path)
        if self.w is None:
            self.w = settings_ui()
            self.w.show()
        else:
            self.w.close()
            self.w = None 

    # загрузка файла по нажатию на кнопку "Выбрать файл"
    def upload_file(self):
        global file
        file = QFileDialog.getOpenFileName(self, "Выберите файл", "./")
        self.ui.label_filename_field.setText(str(os.path.basename(file[0])))

    # запуск транскриб по нажатию на кнопку "Запустить"
    def start(self):
        if (os.path.exists(file[0]) and os.path.isfile(file[0])):
            # запуск всего
            if (self.ui.checkBox_transcript.isChecked() and self.ui.checkBox_bulletpoint.isChecked()):
                # self.ui.label_filename_field.setText("транскриб + буллет")
                print(path)
                self.file_convert()
            # запуск только транскрибации
            elif (self.ui.checkBox_transcript.isChecked()):
                self.ui.label_filename_field.setText("транскриб")
            # запуск только буллетпоинтов
            elif (self.ui.checkBox_bulletpoint.isChecked()):
                self.ui.label_filename_field.setText("буллет")
        

    # конвертация видеофайла в аудио
    def file_convert(self, out_ext = "wav"):
        filename, ext = os.path.splitext(file[0])
        if (ext != "wav"):
            clip = mp.VideoFileClip(file[0])
            clip.audio.write_audiofile(f"{filename}.{out_ext}") # type: ignore
            os.rename(filename + '.' + out_ext, path + os.path.basename(filename) + ".wav")


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = ui()
    window.show()
    sys.exit(app.exec())