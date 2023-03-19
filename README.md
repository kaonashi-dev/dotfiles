# Mis Dotfiles

Este repositorio contiene mis archivos de configuración para mi entorno de trabajo (ArchLinux) . Incluye configuración para mi window manager, así como también una lista de las aplicaciones que necesito instalar y cómo configurarlas.

## Configuración

Mi archivo de configuración base para mi sistema incluye las siguientes configuraciones:

- Configuración del shell
- Variables de entorno
- Alias para comandos frecuentes
- Configuración de teclado
- Configuración de fuentes y colores
- Configuración de mi editor de texto (VSCode)

Para instalar estas aplicaciones en mi sistema, ejecuto los siguientes comandos:

### Sistema
```bash
yay -S neovim lsd bat dunst scrot cbatticon volumeicon brightnessctl pactl alacritty btop nitrogen thunar --noconfirm
```
### Dev
```bash
yay -S yay -S docker node php --noconfirm --noconfirm
```
### Apps Base
```bash
yay -S brave-bin firefox-developer-edition visual-studio-code-bin postman-bin --noconfirm
```
### Multimedia
```bash
yay -S geeqie vlc --noconfirm
```
### Tema de GTK
```bash
yay -S sweet-gtk-theme-dark sweet-folders-icons --noconfirm
```
### Aplicaciones Software

| Software                                                                                            | Utilidad                         |
| --------------------------------------------------------------------------------------------------- | -------------------------------- |
| **[pulseaudio, pavucontrol, pactl](https://wiki.archlinux.org/title/PulseAudio)**                                       | Audio                            |
| **[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**             | Brillo de la pantalla            |
| **[Dunst](https://wiki.archlinux.org/index.php/Desktop_notifications)**                             | Notificaciones                   |
| **[Arandr](https://www.archlinux.org/packages/community/any/arandr/)**                              | GUI Xrandr                       |
| **[cbatticon](https://www.archlinux.org/packages/community/x86_64/cbatticon/)**                     | Bateria systray                  |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**                   | Volumen systray                  |

### Fuentes, temas y GTK

| Software                                                                               | Utilidad                   |
| -------------------------------------------------------------------------------------- | -------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Compositor Xorg            |
| **[JetBrainsMono Nerd Font](https://www.nerdfonts.com/font-downloads)**                | Fuente                     |
| **[Dracula](https://www.gnome-look.org/p/1687249)**                                    | GTK theme                  |
| **[Sweet](https://www.gnome-look.org/p/1253385/)**                                     | GTK iconos                 |
| **[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**  | GUI for changing themes    |
| **[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**                          | GUI for setting wallpapers |

### Apps

| Software                                                              | Utilidad                 |
| --------------------------------------------------------------------- | ------------------------ |
| **[Alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Emulador de terminal     |
| **[Thunar](https://wiki.archlinux.org/index.php/Thunar)**             | Explorador de archivos   |
| **[NeoVim](https://wiki.archlinux.org/index.php/Neovim)**             | Terminal editor          |
| **[Rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menu                     |
| **[Scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Captura de pantalla      |

## Uso
```bash
cd ~
git clone https://github.com/whoami-coder/dotfiles
```

## Contribución

Siéntete libre de tomar lo que necesites de mis dotfiles para tu propio uso, o hacer una contribución al repositorio. Siéntete libre de abrir un Pull Request o una Issue si tienes sugerencias.
