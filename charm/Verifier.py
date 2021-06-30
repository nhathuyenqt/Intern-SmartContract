from Prover import exp_vector
from GlobalConfig import *
from FieldVector import *
from Proof import *

class Verifier:
    def __init__(self):
        self.proof = None


    def verify(self, proof, challenge):
        x = challenge.x
        y = challenge.y
        z = challenge.z
        y_vector = [y**i for i in range(n)]
        #compute commitment l(x) r(x) 
        
        # h_ary = exp_vector(hh_vec, hadamard_product(self.a_R))
        print("-------------")
        # print(h_vec[1])
        # print(hh_vec[1])
        minus_z = mul(uni_vec, -z)

        print("-------------")
        print("Condition 65 : Check t_hat ==? t(x) :")
        gthx = (g**proof.t) * (h**proof.taux)
        gthxV = (proof.V**z*z) * (g**proof.sigma) * proof.T1**x * (proof.T2**(x*x))
        # print("gthx = ", gthx)
        # print("gthxV = ", gthxV)
        if (gthx == gthxV):
            print("True")
        else:
            print("False")

        print("-------------")
        print("Condition 67 : Check l and r \n")
        second_exp = add(mul(y_vector, z), mul(bin_vec, z*z))
        hh_vec = [h_vec[i]**((y **(-1))**i) for i in range(n)]
        P = proof.A*(proof.S**x) *exp_vector(g_vec, minus_z)*exp_vector(hh_vec, second_exp)
        print("P = ", P)
        P_right = (h**proof.muy)*exp_vector(g_vec, proof.l)*exp_vector(hh_vec, proof.r) 
        print("PR = ", P_right)
        if (P == P_right):
            print("True")
        else:
            print("False")


        