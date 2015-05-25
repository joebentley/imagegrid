from setuptools import setup

setup(
    name='imagegrid',
    version='0.1',
    py_modules=['grid'],
    entry_points='''
        [console_scripts]
        imagegrid=grid:main
    ''',
)
