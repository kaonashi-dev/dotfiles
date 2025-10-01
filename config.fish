if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source

# Aliases
alias node="bun"
alias cat="bat"
alias ls="lsd --group-dirs=first"
alias ll="lsd --group-dirs=first -l"
# Mac OS X only
alias code="open -a 'Zed'"
alias claude="bun run --bun claude"

# Variables de entorno en fish
set -gx BAT_THEME tokyonight_night

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH

# GPG
set -gx GPG_TTY (tty)

# Función para cambiar perfiles de AWS
function setaws
    if test (count $argv) -eq 0
        echo "No arguments supplied"
        echo "Example: setaws name"
        echo "Available profiles:"
        aws configure list-profiles
    else
        echo "Exporting aws profiles to: $argv[1]"
        set -gx AWS_PROFILE $argv[1]
        echo "set -gx AWS_PROFILE $argv[1]"
        set -gx AWS_DEFAULT_PROFILE $argv[1]
        echo "set -gx AWS_DEFAULT_PROFILE $argv[1]"
        set -gx AWS_SDK_LOAD_CONFIG 1
        echo "AWS profile set to: $argv[1]"
    end
end
