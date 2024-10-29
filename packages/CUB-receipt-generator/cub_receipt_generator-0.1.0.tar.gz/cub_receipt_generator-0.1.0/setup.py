from setuptools import setup, find_packages

setup(
    name='CUB_receipt_generator',
    version='0.1.0',
    packages=find_packages(),
    description='A package for generating receipts from order data.',
    author='Alex',
    author_email='haylarrr@yandex.ru',
    entry_points={
        'console_scripts': [
            'receipt_generator=receipt_generator.cli:main',
        ],
    },
)