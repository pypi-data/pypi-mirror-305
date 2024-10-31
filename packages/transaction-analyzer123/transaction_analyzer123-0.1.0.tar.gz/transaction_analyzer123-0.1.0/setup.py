from setuptools import setup, find_packages

setup(
    name='transaction_analyzer123',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Sofia',
    author_email='s.a.karpova@edu.centraluniversity.ru',
    description='Python package for analyzing transactions from a CSV file.',
    url='https://github.com/your-username/transaction_analyzer',
    license='MIT',
    entry_points={
        'console_scripts': [
            'transaction_analyzer = transaction_analyzer.main:main',
        ],
    },
)