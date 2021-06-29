from Prover import exp_vector
from GlobalConfig import *
from FieldVector import *
from Proof import *

class Verifier:
    def __init__(self):
        self.proof = None


    def verify(self, proof, challenge):
        x = challenge.x
        y_vector = challenge.y
        z = challenge.z
        
        #compute commitment l(x) r(x) 
        second_exp = mul(y_vector, z) + mul(bin_vec, z*z)
        hh_vec = [h_vec[i]**(y_vector[i] **(-1)) for i in range(n)]
        minus_z = mul(uni_vec, -z)
        P = proof.A*(proof.S**x) *exp_vector(g_vec, minus_z)*exp_vector(hh_vec, second_exp)
        print("P = ", P)
        P_right = (h**proof.muy)*exp_vector(g_vec, proof.l)*exp_vector(hh_vec, proof.r) 
        print("PR = ", P_right)

        