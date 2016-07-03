from setuptools import setup, find_packages

setup(
    name='imagegrid',
    version='0.1',
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        imagegrid=grid:main
    ''',
    include_package_data=True
)
