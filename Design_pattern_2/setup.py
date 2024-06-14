from setuptools import setup

setup(
    name='fje',
    version='0.1',
    py_modules=['fje'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        fje=fje:main
    ''',
)