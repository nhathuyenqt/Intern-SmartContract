from Proof import Challenge, Proof
from GlobalConfig import *
from FieldVector import *

def exp_vector(x, y):
    res = (x[0]**y[0])
    # print("x = ", x)
    for i in range(1, len(x)):
        # print("x = ", x[i], " \ny= ",group1.init(ZR, y[i]))
        # print("x = ", x[i], " \ny= ", y[i], type(y[i]))
        # res = res * (x[i]**group1.init(ZR, y[i]))
        res = res* (x[i]**y[i])
    return res



def inner_product(vec1, vec2):
    product = group1.init(ZR, 0)
    for i in range(n):
        product = product + vec1[i]*vec2[i]
    return product

def sigma(y, z):
    i1 = inner_product(uni_vec, y)
    i2 = inner_product(uni_vec, bin_vec)
    s = (z-z*z)*i1 - z*z*z*i2
    return s


class Prover:
    def __init__(self):
        self.v = 0
        # self.g = group1.random(G1)
        # self.h = group1.random(G1)
        # self.g_vec = [group1.random(G1) for i in range(n)]
        
        
        # self.g = group.randomGen()
        # self.h = group.randomGen()
        # self.g_vec = [group.randomGen() for i in range(n)]
        # self.h_vec = [group.randomGen() for i in range(n)]
        

    def cal_a_vector(self):
        a_L = [int(x) for x in np.binary_repr(self.v)]
        self.a_L = np.pad(a_L, (n-len(a_L), 0), 'constant')
        self.a_L = [int(x) for x in self.a_L]
        self.a_R = [x-1 for x in self.a_L]
        

    def commitment_for_vector(self, x0, x1, x2): 
        # P = h^x0*gvec^x1*hvec^x2
        c = (h**x0)* exp_vector(g_vec,x1)*exp_vector(h_vec,x2)
        # c = c[0]*c[1]
        
        return c
    
    def commitment_for_value(self, x0, x1): 
        # P = h^x0*gvec^x1*hvec^x2
        c = (g**x0)*(h**x1)
        # c = c[0]*c[1]
        
        return c

    def prove(self, _v, gama):
        self.v = _v
        self.cal_a_vector()
        self.a_L = [group1.init(ZR, x) for x in self.a_L]
        self.a_R = [group1.init(ZR, x) for x in self.a_R]

        alpha = group1.random(ZR)
        # print('alpha = ', alpha, type(alpha))
        self.A = self.commitment_for_vector(alpha, self.a_L, self.a_R)
        
        s_L = [group1.random(ZR) for i in range(n)]
        s_R = [group1.random(ZR) for i in range(n)]
        phi = group1.random(ZR)
        self.S = self.commitment_for_vector(phi, s_L, s_R)
        
        #Sent A, S to Prover // add A, S to Proof

        #Challenge Points y, z
        y = group1.random(ZR)
        z = group1.random(ZR)
        y_vec = [y**i for i in range(n)]

        tau1 = group1.random(ZR)
        tau2 = group1.random(ZR)
        
        sig = sigma(y_vec, z)
        print("sigma ", sig)

        
        t0 = z*z*self.v + sig
        z1 = mul(uni_vec, z)
        l0 = subtract(self.a_L, z1)
        l1 = s_L
        
        r0 = add( hadamard_product(y_vec, add(self.a_R, z1)), mul(bin_vec, z*z))
        r1 = hadamard_product(y_vec, s_R)

        t2 = inner_product(l1, r1)
        #t1 = <l0 + l1, r0 + r1> - t0 - t2
        t1 = inner_product(add(l0,l1), add(r0,r1)) - t0 - t2
        self.T1 = self.commitment_for_value(t1, tau1)
        self.T2 = self.commitment_for_value(t2, tau2)
        print('commitment T1 = ', self.T1)
        print('commitment T2 = ', self.T2)
        
        #Challenge Point x step 56
        x = group1.random(ZR)

        l  = l0 + mul(l1, x)
        r = r0 + mul(r1, x)
        
        #Send to V
        t = inner_product(l, r)
        taux = t2*x*x + t1*x + z*z*gama
        muy =  alpha + phi*x

        challenge  = Challenge()
        challenge.set(x, y_vec, z)

        proof = Proof()
        proof.set(taux, muy, t, l, r, self.A, self.S, self.T1, self.T2)
        return proof, challenge


