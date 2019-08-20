import numpy as np 
import matplotlib.pyplot as plt 

#===============================================================
# FELDGLEICHUNG

# Raster
X,Y,Z = np.meshgrid(np.arange(-10,10,1), np.arange(-10,10,1), np.arange(-10,10,1))

# Ort
#x = 20
#y = 1
#Z = 20
r_v = np.asarray([X,Y,Z])
r = np.sqrt(X**2 + Y**2 + Z**2)

# Konstanten
OMEG = 2    # Schwingungen
C = 3       # LiChtgesChwindigkeit
E = 1.6     # elektisChe Feldkonstante
A = 100     # Amplitude
t = 0       # Zeit


# Dipolmoment in z-Richtung (zeitliche Ableitungen)
#e_vec = np.asarray([0,0,1]) 
p1 = (-A * E * np.sin(OMEG * (t-(r/C))))[0][0]
#print(p1)
#print(p1.shape)
p2 = (-A * E * np.cos(OMEG * (t-(r/C))) * OMEG)[0][0]
p3 = ( A * E * np.sin(OMEG * (t-(r/C))) * OMEG**2)[0][0]

# Elektrische Feldgleichung
def E_Feld():
    return ((p3 / ((C**2) * r)) 
         - (p2 / (C * (r**2))) 
         + ((3 * np.dot(p2, r_v) * r_v) / (C * (r**4)))
         + ((3 * np.dot(p3, r_v) * r_v) / ((C**2) * r**4))
         + ((3 * np.dot(p1, r_v) * r_v) / r**3)
         - (p1/(r**3)))

#print(p1.shape)
#print(r_v.shape)
#print(np.dot(p1,r_v).shape)
#print(((3 * np.dot(p1, r_v)).shape)

print(E_Feld()[0])

#===============================================================
# DYNAMIK DES FELDES


#===============================================================
# ANIMIERTER PLOT
"""
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")

# Definition des Feldes im Raster
Ex = E_Feld()[0]
Ey = E_Feld()[1]
Ez = E_Feld()[2]

# Zeige das Feld
fig = plt.figure(figsize=(7,7), dpi=300)
fig.patch.set_facecolor('white')
#plt.xticks([])
#plt.yticks([])

# White borders
#plt.plot(x, z, "o", color = (1,1,1,1), zorder=40, markersize=40)
#plt.plot(-x, z, "o",color = (1,1,1,1), zorder=40, markersize=40)
# Zeige die Ladungen
#plt.plot(x, z, "o", color = (0.3, 0.5, 0.8,1), zorder=60, markersize=15)
#plt.plot(-x, z, "o",color = (1,0.5,0.5,1), zorder=60, markersize=15)

# Plotte alles zu zeigende
#plt.streamplot(X,Z,Ex,Ey, color = (0,0,0.2,1))

#plt.show()
"""