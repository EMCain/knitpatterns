from abc import ABC
from typing import List, Optional

class KnittingBase(ABC):
    def reverse(self): 
        """
        this should always return its own type.
        """
        raise NotImplementedError

class Stitch(KnittingBase):
    def __init__(self, name: str, symbol: str, mother_loops: int=1, daughter_loops: int=1, reverse: 'Stitch'=None,  mirror: 'Stitch'=None):
        """
        A single stitch, which may include multiple loops 
        name - what the stitch would be called in a written pattern e.g. k, p, y/o, ssk, k2tog etc. 
        symbol - a Unicode symbol representing the stitch in a chart e.g. | for knit, - for purl, etc. 
        mother_loops - how many initial loops are taken up by the stitch, e.g. k2tog (knit two together) starts with 2 loops so this would be 2.
        daughter_loops - how many result from the stitch, e.g. k2tog (knit two together) results in 1 loop so this would be 1.
        reverse - what this stitch would be on the "wrong" side, e.g. a purl is the reverse of a knit. Defaults to self. 
        mirror - what this stitch would look like flipped left-to-right e.g. a k2tog is the mirror of a ssk.
        """
        
        self.mother_loops = mother_loops
        self.daughter_loops = daughter_loops
        self.name = name
        self.symbol = symbol
        
        if reverse is None: 
            self.reverse = self 
        else:
            self.reverse = reverse

        if mirror is None: 
            self.mirror = self
        else:
            self.mirror = mirror 

    def __repr__(self):
        return self.name


class StitchPattern(KnittingBase): 
    def __init__(self, pattern: List[Stitch], name=None):
        self.pattern = pattern 
        if name is None: 
            name = ''.join(str(self.pattern))

    def reverse(self, name=None): 
        return StitchPattern([stitch.reverse for stitch in reversed(self.pattern)], name)