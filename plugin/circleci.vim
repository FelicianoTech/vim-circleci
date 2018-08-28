if !has("python3")
	echo "Error: vim-circleci requires Vim compiled with Python 3 support. Exiting."
	finish
endif

if exists('g:vim_circleci_loaded')
	finish
endif

let g:vim_circleci_loaded = 1

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import cci
EOF


function! CCIOpen()
	python3 cci.vim_open()
endfunction

command! -nargs=0 CCIOpen call CCIOpen()

function! CCIValidate()
	python3 cci.config_validate()
endfunction

command! -nargs=0 CCIValidate call CCIValidate()


function! CCIStatus()
	python3 cci.vim_status()
endfunction

command! -nargs=0 CCIStatus call CCIStatus()
