from setuptools import setup, find_packages

setup(
    name='imagegrid',
    version='0.1',
    scripts=['grid.py'],
    entry_points='''
        [console_scripts]
        imagegrid=grid:main
    '''
)
