from setuptools import setup, find_packages

setup(
    name="electrox",
    version="1.24.1",
    packages=find_packages(),
    install_requires=[
        'pygame',  # Make sure to install tkinter as it's used in the code
    ],
    entry_points={
        'console_scripts': [
            'electrox = electrox:main',
        ],
    },
    author="Hussain Luai",
    author_email="hxolotl15@gmail.com",
    description="Electrox is a Python framework for 2D game development with Gen Z and Gen Aplha vibes for some reason... nvm enjoy electrox.",
)
