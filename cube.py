import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import random

class Cube(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1200, 900)
        self.setWindowTitle('Приложение')
        #Ставим размер окна и его название
        
        self.picnames = ['one.png', 'two.png', 'three.png', 'four.png', 'five.png', 'six.png']
        self.piclabel = QLabel(self)
        self.piclabel.move(400, 300)
        self.piclabel.resize(300, 300)
        #картинка
        
        self.newgame = QPushButton('Перезапустить', self)
        self.newgame.clicked.connect(self.restart)
        self.newgame.move(20, 20)
        #кнопка перезапуска
        
        self.results = QLabel(self)
        self.results.resize(600, 20)
        self.results.move(400, 130)
        #результаты последних 10 бросков
        
        self.lblresults = QLabel(self)
        self.lblresults.setText('Последние 10 бросков:')
        self.lblresults.resize(150, 20)
        self.lblresults.move(400, 100)
        #надпись
        
        self.throw = QPushButton('Бросить', self)
        self.throw.move(600, 50)
        self.throw.clicked.connect(self.makethrow)
        #кнопка для броска кубика
        
        self.listnumbers = []
        #список результатов бросков
        
        self.labelfreq = QLabel(self)
        self.labelfreq.setText('Частота выпадения чисел на кубике:')
        self.labelfreq.resize(600, 20)
        self.labelfreq.move(100, 100)
        #надпись


        self.frequencies = QLabel(self)
        self.frequencies.resize(100, 200)
        self.frequencies.move(100, 120)
        #частоты выпадения чисел
        
        self.all = 0
        self.counter = [0] * 6
        self.strfreq = ''
        #счетчики количества бросков и чисел на кубике, строка для вывода
        
        self.amount = QLabel(self)
        self.amount.setText('N = ')
        self.amount.resize(100, 20)
        self.amount.move(600, 100)
        #вывод количества бросков
        
    def makethrow(self):
        number = random.randint(1, 6)
        filename = self.picnames[number - 1]
        pixmap = QPixmap(filename)
        self.piclabel.setPixmap(pixmap)
        self.listnumbers.append(str(number))
        if len(self.listnumbers) == 11:
            self.listnumbers.remove(self.listnumbers[0])
        self.results.setText('; '.join(self.listnumbers))
        self.counter[number - 1] += 1
        self.all += 1
        for i in range(6):
            f = (self.counter[i] / self.all) * 100
            f = '{0:.2f}'.format(f)
            self.strfreq += 'f(' + str(i + 1) + ')=' + f + '%' + 2 * '\n'
        self.frequencies.setText(self.strfreq)
        self.amount.setText('N = ' + str(self.all))
        self.strfreq = ''
        #работаем с данными, основная функция
        
    def restart(self):
        self.results.setText('')
        self.piclabel.clear()
        self.listnumbers = []
        self.counter = [0] * 6
        self.frequencies.setText('')
        self.strfreq = ''
        self.all = 0
        self.amount.setText('N = ')
        #функция перезапуска
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cube()
    ex.show()
    sys.exit(app.exec_())
