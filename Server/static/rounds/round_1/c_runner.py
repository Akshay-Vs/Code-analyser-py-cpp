from ctypes import cdll, c_int
import subprocess

subprocess.run(['gcc', '-shared', '-o', 'problem.so', 'problem.c'])
lib = cdll.LoadLibrary('./problem.so')

lib.add_numbers.argtypes = [c_int, c_int]
lib.add_numbers.restype = c_int

result = lib.add_numbers(1, 2)
print(result)