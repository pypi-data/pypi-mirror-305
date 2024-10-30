from setuptools import setup, find_packages

setup(
    name='customer_analyzer_cu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas'],
    author='Anastasia',
    author_email='a.opushneva@edu.centraluniversity.ru',
    description='Python package for analyzing customer data from a CSV file and generating a report.',
    url='https://github.com/your-username/customer_analyzer',
    license='MIT',
    entry_points={
        'console_scripts': [
            'customer_analyzer = customer_analyzer.main:main',
        ],
    },
)