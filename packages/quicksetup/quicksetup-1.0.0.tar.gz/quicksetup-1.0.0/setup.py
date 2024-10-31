from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='quicksetup',
  version='1.0.0',
  description='For beginners to do a quick installation.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  license='MIT', 
  classifiers=classifiers,
  keywords='essentials', 
  packages=find_packages(),
  install_requires=[
      'requests',
      'pystyle',
      'colorama',
      'numpy',
      'datetime',
      'discord',
      'discord.py',
      'customtkinter',
      'auto-py-to-exe',
      'beutifulsoup4',
      'pycord',
      'pygame',
      'pyinstaller',
      'pyautogui',
      'pynput',
      'pyperclip',
      'python-nmap',
      'selenium',
      'scapy',
      'twine',
      'tesseract',
      'termcolor'
  ] 
)