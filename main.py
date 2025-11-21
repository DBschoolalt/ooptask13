import sys
del sys.argv[0]

import characters

from characters import *

import text


class InfraData:
	__data = {}
	@staticmethod
	def Set(key, data):
		InfraData.__data.update({key: data})

	@staticmethod
	def Get(key):
		return InfraData.__data[key]

	@staticmethod
	def Exists(key):
		if key in InfraData.__data:
			return True
		return False

	@staticmethod
	def Remove(key):
		InfraData.__data.pop(key)

	@staticmethod
	def Clear():
		InfraData.__data.clear()



class CLIParser:
	@staticmethod
	def Parse(commandline):
		commandline = commandline
		command = commandline[0]
		args = [] 
		opts = {}

		skip_next = False
		for i, arg in enumerate(commandline): 
			if i == 0 or skip_next:
				skip_next = False
				continue
			if arg.startswith("--") or arg.startswith("-"): 
				opts[arg] = commandline[i + 1]
				skip_next = True
			else:
				args.append(arg)

		# print(f"Command: {command}") 
		# print(f"Args passed: {str.join(", ", args)}") 
		# print(f"Options passed: {opts}")

		return command, args, opts

class CLIPresenter():
	@staticmethod
	def Input(text):
		return input(text)
	def Output(text):
		print(text)

class CLIExecutor():
	presenter = CLIPresenter()
	data = InfraData()
	@staticmethod
	def Execute(command, args, opts):
		if command == "newchr":
			name = CLIPresenter.Input('Character name: ')
			chrclass = CLIPresenter.Input('Select class (1=Knight, 2=Mystic, 3=Creature): ')
			if chrclass == '1':
				InfraData.Get('game_chrs').append(characters.Knight(name))
			elif chrclass == '2':
				InfraData.Get('game_chrs').append(characters.Mystic(name))
			elif chrclass == '3':
				InfraData.Get('game_chrs').append(characters.Creature(name))

		elif command == "listchr":
			for i in InfraData.Get('game_chrs'):
				CLIPresenter.Output(i.list())

		elif command == "startgame":
			g = game.Game()
			g.new(InfraData.Get('game_chrs'))
			g.play()

		elif command == "newdoc":

			InfraData.Set('doc', text.DocumentBuilder(args[0]))

		elif command == "addp":
			if not InfraData.Exists('doc'):
				CLIPresenter.Output('no document!')
				return
			InfraData.Get('doc').addParagraph(args[0])

		elif command == "addh":
			if not InfraData.Exists('doc'):
				CLIPresenter.Output('no document!')
				return
			InfraData.Get('doc').addHeading(args[0])

		elif command == "docup":
			if not InfraData.Exists('doc'):
				CLIPresenter.Output('no document!')
				return
			InfraData.Get('doc').Up()


		elif command == "doc":
			if not InfraData.Exists('doc'):
				CLIPresenter.Output('no document!')
				return
			CLIPresenter.Output(InfraData.Get('doc').ToString())


		else:
			CLIPresenter.Output('invalid command!')


p = CLIParser()
e = CLIExecutor()
pr = CLIPresenter()

InfraData.Set('game_chrs', [])

while True:
	inp = pr.Input('> ')
	command, args, opts = p.Parse(inp.split())
	e.Execute(command, args, opts)
