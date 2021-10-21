import numpy as np

p_ksi = np.array([0.37, 0.02, 0.21, 0.40]) # ОПЕЧАТКА!!!
p_eta = np.array([0.17, 0.23, 0.33, 0.27])

E = np.array([[1, 1, 1, 1], [1, 1j, -1, -1j], [1, -1, 1, -1], [1, -1j, -1, 1j]])

phi_ksi = E.dot(p_ksi)
phi_eta = E.dot(p_eta)

E_inv = np.linalg.inv(E)

phi_ksi_plus_eta = phi_eta * phi_ksi

print(E_inv.dot(phi_ksi_plus_eta))
