import pathlib
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parents[0]

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="BeatSaverPython",
    version="1.0.0",
    license='MIT license',
    description="An Unofficial Python Beat Saver API Library.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/megamaz/beatsaver-python',
    author='megamaz',
    author_email="raphael.mazuel@gmail.com",
    classifiers = [
        'Development Status :: 4 - Beta',
        # 'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9'
    ],
    packages=find_packages(),
    python_requires='>=3.8, <4',
    project_urls={
        'Bug Reports': 'https://github.com/megamaz/beatsaver-python/issues'
    }
)