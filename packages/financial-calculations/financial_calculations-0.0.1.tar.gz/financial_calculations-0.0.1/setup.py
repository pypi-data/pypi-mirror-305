from setuptools import setup, find_packages

setup(
    name="financial_calculations",
    version="0.0.1",
    packages=find_packages(),
    description="Пакет для расчета чистой прибыли и ROI",
    author="Egor Drobyazko",
    author_email="drobyazko_04@mail.ru",
    entry_points={
        'console_scripts': [
            'calculate_financials=main:main',
        ],
    },
)