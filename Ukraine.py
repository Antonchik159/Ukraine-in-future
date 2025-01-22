#Імпорт усіх необхідних модулів
import subprocess
import json
import sys
import os
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QStackedWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtGui import QPixmap, QImage
import webbrowser
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimedia import QSoundEffect
from ui import Ui_My_App
from mainw import Ui_Main_page
from settings import Ui_Setting
from notes import Ui_Note
from dialog import Ui_Dialog
from dishes import Ui_Dish_Window
from loader import Ui_MainWindow
from instagram import Ui_Instagram
from film_pars import main
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
        self.progress_value += 2
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
        self.ui.bn_film.clicked.connect(self.open_flm)
        self.ui.btn_film_info.clicked.connect(self.open_film_inform)
        self.ui.inst_btn.clicked.connect(self.open_inst)
        self.setting = setting
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

    def open_flm(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        main()
        flm.show()


    def open_inst(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        inst.show()

    def open_film_inform(self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        file_path = 'document/film_information.txt'
        with open(file_path, 'r', encoding='utf-8') as file:
                # Зчитування файлу
                contents = file.read()
                message_box = QMessageBox()
                message_box.setWindowIcon(QIcon('image/message.png'))
                message_box.setWindowTitle('Помічник')
                message_box.setText(contents)
                message_box.exec()

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
        self.ui.pushButton.clicked.connect(lambda: self.del_note(self.ui.notes_listwidget.currentItem()))
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

    def del_note(self, item):
        current_title = item.text()
        file_name = f"notes_save/{current_title}.txt"

        for i, (title, _) in enumerate(self.notes):
            print("Порівнюємо з:", title)
            if title == current_title:
                if os.path.exists(file_name):
                    os.remove(file_name)
                    self.notes.pop(i)
                    print("Замітка видалена.")
                    self.ui.notes_listwidget.takeItem(i)
                    break

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
       self.ui.pushButton_2.clicked.connect(self.default)
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

    def default (self):
        if self.setting.sound_enabled:
            self.sound_effect.play()
        self.ui.checkBox.setChecked(False)
        self.ui.horizontalSlider.setValue(100)
        self.hide()
        QApplication.quit()
        python = sys.executable
        subprocess.call([python] + sys.argv)
            
        

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

class Instagram(QMainWindow):
    def __init__(self, setting):
       super().__init__()
       self.ui = Ui_Instagram()
       self.ui.setupUi(self)
       self.hide()
       self.setting = setting
       self.sound_effect = QSoundEffect()
       self.sound_effect.setSource(QUrl.fromLocalFile('sound/click.wav'))

class Films(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Фільми')
        self.setGeometry(100, 100, 500, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.addWidget(self.stacked_widget)
        self.central_widget.setLayout(self.central_layout)

        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.image_download_finished)

        self.image_requests = {}

        self.create_pages()
        self.current_page = 0 

        self.forward_button = QPushButton('Вперед')
        self.forward_button.clicked.connect(self.next_page)

        self.backward_button = QPushButton('Назад')
        self.backward_button.clicked.connect(self.previous_page)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.backward_button)
        button_layout.addWidget(self.forward_button)
        self.central_layout.addLayout(button_layout)

        self.update_buttons()


    def create_pages(self):
        with open('film.json', encoding="utf-8") as json_file:
            data = json.load(json_file)

        new_data = {"pages": [data]}

        with open('new_film.json', 'w', encoding="utf-8") as new_json_file:
            json.dump(new_data, new_json_file, ensure_ascii=False, indent=4)

        with open('new_film.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            self.pages = data['pages']

        cards_per_page = 9
        num_pages = len(self.pages[0]) // cards_per_page
        if len(self.pages[0]) % cards_per_page != 0:
            num_pages += 1

        self.loaded_data = []
        for page_num in range(num_pages):
            page_widget = QWidget()
            page_layout = QVBoxLayout()

            grid_layout = QGridLayout()

            start_index = page_num * cards_per_page
            end_index = start_index + cards_per_page
            page = self.pages[0][start_index:end_index]

            for index in range(len(page)):
                self.loaded_data.append(page[index])

            for row in range(3):
                for col in range(3):
                    index = row * 3 + col
                    if index < len(page):
                        item = page[index]

                        card_widget = QWidget()
                        card_layout = QVBoxLayout()

                        img_url = item['img']
                        image_label = QLabel()
                        image_label.setAlignment(Qt.AlignCenter)
                        image_label.setScaledContents(True)
                        image_label.setFixedSize(150, 200)
                        self.load_image(img_url, image_label)

                        description_label = QLabel(item['product_name'])
                        description_label.setAlignment(Qt.AlignCenter)
                        description_label.setStyleSheet('font-size: 16px; font-weight: bold;')
                        description_label.setWordWrap(True)
                        description_label.setFixedWidth(200)
                        description_label.setTextFormat(Qt.RichText)
                        description_label.setText(f'<p style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{item["product_name"]}</p>')

                        link_button = QPushButton('Дивитись')
                        link_button.setProperty("index", index)
                        link_button.setStyleSheet('background-color: #3498db; color: white; border: none; padding: 5px 10px;')
                        link_button.clicked.connect(self.open_link)

                        card_layout.addWidget(image_label)
                        card_layout.addWidget(description_label)
                        card_layout.addWidget(link_button)

                        card_widget.setLayout(card_layout)

                        grid_layout.addWidget(card_widget, row, col)

            page_layout.addLayout(grid_layout)
            page_widget.setLayout(page_layout)

            self.stacked_widget.addWidget(page_widget)

    def load_image(self, url, image_label):
        request = QNetworkRequest(QUrl(url))
        self.network_manager.get(request)

        self.image_requests[image_label] = request

    def image_download_finished(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            image = QImage.fromData(data)
            pixmap = QPixmap.fromImage(image)
            image_request = reply.request()
            image_label = None

            for label, request in self.image_requests.items():
                if request == image_request:
                    image_label = label
                    break

            if image_label is not None:
                image_label.setPixmap(pixmap)
        else:
            print("Error loading image:", reply.error(), reply.errorString())

    def open_link(self):
        current_index = self.stacked_widget.currentIndex()
        current_data = self.loaded_data[current_index * 9:]

        button = self.sender()
        index = button.property("index")

        if 0 <= index < len(current_data):
            product_link = current_data[index]['product_link']
            webbrowser.open(product_link)

    def next_page(self):
        if self.current_page < self.stacked_widget.count() - 1:
            self.current_page += 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_buttons()

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.stacked_widget.setCurrentIndex(self.current_page)
            self.update_buttons()

    def update_buttons(self):
        self.forward_button.setEnabled(self.current_page < self.stacked_widget.count() - 1)
        self.backward_button.setEnabled(self.current_page > 0)

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
    flm = Films()
    inst = Instagram(setting)
    apply_settings_from_json(ex, 'data/opacity.json')
    apply_settings_from_json(mpg, 'data/opacity.json')
    apply_settings_from_json(mds, 'data/opacity.json')
    apply_settings_from_json(dlg, 'data/opacity.json')
    apply_settings_from_json(stt, 'data/opacity.json')
    apply_settings_from_json(nte, 'data/opacity.json')
    sys.exit(app.exec_())