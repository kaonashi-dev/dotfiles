# My Dotfiles

This repository contains my configuration files for my work environment (ArchLinux). It includes settings for my window manager, as well as a list of applications I need to install and how to configure them.

## Configuration

My base configuration file for my system includes the following settings:

- Shell configuration
- Environment variables
- Aliases for frequent commands
- Keyboard configuration
- Fonts and color settings
- Text editor configuration (VSCode)

To install these applications on my system, I run the following commands:

### System
```bash
yay -S neovim lsd bat dunst scrot cbatticon volumeicon brightnessctl pactl alacritty btop nitrogen thunar --noconfirm
```
### Development
```bash
yay -S docker node php --noconfirm
```
### Base Apps
```bash
yay -S brave-bin firefox-developer-edition visual-studio-code-bin postman-bin --noconfirm
```
### Multimedia
```bash
yay -S geeqie vlc --noconfirm
```
### GTK Theme
```bash
yay -S sweet-gtk-theme-dark sweet-folders-icons --noconfirm
```
### Software Applications

| Software                                                                                            | Utility                        |
| --------------------------------------------------------------------------------------------------- | ------------------------------ |
| **[pulseaudio, pavucontrol, pactl](https://wiki.archlinux.org/title/PulseAudio)**                   | Audio                          |
| **[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**             | Screen brightness              |
| **[Dunst](https://wiki.archlinux.org/index.php/Desktop_notifications)**                             | Notifications                  |
| **[Arandr](https://www.archlinux.org/packages/community/any/arandr/)**                              | GUI for Xrandr                 |
| **[cbatticon](https://www.archlinux.org/packages/community/x86_64/cbatticon/)**                     | Battery systray                |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**                   | Volume systray                 |

### Fonts, Themes, and GTK

| Software                                                                               | Utility                      |
| -------------------------------------------------------------------------------------- | ---------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Xorg compositor              |
| **[JetBrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads)**                | Font                         |
| **[Dracula](https://www.gnome-look.org/p/1687249)**                                    | GTK theme                    |
| **[Sweet](https://www.gnome-look.org/p/1253385/)**                                     | GTK icons                    |
| **[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**  | GUI for changing themes      |
| **[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**                          | GUI for setting wallpapers   |

### Apps

| Software                                                              | Utility                |
| --------------------------------------------------------------------- | ---------------------- |
| **[Alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Terminal emulator      |
| **[Thunar](https://wiki.archlinux.org/index.php/Thunar)**             | File explorer          |
| **[NeoVim](https://wiki.archlinux.org/index.php/Neovim)**             | Terminal text editor   |
| **[Rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menu                   |
| **[Scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Screenshot tool        |

## Usage
```bash
cd ~
git clone https://github.com/kaonashi-dev/dotfiles
```
