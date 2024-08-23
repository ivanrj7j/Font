from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    required = f.read().split("\n")

with open("README.md", "r") as f:
    desc = f.read()

setup(
    name='Font',
    version='1.0',
    packages=find_packages(),
    install_requires=required,
    description='A custom text rendering library using custom fonts for opencv',
    author='Ivan Raphel Jaison',
    author_email='ivanrj7j@gmail.com',
    url='https://github.com/ivanrj7j/Font',
    license='Apache 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    long_description_content_type='text/markdown',
    long_description=desc
)