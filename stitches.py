from classes import *

# some standard stitches
knit = Stitch('k', u'|', 1, 1)
purl = Stitch('p', u'-', 1, 1, knit)
knit.reverse = purl 

# functions to create common stitch patterns 
def knpn(k: int, p: int):
    return StitchPattern([*[knit]*k, *[purl]*p], name=f'k{k}p{p}')