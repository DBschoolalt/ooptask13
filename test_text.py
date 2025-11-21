from text import Root, Heading

def test_rootrender():
	a = Root('1')
	assert a.Render() == '1\n\n'

def test_headingrender():
	a = Heading('1')
	assert a.Render() == '1'