from utils import *
import matplotlib.pyplot as plt

n0 = 3
N = 50000
m = 3


G1 = model_A(n0, N, m)


k, pk = get_pdf(G1)
plt.plot(k, pk, "ro")
plt.yscale("log")
plt.xlabel("$k$")
plt.ylabel("$p(k)$")
plt.show()