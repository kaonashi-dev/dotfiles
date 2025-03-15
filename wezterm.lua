local wezterm = require("wezterm")

local config = wezterm.config_builder()

-- config.color_scheme = 'Catppuccin Mocha'
config.color_scheme = 'Gruvbox Dark (Gogh)'

config.font = wezterm.font("JetBrains Mono", { weight = "Regular" })
config.font_size = 19

config.enable_tab_bar = false

config.window_decorations = "RESIZE"
config.window_background_opacity = 0.95
-- config.macos_window_background_blur = 10

return config