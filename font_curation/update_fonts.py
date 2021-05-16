import glob
import logging
import os.path
import shutil


logging.basicConfig(
  level=logging.DEBUG,
  format="%(levelname)s: %(asctime)s %(message)s"
)


NOTO_TTF_DIR = "/home/vvasuki/misc-git/noto-fonts/hinted/ttf/"
HUGO_THEME_FONT_DIR = "/home/vvasuki/vvasuki-git/kannaDa/themes/sanskrit-documentation-theme-hugo/static/fonts/"
INDIC_FONT_REPO_DIR = "/home/vvasuki/sanskrit-coders/sanskrit-fonts/fonts"

def update_noto_fonts(src_dir):
  files = glob.glob(os.path.join(src_dir, "**/" + "Noto*.ttf"))
  for file in files:
    latest_file = glob.glob(os.path.join(NOTO_TTF_DIR, "**/" + os.path.basename(file)))[0]
    logging.info("Copying %s to %s", latest_file, file)
    shutil.copyfile(latest_file, file)


if __name__ == '__main__':
  logging.info("Please ensure that you've pulled the latest files at %s", NOTO_TTF_DIR)
  # update_noto_fonts(src_dir=HUGO_THEME_FONT_DIR)
  update_noto_fonts(src_dir=INDIC_FONT_REPO_DIR)