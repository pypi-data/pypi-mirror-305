from setuptools import setup, find_packages

setup(
    name='finance-calculator-NovEf',
    version='0.2',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'finance-calculator-NovEf=finance_calculator.__main__:main',
        ],
    },
    description='A package for calculating net profit and ROI',
    author='Novoselov Efim',
    author_email='kuku@mail.com'
)