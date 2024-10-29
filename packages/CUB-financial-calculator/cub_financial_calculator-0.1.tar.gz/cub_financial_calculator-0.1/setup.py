from setuptools import setup, find_packages

setup(
    name='CUB_financial_calculator',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'CUB_financial_calculator=CUB_financial_calculator.cli:main',
        ],
    },
    description='A package for calculating financial metrics like net profit and ROI.',
    author='Alex',
    author_email='haylarrr@yandex.ru',
)