if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source

# Aliases
alias cat="bat"
alias ls="lsd --group-dirs=first"
alias ll="lsd --group-dirs=first -l"
# Mac OS X only
alias code="open -a 'cursor'"
alias zed="open -a 'Zed' -n"
alias pip="pip3"

# Variables de entorno en fish
set -gx BAT_THEME tokyonight_night

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH

# Homebrew Python (prioridad sobre pyenv)
set --export PATH /opt/homebrew/bin $PATH

# pyenv initialization
if command -v pyenv 1>/dev/null 2>&1
    pyenv init - | source
end

# GPG
set -gx GPG_TTY (tty)

set -gx NVM_DIR "$HOME/.nvm"

# Cargar nvm
if test -s /opt/homebrew/opt/nvm/nvm.sh
    bass source /opt/homebrew/opt/nvm/nvm.sh
end

set --export NVM_DIR "$HOME/.nvm"

source ~/.orbstack/shell/init2.fish 2>/dev/null || :
