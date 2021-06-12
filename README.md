A repo to deploy and test various Sanskrit fonts.

- Also see https://sanskrit-coders.github.io/site/pages/content/fonts/

# Installation
## Arch Linux
`yay -S sanskrit-fonts`

## Other Linux Distros
```sh
$ git clone https://github.com/sanskrit-coders/sanskrit-fonts.git
$ sudo mkdir -p /usr/share/fonts/sanskrit-fonts/
$ sudo cp -rf "sanskrit-fonts/fonts"/* "/usr/share/fonts/sanskrit-fonts/"
$ fc-cache -f -v # clear and regenerate font cache
```

# Contribution
- AUR Package <https://aur.archlinux.org/packages/sanskrit-fonts/>
- Creating a new release: See <https://aur.archlinux.org/cgit/aur.git/tree/README.md?h=sanskrit-fonts>.
