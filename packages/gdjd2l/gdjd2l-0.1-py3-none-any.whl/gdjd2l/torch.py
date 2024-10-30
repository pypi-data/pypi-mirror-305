import torch
import pandas as pd
import numpy as np

class RegisterResult:
    def __init__(self,n):
        self.resultList = [0.] * n
    def add(self,*args):
        self.resultList = [a + float(b) for a,b in zip(self.resultList,args)]
    def __getitem__(self, item):
        return self.resultList[item]

if __name__ == '__main__':
    A =RegisterResult(2)
    print(A[0])






