let SessionLoad = 1
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
doautoall SessionLoadPre
silent only
silent tabonly
cd C:/IT/study/python_crash_course/crash_course/eric_matthes/12-20_chapters_projects/web_applications
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
let s:shortmess_save = &shortmess
set shortmess+=aoO
badd +22 C:/IT/study/python_crash_course/crash_course/eric_matthes/12-20_chapters_projects/web_applications/ll_project/urls.py
badd +13 learning_logs/urls.py
badd +218 ~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/keymaps.lua
badd +11 learning_logs/views.py
badd +1 learning_logs/index.html
badd +2 C:/IT/study/python_crash_course/crash_course/eric_matthes/12-20_chapters_projects/web_applications/learning_logs/tests.py
badd +4 learning_logs/templates/learning_logs/index.html
badd +6 learning_logs/templates/learning_logs/base.hmtl
badd +6 learning_logs/templates/learning_logs/base.html
badd +14 learning_logs/templates/learning_logs/topics.html
badd +125 ~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/options.lua
argglobal
%argdel
edit learning_logs/templates/learning_logs/index.html
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
wincmd w
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe '1resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 1resize ' . ((&columns * 63 + 96) / 192)
exe '2resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 2resize ' . ((&columns * 63 + 96) / 192)
exe '3resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 3resize ' . ((&columns * 63 + 96) / 192)
exe '4resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 4resize ' . ((&columns * 64 + 96) / 192)
exe '5resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 5resize ' . ((&columns * 63 + 96) / 192)
exe '6resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 6resize ' . ((&columns * 64 + 96) / 192)
argglobal
balt learning_logs/index.html
setlocal foldmethod=expr
setlocal foldexpr=v:lua.vim.lsp.foldexpr()
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 4 - ((3 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 4
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("learning_logs/urls.py", ":p")) | buffer learning_logs/urls.py | else | edit learning_logs/urls.py | endif
if &buftype ==# 'terminal'
  silent file learning_logs/urls.py
endif
balt learning_logs/templates/learning_logs/index.html
setlocal foldmethod=expr
setlocal foldexpr=v:lua.LazyVim.treesitter.foldexpr()
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 13 - ((12 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 13
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("learning_logs/templates/learning_logs/base.html", ":p")) | buffer learning_logs/templates/learning_logs/base.html | else | edit learning_logs/templates/learning_logs/base.html | endif
if &buftype ==# 'terminal'
  silent file learning_logs/templates/learning_logs/base.html
endif
balt learning_logs/templates/learning_logs/base.hmtl
setlocal foldmethod=expr
setlocal foldexpr=0
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 6 - ((5 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 6
normal! 0
wincmd w
argglobal
if bufexists(fnamemodify("~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/options.lua", ":p")) | buffer ~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/options.lua | else | edit ~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/options.lua | endif
if &buftype ==# 'terminal'
  silent file ~/AppData/Local/nvim-data/lazy/LazyVim/lua/lazyvim/config/options.lua
endif
balt learning_logs/templates/learning_logs/base.html
setlocal foldmethod=expr
setlocal foldexpr=v:lua.vim.lsp.foldexpr()
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
121
sil! normal! zo
let s:l = 125 - ((24 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 125
normal! 04|
wincmd w
argglobal
if bufexists(fnamemodify("learning_logs/views.py", ":p")) | buffer learning_logs/views.py | else | edit learning_logs/views.py | endif
if &buftype ==# 'terminal'
  silent file learning_logs/views.py
endif
balt learning_logs/templates/learning_logs/base.html
setlocal foldmethod=expr
setlocal foldexpr=v:lua.LazyVim.treesitter.foldexpr()
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 11 - ((10 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 11
let s:c = 49 - ((31 * winwidth(0) + 31) / 63)
if s:c > 0
  exe 'normal! ' . s:c . '|zs' . 49 . '|'
else
  normal! 049|
endif
wincmd w
argglobal
if bufexists(fnamemodify("learning_logs/templates/learning_logs/topics.html", ":p")) | buffer learning_logs/templates/learning_logs/topics.html | else | edit learning_logs/templates/learning_logs/topics.html | endif
if &buftype ==# 'terminal'
  silent file learning_logs/templates/learning_logs/topics.html
endif
balt learning_logs/views.py
setlocal foldmethod=expr
setlocal foldexpr=v:lua.vim.lsp.foldexpr()
setlocal foldmarker={{{,}}}
setlocal foldignore=#
setlocal foldlevel=99
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldenable
let s:l = 14 - ((13 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 14
normal! 014|
wincmd w
4wincmd w
exe '1resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 1resize ' . ((&columns * 63 + 96) / 192)
exe '2resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 2resize ' . ((&columns * 63 + 96) / 192)
exe '3resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 3resize ' . ((&columns * 63 + 96) / 192)
exe '4resize ' . ((&lines * 29 + 30) / 61)
exe 'vert 4resize ' . ((&columns * 64 + 96) / 192)
exe '5resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 5resize ' . ((&columns * 63 + 96) / 192)
exe '6resize ' . ((&lines * 30 + 30) / 61)
exe 'vert 6resize ' . ((&columns * 64 + 96) / 192)
tabnext 1
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0 && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20
let &shortmess = s:shortmess_save
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
set hlsearch
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
