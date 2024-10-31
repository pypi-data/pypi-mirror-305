from setuptools import setup, find_packages

setup(
    name='customer_analyzer123',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Sofia',
    author_email='s.a.karpova@edu.centraluniversity.ru',
    description='Python package for analyzing customer data from a CSV file and generating a report.',
    url='https://github.com/your-username/customer_analyzer',
    license='MIT',
    entry_points={
        'console_scripts': [
            'customer_analyzer = customer_analyzer.main:main',
        ],
    },
)