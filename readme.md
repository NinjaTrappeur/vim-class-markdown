# vim-class-markdown

This vim plugin is designed to make class notetaking easier by taking great advantage of markdown and webcams.

###Dependencies
- Vim compiled with python
- Python markdown
- Python pygments (for code syntax hilighting)
- Vim-pathogen

###Installation
First please install [vim-pathogen](https://github.com/tpope/vim-pathogen).
Next, install python2-pip.
Then, install python markdown and pygments:

	pip install markdown pygments

Finally, install vim-class-markdown in your bundle:

	cd ~/.vim/bundle
	git clone https://github.com/NinjaTrappeur/vim-class-markdown.git
 
###Features
- Automatic html generation

###Usage
- :GenerateHTML to generate the html file. This file will be generated at the same location than the markdown file.
