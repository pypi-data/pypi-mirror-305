from setuptools import setup, find_packages

setup(
    name="electrox",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'tkinter',  # Make sure to install tkinter as it's used in the code
    ],
    entry_points={
        'console_scripts': [
            'electrox = electrox:main',
        ],
    },
    author="Hussain Luai",
    author_email="hxolotl15@gmail.com",
    description="Electrox is a Python framework for 2D game development with Gen Z vibes",
)
