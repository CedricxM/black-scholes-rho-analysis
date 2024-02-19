import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def black_scholes_rho(S, K, T, r, q, sigma):
    d2 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    return rho

# Question 2: Variation de Rho en fonction de la valeur du spot S
K = 1.1432
r = 0.0260  # 2.60%
q = -0.0031  # -0.31%
T = 0.25  # 3 mois
sigma = 0.0616  # 6.16%

S_values = np.linspace(1.1, 1.2, 100)
rho_values = [black_scholes_rho(S, K, T, r, q, sigma) for S in S_values]

plt.figure(figsize=(8, 6))
plt.plot(S_values, rho_values, label='Rho en fonction de S')
plt.title('Variation de Rho en fonction de la valeur du spot S')
plt.xlabel('Spot (S)')
plt.ylabel('Rho')
plt.legend()
plt.grid(True)
plt.show()

# Question 3: Variation de Rho en fonction de la maturité T pour les cas ATM, ITM et OTM
S_atm = 1.1432
S_itm = 1.1750
S_otm = 1.1150

T_values = np.linspace(0.01, 1, 100)
rho_atm_values = [black_scholes_rho(S_atm, K, T, r, q, sigma) for T in T_values]
rho_itm_values = [black_scholes_rho(S_itm, K, T, r, q, sigma) for T in T_values]
rho_otm_values = [black_scholes_rho(S_otm, K, T, r, q, sigma) for T in T_values]

plt.figure(figsize=(8, 6))
plt.plot(T_values, rho_atm_values, label='ATM')
plt.plot(T_values, rho_itm_values, label='ITM')
plt.plot(T_values, rho_otm_values, label='OTM')
plt.title('Variation de Rho en fonction de la maturité T')
plt.xlabel('Maturité (T)')
plt.ylabel('Rho')
plt.legend()
plt.grid(True)
plt.show()


