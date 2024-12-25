# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Plugins
plugins=(
   zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh

# User configuration

# Aliases
alias cat="bat"
alias ls="lsd --group-dirs=first"
alias ll="ls -l"
# Mac OS X only
alias code="open -a 'Zed'"
alias ps.="open -a 'phpstorm' ."
alias phpStorm="open -a 'phpstorm'"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
