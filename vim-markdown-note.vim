if !has('python')
	finish
endif

function! generateHTML()
	pyfile python/htmlGenerator.py
endfunc

command! -nargs=0 generateHTML call generateHTML()
