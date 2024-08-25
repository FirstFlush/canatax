from setuptools import setup, find_packages

setup(
    name='canatax',
    version='1.3.0',
    description='An easy-to-use, dependency-free Canadian sales and income tax calculator.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Michael Pearce',
    author_email='firstflush@protonmail.com',
    url='https://github.com/firstflush/canatax',
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
