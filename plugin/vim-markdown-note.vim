if !has('python')
	finish
endif

function! GenerateHTML()
	pyfile ~/.vim/bundle/vim-class-markdown/python/htmlGenerator.py
endfunc

command! -nargs=0 GenerateHTML call GenerateHTML()
