from pathlib import Path
from setuptools import setup, find_packages

# Setup process taken from here: https://www.freecodecamp.org/news/build-your-first-python-package/.

DESCRIPTION = 'Go language support for ninja-bear'
LONG_DESCRIPTION = Path(__file__).parent.absolute().joinpath('README.md').read_text()

setup(
        name='ninja-bear-language-go', 
        version='0.1.0',
        author='monstermichl',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        py_modules=['ninja_bear_language_go'],
        entry_points = {
            'ninja_bear_language_go': ['config=ninja_bear_language_go.config:Config']
        },
        extras_require={
            'dev': [
                'ninja-bear>=0.1.0',
                'wheel>=0.41.1',
                'twine>=4.0.2',
                'ruff>=0.0.47',
                'coverage>=7.2.7',
            ],
        },
        python_requires='>=3.10',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],
        url='https://github.com/monstermichl/ninja-bear-language-go.git',
        keywords=[
            'ninja-bear',
            'plugin',
            'language',
            'go',
        ],
)
