from setuptools import setup, find_packages

setup(
    name='py_game_of_life',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'py_game_of_life': ['toad.txt'],
    },
    install_requires=[
        # Add any dependencies here
    ],
)