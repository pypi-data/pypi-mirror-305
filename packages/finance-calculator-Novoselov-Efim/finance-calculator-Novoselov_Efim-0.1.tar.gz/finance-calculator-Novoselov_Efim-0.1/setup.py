from setuptools import setup, find_packages

setup(
    name='finance-calculator-Novoselov_Efim',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'finance-calculator-Novoselov_Efim=finance_calculator.__main__:main',
        ],
    },
    description='A package for calculating net profit and ROI',
    author='Novoselov Efim/Stanislav Kuleshov',
    author_email='kuku@mail.com'
)