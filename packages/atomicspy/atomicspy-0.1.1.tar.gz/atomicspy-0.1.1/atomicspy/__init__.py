__version__ = '0.1.0'
__author__ = 'IHEfty'

from .generate import some_function  
from .data import load_data          

def hello_atomicpy():
    print("Welcome to AtomicsPy! Version:", __version__)

def help():
    print("=== AtomicsPy Help ===")
    print("Version:", __version__)
    print("Author:", __author__)
    print()
    print("Available Functions:")
    print("1. some_function(): Description of what some_function does.")
    print("2. load_data(): Description of how to load data.")
    print()
    print("For more information, visit the documentation or repository:")
    print("URL: https://github.com/IHEfty/atomics-py")
    print("======================")

__all__ = ['some_function', 'load_data', 'hello_atomicspy', 'help']

