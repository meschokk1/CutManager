from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel,QFileDialog
from PyQt5 import uic
import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        # Загружаем ui файл с интерфейсом
        uic.loadUi('dialog.ui',self)

        # Описываем виджеты
        self.setWindowTitle('CutManager v_0.1')
        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')
        self.button_2 = self.findChild(QPushButton, 'pushButton_2')
        self.label = self.findChild(QLabel, 'label_2')
        self.label_2.resize(600,400)
        self.label_3 = self.findChild(QLabel, 'label_3')
        self.label_3.setStyleSheet('color: rgb(0, 255, 0);')
        # Описываем, что произойдет при нажатии
        self.button.clicked.connect(self.clicker)
        self.button_2.clicked.connect(self.crop_image)
    def set_of_files(self):
        list_of_files = '\n'.join(str(value) for value in filenames[0])
        return list_of_files
    def clicker(self):
        # self.label_2.setText('Файлы выбраны')
        # Открыть файловый диалог
        global filenames
        filenames = QFileDialog.getOpenFileNames(self, 'Выберите изображение', "c:", "All Files (*);;BMP(*.bmp);;PNG(*.png);;JPG(*.jpg)")
       # Вывод выбранных файлов на экран
        if filenames:
            list_of_files = '\n'.join(str(value) for value in filenames[0])
            self.label_2.setText('Выбранные файлы:\n'+list_of_files)

    def crop_image(self):
        for file in filenames[0]:
            im = Image.open(file)  # Путь к картинке
            img_width, img_height = im.size
            im_new = im.crop((1,1,img_width-1,img_height-1))
            im_new.save(file, quality = 100)
        self.label_3.setText('Файлы обработаны')

app = QApplication(sys.argv)
UIWindow = UI()
UIWindow.show()
sys.exit(app.exec_())