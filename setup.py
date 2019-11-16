from setuptools import setup

setup(
    name='html-compiler',
    version='0.1',
    author='Hsuan-Hau Liu',
    description='A simple and lightweight html compiler.',
    packages=['html_compiler',],
    install_requires=['beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'html_compiler=html_compiler.__main__:main'
        ]
    }
)
