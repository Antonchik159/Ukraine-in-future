#Імпорт усіх необхідних модулів
import subprocess
import json
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
from ui import Ui_My_App
from mainw import Ui_Main_page
from settings import Ui_Setting
from notes import Ui_Note
from dialog import Ui_Dialog
from dishes import Ui_Dish_Window
from loader import Ui_MainWindow
# Оголошення класу Loader, що наслідується від QMainWindow
class Loader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.timer = QTimer(self)
        self.timer.start(100)
        self.progress_value = 0
        self.timer.timeout.connect(self.update_progress)
        self.show()

    def update_progress(self):
        self.progress_value += 1
        self.ui.progressBar.setValue(self.progress_value)
        if self.progress_value >= 100:
            self.timer.stop()
            self.hide()
            ex.show()

#Оголошення класу Widget, який наслідується від QMainWindow
class Widget(QMainWindow):
    def __init__(self, setting):
        super().__init__()
        self.ui = Ui_My_App()
        self.ui.setupUi(self)
        self.ui.inform.clicked.connect(self.read_inform)
        self.ui.pushButton.clicked.connect(self.open_main_page)
        self.setting = setting
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))
    
    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def read_inform(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        # Відкриття файлу в режимі читання
        file_path = 'document/information.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
                # Зчитування файлу
                contents = file.read()
                message_box = QMessageBox()
                message_box.setWindowTitle('Інформація')
                message_box.setWindowIcon(QIcon('image/message.png'))
                message_box.setText(contents)
                message_box.exec()
    
    def open_main_page (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        mpg.show()
#Оголошення класу Main_window, який наслідується від QMainWindow
class Main_window(QMainWindow):
    def __init__(self, setting): 
        super().__init__()
        self.ui = Ui_Main_page()
        self.ui.setupUi(self)
        self.hide()
        self.ui.leave.clicked.connect(self.exit)
        self.ui.pushButton.clicked.connect(self.open_setting)
        self.ui.btn_note.clicked.connect(self.open_note)
        self.ui.note_inf.clicked.connect(self.open_note_inform)
        self.ui.book_inf.clicked.connect(self.open_reference_inform)
        self.ui.btn_book.clicked.connect(self.open_dialog)
        self.ui.dishes_btn.clicked.connect(self.open_menu_dish)
        self.ui.dishes_inf_btn.clicked.connect(self.open_dish_inform)
        self.setting = setting
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def open_note (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        nte.show()

    def open_menu_dish (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        mds.show()

    def exit (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        ex.show()

    def open_setting (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        stt.show()

    def open_dialog (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        dlg.show()

    def open_note_inform (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        file_path = 'document/note_information.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
                # Зчитування файлу
                contents = file.read()
                message_box = QMessageBox()
                message_box.setWindowIcon(QIcon('image/message.png'))
                message_box.setWindowTitle('Помічник')
                message_box.setText(contents)
                message_box.exec()

    def open_reference_inform (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        file_path = 'document/reference_book_inform.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
                # Зчитування файлу
                contents = file.read()
                message_box = QMessageBox()
                message_box.setWindowIcon(QIcon('image/message.png'))
                message_box.setWindowTitle('Помічник')
                message_box.setText(contents)
                message_box.exec()

    def open_dish_inform (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        file_path = 'document/dish_information.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
                # Зчитування файлу
                contents = file.read()
                message_box = QMessageBox()
                message_box.setWindowIcon(QIcon('image/message.png'))
                message_box.setWindowTitle('Помічник')
                message_box.setText(contents)
                message_box.exec()
#Оголошення класу Notes, який наслідується від QMainWindow
class Notes(QMainWindow):
    def __init__(self, setting): 
        super().__init__()
        self.ui = Ui_Note()
        self.ui.setupUi(self)
        self.ui.add_button.clicked.connect(self.add_note)
        self.ui.notes_listwidget.itemDoubleClicked.connect(self.edit_note)
        self.notes = []
        self.load_notes()
        self.hide()
        self.setting = setting
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def add_note(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        title = self.ui.title_edit.text()
        note = self.ui.notes_textedit.toPlainText()
        if title and note:
            self.notes.append((title, note))
            self.ui.notes_listwidget.addItem(title)
            self.clear_inputs()
            self.save_notes(title, note)

    def edit_note(self, item):
        current_title = item.text()
        for i, (title, note) in enumerate(self.notes):
            if title == current_title:
                self.ui.title_edit.setText(title)
                self.ui.notes_textedit.setPlainText(note)
                self.ui.notes_listwidget.takeItem(i)
                break

    def save_notes(self, title, note):
        file_name = f"notes_save/{title}.txt"
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(note)
        except Exception as e:
            print(f"Помилка при збереженні нотатки '{title}': {str(e)}")

    def load_notes(self):
        import glob
        file_list = glob.glob("notes_save/*.txt")
        for file_name in file_list:
            try:
                title = file_name[len("notes_save/"):-4]
                with open(file_name, "r", encoding="utf-8") as file:
                    note = file.read()
                    self.notes.append((title, note))
                    self.ui.notes_listwidget.addItem(title)
            except Exception as e:
                print(f"Помилка при завантаженні нотатки '{file_name}': {str(e)}")

    def clear_inputs(self):
        self.ui.title_edit.clear()
        self.ui.notes_textedit.clear()

    def closeEvent(self, event):
        for title, note in self.notes:
            self.save_notes(title, note)
        event.accept()
#Оголошення класу Settings, який наслідується від QMainWindow
class Settings (QMainWindow):
    def __init__(self, setting):
       super().__init__()

       self.ui = Ui_Setting()
       self.ui.setupUi(self)
       self.hide()
       self.ui.pushButton.clicked.connect(self.go_main)
       self.ui.horizontalSlider.valueChanged.connect(self.set_opacity)
       self.ui.save.clicked.connect(self.restart_program)
       self.subwindows = []
       self.setting = setting
       self.ui.checkBox.setChecked(setting.sound_enabled)
       self.ui.checkBox.stateChanged.connect(self.toggle_sound)
       self.sound_effect = QSoundEffect()
       self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

    def toggle_sound(self, state):
        self.setting.sound_enabled = state == Qt.Checked
        self.setting.save_to_json('data/settings.json')

    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def restart_program(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        QApplication.quit()
        python = sys.executable
        subprocess.call([python] + sys.argv)

    def set_opacity(self, value):
        opacity = value / 100
        self.setWindowOpacity(opacity)
        self.save_opacity_to_json(opacity)

    def go_main (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        mpg.show()

    def save_opacity_to_json(self, opacity):
        opacity_data = {"opacity": opacity}

        with open("data/opacity.json", "w") as file:
            json.dump(opacity_data, file)
#Оголошення класу Dialog, який наслідується від QMainWindow
class Dialog (QMainWindow):
    def __init__(self, setting):
       super().__init__()
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.hide()
       self.ui.exit.clicked.connect(self.exit_main)
       self.setting = setting
       self.sound_effect = QSoundEffect()
       self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))
    
    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def exit_main (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        mpg.show()
#Оголошення класу Menu, який наслідується від QMainWindow
class Menu (QMainWindow):
    def __init__(self, setting):
       super().__init__()
       self.ui = Ui_Dish_Window()
       self.ui.setupUi(self)
       self.hide()
       self.ui.exit_btn.clicked.connect(self.exit_m)
       self.setting = setting
       self.sound_effect = QSoundEffect()
       self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

    def apply_settings(self, settings):
        # Застосування налаштувань до вікна
        if 'opacity' in settings:
            self.setWindowOpacity(settings['opacity'])

    def exit_m (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.hide()
        mpg.show()

class Setting:
    def __init__(self):
        self.sound_enabled = False

    def load_from_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        self.sound_enabled = data.get('sound_enabled', False)

    def save_to_json(self, filename):
        data = {
            'sound_enabled': self.sound_enabled
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

def apply_settings_from_json(ex, json_file):
    with open(json_file, 'r') as file:
        settings = json.load(file)

    ex.apply_settings(settings)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('image/icon.png'))
    ldr = Loader()
    ldr.show()
    setting = Setting()
    setting.load_from_json('data/settings.json')
    ex = Widget(setting)
    mpg = Main_window(setting)
    mds = Menu(setting)
    dlg = Dialog(setting)
    nte = Notes(setting)
    stt = Settings(setting)
    apply_settings_from_json(ex, 'data/opacity.json')
    apply_settings_from_json(mpg, 'data/opacity.json')
    apply_settings_from_json(mds, 'data/opacity.json')
    apply_settings_from_json(dlg, 'data/opacity.json')
    apply_settings_from_json(stt, 'data/opacity.json')
    apply_settings_from_json(nte, 'data/opacity.json')
    sys.exit(app.exec_())