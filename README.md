A repo to deploy and test various Sanskrit fonts.

# Creating a new Arch Linux package release
- Create a github release.
- Update packages/PKGBUILD.
  - Fix the version numbers.
  - Get the sha256sum by running `sha256sum packages/releases/sanskrit-fonts-1.0.tar.gz`
- Verify package by running `makepkg` in packages directory.
- Update AUR repository.
