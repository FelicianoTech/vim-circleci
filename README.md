# vim-circleci [![CircleCI Build Status](https://circleci.com/gh/felicianotech/vim-circleci.svg?style=shield)](https://circleci.com/gh/felicianotech/vim-circleci) [![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/felicianotech/vim-circleci/master/LICENSE)

A Vim plugin for CircleCI.
This plugin is currently in beta.
The commands and dependencies may change before the v1.0.0 release.

This plugin provides features to make developing software that's tested on CircleCI easier.


## Usage

Once installed, this plugin provides a few useful features.

### Commands

`:CCIOpen` - Opens the CircleCI page for the project in your default browser.
`:CCIValidate` - Validate the repo's CircleCI configuration file.
`:CCIStatus` - Returns build status for `master` branch.


## Requirements

- Vim v8.0+ - with Python 3 support ([how to check](https://feliciano.tech/blog/how-to-check-if-vim-supports-python/))
- CircleCI CLI v0.1.2200+ - with CircleCI token configured ([install instructions](https://feliciano.tech/blog/how-to-install-the-circleci-cli/))


## Installation

With [Vundle](https://github.com/gmarik/vundle), add the following to your vimrc and then run `:PluginInstall`:

```
 Plugin 'felicianotech/vim-circleci'
```

With [Pathogen](https://github.com/tpope/vim-pathogen):

```
git clone https://github.com/felicianotech/vim-circleci ~/.vim/bundle/
```

Or install the plugin [without a plugin manager](https://howchoo.com/g/ztmyntqzntm/how-to-install-vim-plugins-without-a-plugin-manager).

## License

The code for this Vim plugin is licensed under the [MIT License](LICENSE).
