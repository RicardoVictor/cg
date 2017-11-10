from abc import ABC, abstractmethod

class Fonte(ABC):
    @abstractmethod
    def __init__(self, fx, fy, fz, IdR, IdG, IdB, IeR, IeG, IeB):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.IdR = IdR
        self.IdG = IdG
        self.IdB = IdB
        self.IeR = IeR
        self.IeG = IeG
        self.IeB = IeB