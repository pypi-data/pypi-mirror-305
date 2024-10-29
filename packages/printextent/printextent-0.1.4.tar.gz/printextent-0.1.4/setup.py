from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='printextent',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[],
    description='A text changing package that allows the user to easily change colors, text styles and color backgrounds.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ScriptingBytes',
    author_email='thomaskkyrouac@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)