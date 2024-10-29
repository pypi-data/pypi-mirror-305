from setuptools import setup, find_packages

setup(
    name='my-package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'my-script=my_package.module:main_function',
        ],
    },
)