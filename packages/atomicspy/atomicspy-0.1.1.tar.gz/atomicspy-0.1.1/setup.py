from setuptools import setup, find_packages

setup(
    name='atomicspy',
    version='0.1.1',
    author='IHEfty',
    author_email='asifthegambler@gmail.com',
    description='A Python library for chemical compounds and elements.',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/IHEfty/atomic-py',  
    packages=find_packages(),
    include_package_data=True, 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
