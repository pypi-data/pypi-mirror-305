from setuptools import setup, find_packages

setup(
    name='sales_analyzer123',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Sofia',
    author_email='s.a.karpova@edu.centraluniversity.ru',
    description='Python package for analyzing sales data from a CSV file.',
    url='https://github.com/your-username/sales_analyzer',
    license='MIT',
    entry_points={
        'console_scripts': [
            'sales_analyzer = sales_analyzer.main:main',
        ],
    },
)