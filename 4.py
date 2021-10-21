import numpy as np

p_ksi = np.array([0.45, 0.34, 0.21])
assert np.sum(p_ksi) == 1

N = 3
x = np.r_[0:N - 1:N * 1j]
y = np.r_[0:N - 1:N * 1j]

X, Y = np.meshgrid(x, y)
E = np.exp(2j * np.pi * X * Y / N)

phi_ksi = E.dot(p_ksi)

phi_eta = phi_ksi
n = 1
while (np.linalg.norm(phi_eta) ** 2 - 1 > 0.01):
    phi_eta *= phi_ksi
    n += 1

print(n)
