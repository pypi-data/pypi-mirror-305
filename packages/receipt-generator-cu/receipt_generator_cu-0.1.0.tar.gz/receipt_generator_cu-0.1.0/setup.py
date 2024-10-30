from setuptools import setup, find_packages

setup(
    name='receipt_generator_cu',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pandas'],
    author='Anastasia',
    author_email='a.opushneva@edu.centraluniversity.ru',
    description='Python package for generating receipts from JSON data.',
    url='https://github.com/your-username/receipt_generator',
    license='MIT',
    entry_points={
        'console_scripts': [
            'receipt_generator = receipt_generator.main:main',
        ],
    },
)