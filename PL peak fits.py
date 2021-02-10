import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pandas as pd

# Dados MoS2
pl1 = pd.read_table('pl_mos2.txt')
pl1['energy'] = 1239.8/pl1['wavelength']

# Dados WS2
pl2 = pd.read_table('pl_ws2.txt')
pl2['energy'] = 1239.8/pl2['wavelength']

# Função Lorentziana para ajuste
def lorentzian(x, amp1, cen1, wid1):
    return (amp1*wid1**2/((x-cen1)**2+wid1**2))


def lorentzian_off(x, off, amp1, cen1, wid1):
    return off + (amp1*wid1**2/((x-cen1)**2+wid1**2))

# Ajuste MoS2
p01 = np.array([200, 600, 1.84, 0.1])
pars1, cov1 = curve_fit(lorentzian_off, pl1.energy, pl1.intensity, p01)
print(pars1)

x1 = np.linspace(min(pl1.energy), max(pl1.energy), 10000)
y1 = lorentzian_off(x1, pars1[0], pars1[1], pars1[2], pars1[3])
#y_exp = lorentzian(x1, 567, 1.84, 0.04) # Ajuste com esses parâmetros funciona muito bem!

# Ajuste WS2
p02 = np.array([18000, 1.95, 0.5])
pars2, cov2 = curve_fit(lorentzian, pl2.energy, pl2.intensity, p02)
print(pars2)

x2 = np.linspace(min(pl2.energy), max(pl2.energy), 10000)
y2 = lorentzian(x2, pars2[0], pars2[1], pars2[2])


# Plot MoS2
fig1 = plt.plot(pl1.energy, pl1.intensity, 'k', label='MoS$_2$')
plt.xlabel('Energia (eV)', fontname='Arial', fontsize=16)
plt.ylabel('Intensidade (u.a.)', fontname='Arial', fontsize=16)
plt.plot(x1, y1, 'r--', label='Ajuste lorentziano')
plt.legend()
plt.savefig('MoS2 PL fit.png', dpi=300, bbox_inches='tight')
plt.show()

# Plot WS2
fig2 = plt.plot(pl2.energy, pl2.intensity, 'b', label='WS$_2$')
plt.xlabel('Energia (eV)', fontname='Arial', fontsize=16)
plt.ylabel('Intensidade (u.a.)', fontname='Arial', fontsize=16)
plt.plot(x2, y2, 'r:', label='Ajuste lorentziano')
plt.xlim(1.5, 2.3)
plt.legend()
plt.savefig('WS2 PL fit.png', dpi=300, bbox_inches='tight')
plt.show()
