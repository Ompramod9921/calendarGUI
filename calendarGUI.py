import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget

class CalendarDemo(QWidget):

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Calendar')
		self.setGeometry(250, 250, 400, 250)
		self.initUI()

	def initUI(self):
		self.calendar = QCalendarWidget(self)
		self.calendar.setGridVisible(True)

def main():
	app = QApplication(sys.argv)
	demo = CalendarDemo()
	demo.show()
	sys.exit(app.exec_())

main()