from abc import ABC, abstractmethod

class IRenderable(ABC):
	@abstractmethod
	def Render(self):
		pass

class Container(IRenderable):
	def __init__(self, name):
		self._name = name
		self._children = []

	def addChild(self, child):
		self._children.append(child)
		child._parent = self

	def isRoot(self):
		pass

class Leaf(IRenderable):
	def __init__(self, content):
		self._content = content

class Root(Container):
	def __new__(cls, title):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Root, cls).__new__(cls)
		return cls.instance

	def __init__(self, title):
		super().__init__(title)

	def Render(self):
		a = f"{self._name}\n\n"
		for txt in self._children:
			a += f"{txt.Render()}\n"
		return str(a)

	def isRoot(self):
		return True

class Heading(Container):
	def __init__(self, name):
		super().__init__(name)

	def Render(self):
		a = f"{self._name}\n"
		for txt in self._children:
			thetext = (txt.Render()).split('\n')
			for b in thetext:
				a += f"\t{b}\n"
		return a.rstrip("\n")

class Paragraph(Leaf):
	def __init__(self, content):
		super().__init__(content)

	def Render(self):
		return f"{self._content}"






class DocumentBuilder():
	def __init__(self, title):
		self.__root = Root(title)
		self._current = self.__root

	def addHeading(self, name):
		heading = Heading(name)
		self._current.addChild(heading)
		self._current = heading
		return self

	def addParagraph(self, text):
		paragraph = Paragraph(text)
		self._current.addChild(paragraph)
		return self

	def Up(self):
		if self._current.isRoot():
			print('in root already')
		else:
			self._current = self._current._parent
		return self

	def ToString(self):
		return self.__root.Render()


# doc = DocumentBuilder('maple juice')
# doc.addHeading('first heading!').addParagraph('some line of text!').addParagraph('another line of text!')
# doc.Up()
# doc.addParagraph('line of text outside the first heading')
# doc.addHeading('second heading!').addParagraph('another line of text!')
# doc.addHeading('third heading!').addParagraph('nests!')
# doc.Up()
# doc.addParagraph('text!')
# doc.Up()
# doc.addParagraph('conclude.')

# print(doc.ToString())
