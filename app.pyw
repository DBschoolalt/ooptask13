from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from main import *
app = QApplication([])
win = QMainWindow()
win.setGeometry(500, 200, 500,500)

CLIParser = CLIParser()
CLIExecutor = CLIExecutor()
CLIPresenter = CLIPresenter()

CLIExecutor.Execute('loadjson', '', '')
CLIExecutor.Execute('newgame', '', '')

label = QLabel(win)
label.setAlignment(Qt.AlignmentFlag.AlignTop)
label.setText('')
label.setGeometry(50, 20, 500-50, 500-20)
	

def func_loadjson():
	txt = CLIExecutor.Execute('loadjson', '', '')
	CLIExecutor.Execute('newgame', '', '')
	label.setText(txt)
def func_listchr():
	txt = CLIExecutor.Execute('listgame', '', '')
	label.setText(txt)
def func_turn():
	txt = CLIExecutor.Execute('nextturn', '', '')
	label.setText(txt)
def func_newchr():
	name, done1 = QInputDialog.getText(win, 'Input Dialog', 'Enter your name:')
	clas, done2 = QInputDialog.getItem(win, 'Input Dialog', 'pick a class:', ['Knight', 'Mystic', 'Creature'])
	print(name, clas)
	if done1 and done2:
		CLIExecutor.Execute('newchr', [name, clas], '')
		CLIExecutor.Execute('newgame', '', '')
def func_restartgame():
	CLIExecutor.Execute('newgame', '', '')
	label.setText('-- game reset --')

def func_savegame():
	CLIExecutor.Execute('savegame', '', '')
	label.setText(label.text()+'\n-- state saved --')

def func_loadgame():
	CLIExecutor.Execute('loadgame', '', '')
	label.setText('-- state loaded --')



buttons = {}
buttonset1 = [
	["next turn", func_turn],
	["current characters", func_listchr],
	["save current state", func_savegame],
	["load saved state", func_loadgame],

	["load characters from file (restarts the game)", func_loadjson],
	["add character (restarts the game)", func_newchr],
	["restart the game", func_restartgame],
]

for i,v in enumerate(buttonset1):
	buttons[v[0]] = QPushButton(win)
	buttons[v[0]].setText(v[0])
	buttons[v[0]].setGeometry(50, 500-(30*(len(buttonset1)-1))+(20+5)*i, 400, 20)
	buttons[v[0]].clicked.connect(v[1])






win.show()

app.exec()



#e.Execute('play', '', '')









# while True:
# 	inp = pr.Input('> ')
# 	command, args, opts = p.Parse(inp.split())
# 	e.Execute(command, args, opts)