from setuptools import setup, find_packages

setup(
    name='anton_color',
    version='0.1.1',
    author='AntonThomzz',
    author_email='antonthomzz@gmail.com',
    description='Modul untuk memberikan warna teks di terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AntonThomz/color-py',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)