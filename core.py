import numpy as np
from numpy import array
import random

def dist(p1,p2):
    return np.linalg.norm(p1-p2)

class Body:
    def __init__(self,
                pos=array((0.0,0.0)),
                vel=array((0.0,0.0)),
                mass=1
            ):
        self.pos,self.vel=array(pos,dtype=np.float),array(vel,dtype=np.float)
        self.force=array((0.0,0.0))
        self.mass=mass
    def __repr__(self):
        return "Body(pos=%s,vel=%s,mass=%s)"%(str(self.pos),str(self.vel),str(self.mass))

class Force:
    def get_force(self,body):
        force=array((0.0,0.0))
        #Do something...
        return force

class Space:
    def __init__(self):
        self.bodies=[]
        self.forces=[]
    def add_force(self,force):
        self.forces.append(force)
    def add_body(self,body):
        self.bodies.append(body)
    def force_process(self):
        for body in self.bodies:
            resultant_force=[]
            for force in self.forces:
                resultant_force.append(force.get_force(body))
            body.force=sum(resultant_force)
    def motion_process(self,tick_len):
        for body in self.bodies:
            acl=body.force/body.mass
            body.vel+=acl*tick_len
            body.pos+=body.vel*tick_len
    def collision_process(self):
        for body in self.bodies:
            if body.pos[0]<-100 or body.pos[0]>100:
                body.vel[0]*=-1
            if body.pos[1]<-100 or body.pos[1]>100:
                body.vel[1]*=-1
    def process(self,tick_len):
        self.force_process()
        self.motion_process(tick_len)
        self.collision_process()