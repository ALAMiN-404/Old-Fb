import os, sys
try:
    __import__("cyber").Main()
except Exception as e:
    exit(str(e))
