from os import stat
import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QAbstractButton, QApplication, QFileDialog, QLabel, QLineEdit, QMessageBox, QRadioButton,QWidget,QPushButton
from PySide6.QtGui import QActionEvent, QCloseEvent, QCursor, QFont, QIcon

from core.yt_download import DownloadYT


class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
    
    def setup(self):
        w = 400
        h = 500

        x = (1366 /2) - (w/2)
        y = (768 /2) - ((h/2)-40)

        self.setGeometry(x,y,w,h)
        self.setMaximumSize(w,h)
        self.setMinimumSize(w,h)

        self.setWindowTitle(" Minha primeira aplicação")
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('assets\ico.ico')))

        self.setAutoFillBackground(True)
        self.setStyleSheet('background-color: #fff')

        self.set_img()
        self.label_principal()
        self.url_vid()
        self.select_resolution()
        self.button_download()

        self.show()
    
    def closeEvent(self, event: QCloseEvent):
        reply =  QMessageBox.question(
            self,
            'Message',
            'Deseja fechar o programa?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        """box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle('Feixar programa')
        box.setText('Deseja feixar o programa?')
        box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        buttonY = box.button(QMessageBox.Yes)
        buttonY.setText('Sim')
        buttonN = box.button(QMessageBox.No)
        buttonN.setText('Não')
        box.exec_()

        if box.clickedButton() == buttonY:
            event.accept()
        elif box.clickedButton() == buttonN:
            event.ignore()"""
        
    def set_img(self):
        img = QIcon('assets/video.png')
        lb_img = QLabel('Palavra',self)
        lb_img.move(67,56)
        red_img = img.pixmap(60,60,QIcon.Active)

        lb_img.setPixmap(red_img)
    
    def label_principal(self):
        lb_YT = QLabel('YouTube',self)
        lb_YT.move(137,45)
        lb_YT.setStyleSheet('font-size: 48px; color: #E28086;font-weight:bold')
        lb_YT.setFont(QFont('fonts\CircularStd-Bold.otf'))

        sub_lb_YT = QLabel('download...',self)
        sub_lb_YT.move(149,98)
        sub_lb_YT.setStyleSheet('font-size: 20px; color: #494343;font-style:book')
        sub_lb_YT.setFont(QFont('fonts\CircularStd-Book.otf').setBold(True))
    
    def url_vid(self):
        font_lb = QFont('fonts\CircularStd-Book.otf')
        font_lb.setPointSize(14)

        lb_camp = QLabel('url:',self)
        lb_camp.move(55,174)
        lb_camp.setStyleSheet('color: #888080;font-style:300')
        lb_camp.setFont(font_lb)

        font_camp = QFont('fonts\CircularStd-Book.otf')
        font_camp.setPointSize(11)

        self.camp_url = QLineEdit(self)
        self.camp_url.setGeometry(41,203,318,35)
        self.camp_url.setFont(font_camp)
        self.camp_url.setStyleSheet('background-color: #FCFCFC; border: 1px solid #E2DFDF; border-radius:5px; padding-left:8px; padding-right:8px;color:#494343')
        self.camp_url.font()
        self.camp_url.setPlaceholderText('https://www.youtube.com/watch?v=1V_xRb0x9aw')

    def select_resolution(self):
        font_rd = QFont('fonts\CircularStd-Book.ttf')
        font_rd.setPointSize(10)

        css = ('color: #888080; letter-spacing:1.5px')

        self.rd_1 = QRadioButton("Alta qualidade",self)
        self.rd_1.move(70,262)
        self.rd_1.setFont(font_rd)
        self.rd_1.setStyleSheet(css)

        self.rd_2 = QRadioButton("Baixa qualidade",self)
        self.rd_2.move(70,290)#70,287
        self.rd_2.setFont(font_rd)
        self.rd_2.setStyleSheet(css)
        self.rd_2.isChecked()

        self.rd_3 = QRadioButton("Apenas o áudio",self)
        self.rd_3.move(70,316)#70,310
        self.rd_3.setFont(font_rd)
        self.rd_3.setStyleSheet(css)
        self.rd_3.isChecked()
    
    def update_checked(self):
        if self.rd_1.isChecked() == True:
            rd = 1
            return rd
        elif self.rd_2.isChecked() == True:
            rd = 2
            return rd
        elif self.rd_3.isChecked() == True:
            rd = 3
            return rd
        

    
    def button_download(self):
        css_btt = (
                "QPushButton"
                "{"
                "border-radius:10px; background-color: #E28086; color: #fff; font-size:18px"
                "}"
                "QPushButton::pressed"
                "{"
                "background-color : #D8797F;"
                "}"
                )

        self.btt_dw = QPushButton('BAIXAR',self)
        self.btt_dw.setGeometry(124,386,152,37)
        self.btt_dw.setStyleSheet(css_btt)
        self.btt_dw.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btt_dw.clicked.connect(self.directory_save)
    
    def directory_save(self):
        find_path_save = QFileDialog.getExistingDirectory(self, "Onde desejar salvar?")
        self.path_save = find_path_save

        self.download_video()
    
    def download_video(self):
        self.url_video = self.camp_url.text()

        res_vid = self.update_checked()

        start_download = DownloadYT(self.url_video,self.path_save).start_download(res_vid)

        self.messager_down(start_download)

        #if start_download:
            #print("Download concluído!")
    
    def messager_down(self,start_download):
        if start_download:
            sucess_messager = QMessageBox.about(self,"Download concluído","Pronto!\nSeu download foi concluído com sucesso!")

            
def start():
    app = QApplication(sys.argv)
    window_app = Janela()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()