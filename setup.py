from setuptools import setup, find_packages

setup(
    name='gousto_scraper',
    version='0.0.2',
    description='Gousto recipe scraper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VFjr/gousto-scraper',
    author='Victor Florea',
    author_email='victor.florea.jr@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'aiohttp>=3.8.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)