from setuptools import setup, find_packages

setup(
    name='guard_decorator',
    version='0.1.0',
    author='xilax79',
    author_email='xilax79@gmail.com',
    description='A decorator to simplify error handling in Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xilax79/guard_decorator',
    packages=find_packages(),
    license='Apache 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
