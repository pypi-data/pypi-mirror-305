from setuptools import setup, find_packages

setup(
    name='bobberThing',
    version='0.1.0',
    packages=find_packages(),
    author='sebass',
    author_email='sebass@sebass.fr.skibidi.com',
    description='bobber mcbob',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/bob',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
