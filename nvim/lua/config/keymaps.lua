local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}
local cmd = vim.cmd


-- don't use arrow keys
map('', '<up>', '<nop>', {noremap = true})
map('', '<down>', '<nop>', {noremap = true})
map('', '<left>', '<nop>', {noremap = true})
map('', '<right>', '<nop>', {noremap = true})

-- move in INSERT mode
map('i', '<C-h>', '<left>', default_opts)
map('i', '<C-j>', '<down>', default_opts)
map('i', '<C-k>', '<up>', default_opts)
map('i', '<C-l>', '<right>', default_opts)

-- nvim-tree
map('n', '<C-n>', ':Neotree toggle<CR>', default_opts)       -- open/close
