from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='canatax',
    version='0.2.0',
    description='A simple Canadian income tax calculator.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Michael Pearce',
    author_email='firstflush@protonmail.com',
    url='https://github.com/firstflush/canatax',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
