import sys
del sys.argv[0]

import game

import text

import json


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
		if (key in InfraData.__data):
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


InfraData.Set('game_chrs', [])

class CLIExecutor():
	@staticmethod
	def Execute(command, args, opts):
		CLIPresenter.Output('')
		if command == "newchr":
			InfraData.Get('game_chrs').append({"name": str(args[0]), "class": str(args[1]) } )
			CLIPresenter.Output(str(args[0])+' added')
			return 

		elif command == "loadjson":
			strin = ''
			InfraData.Set('game_chrs', [])
			with open('characters.json', 'r') as file:
				data = json.load(file)
			for i in data["characters"]:
				InfraData.Get('game_chrs').append({"name": i["name"], "class": i["class"]})
				CLIPresenter.Output(i["name"]+' loaded')
				strin += i["name"]+' loaded'+'\n'

			return(strin)



		elif command == "newgame":
			InfraData.Remove('thegame')
			InfraData.Set('thegame', game.Game())
			InfraData.Get('thegame').new(InfraData.Get('game_chrs'))
		elif command == "nextturn":
			return InfraData.Get('thegame').turn()

		elif command == "loadgame":
			with open('gamestate.json', 'r') as file:
				InfraData.Get('thegame').setState(json.load(file))
		elif command == "savegame":
			with open('gamestate.json', 'w') as file:
				json.dump(InfraData.Get('thegame').getState(), file)

		elif command == "listgame":
			return InfraData.Get('thegame').list()

		else:
			CLIPresenter.Output('invalid command!')


