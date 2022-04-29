# Vim

This directory contains a [`Vagrantfile`](./Vagrantfile) and vim configuration
which defines a virtual machine to demonstrate how [vim](https://www.vim.org/)
can work with tools to help improve your Python code quality.

The virtual machine is based on Arch Linux and will work with both the
virtualbox and libvirt backends for Vagrant.

See the [Vagrant documentation](https://www.vagrantup.com/downloads) for
installation instructions.

## Getting started

Start and provision the virtual machine

```bash
vagrant up
```

Connect to the virtual machine

```bash
vagrant ssh
```

When you first start vim, the [vim-plug](https://github.com/junegunn/vim-plug)
plugin manager will be installed along with a [selection of
plugins](vim_config/vim/plug.vim).

```bash
vim
```

## Usage

The examples directory will have been copied to your current working directory
(`/home/vagrant`) during provisioning.

Open one of the broken files with vim

```bash
vim examples/mypy/incompatible_type/broken.py
```

[Syntastic](https://github.com/vim-syntastic/syntastic) has been configured to
automatically open a list of errors in the [location
list](https://vimhelp.org/quickfix.txt.html).

Lines with errors are also indicated to the left of the line numbers.

You can navigate to errors forwards and backwards in the list using `]l` and
`[l` respectively. `[L` and `]L` will take you to the first and last errors
respectively. These macros are defined in the
[vim-unimpaired](https://github.com/tpope/vim-unimpaired) plugin.

When you have made changes you can rerun the checkers with `:SyntasticCheck`.
The checkers will also be rerun automatically whenever you save a file.

You can look at the details of the available and enabled checkers with
`:SyntasticInfo`.

If Syntastic messages are getting in your way, you can turn automatic checking
off for the buffer with `:SyntasticToggleMode`.

## Airline integration

The [vim-airline](https://github.com/vim-airline/vim-airline) status bar has a
Syntastic plugin. When you open a file with errors, Syntastic, information will
be shown at the right hand side of the status bar. It will indicate the line
number of the first error and the total number of errors.
