import numpy as np
from numpy import array

import core

GRAVITY_CONST=6.67*(10**-11)
GRAVITY_ACCELERATION=-10

class Gravity(core.Force):
    def get_force(self,body):
        force=array((0,body.mass*GRAVITY_ACCELERATION))
        return force

class Attraction(core.Force):
    def __init__(self,bind_body):
        self.bind_body=bind_body
    def get_force(self,body):
        r=core.dist(self.bind_body.pos,body.pos)
        if r==0:
            return array((0.0,0.0))
        force_len=(self.bind_body.mass*body.mass*GRAVITY_CONST)/(r**2)
        force=(self.bind_body.pos-body.pos)*(force_len/r)
        return force