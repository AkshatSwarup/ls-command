from setuptools import setup

setup(
    name='ls_command',
    version='0.1.0',
    description='Prints out json content in the style of ls (linux utility)',
    url='https://github.com/AkshatSwarup/ls-command',
    author='Akshat Swarup',
    author_email='akshatswarup62@gmail.com',
    license='LICENSE.txt',
    packages=['ls_command'],
    install_requires=['pytest'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3',
    ],
)