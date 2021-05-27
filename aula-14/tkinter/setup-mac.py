# Converte aplicação para macOS

from setuptools import setup

APP=['gui-grid.py']
OPTIONS= {
  'argv_emulation': True
}

setup(
  app=APP,
  options={'py2app': OPTIONS},
  setup_requires=['py2app']
)