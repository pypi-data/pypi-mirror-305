from setuptools import setup, find_packages

setup(
    name='sales_analyzer_cu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas'],
    author='Anastasia',
    author_email='a.opushneva@edu.centraluniversity.ru',
    description='Python package for analyzing sales data from a CSV file.',
    url='https://github.com/your-username/sales_analyzer',
    license='MIT',
    entry_points={
        'console_scripts': [
            'sales_analyzer = sales_analyzer.main:main',
        ],
    },
)