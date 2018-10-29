# Theoretische Physik 1, Blatt 1
# Quentin Wach, 17. Oktober 2018
"""
TODO:	- Interaktivität: Live Parameterveränderung
"""

import matplotlib.pyplot as plt
import numpy as np
import math

### Plotdesign ###
plt.style.use('seaborn')


### Bahnkurve ###
# Parameter
t_res = 0.001 # Zeitauflösung
t_max = 2.2 # Zeitendpunkt in s
t = np.arange(0., t_max, t_res) # Zeitintervall
v_0 = 20 # Anfangsgeschwindigkeit in m/s
g = 9.81 # Erdbeschleunigung in m/s²
phi = 60 # Wurfwinkel in °
# [0,90]°, 0° --> hoch, 90° --> weit, 45° --> ideal

# x-Koordinate
distance_over_time = v_0 * t * math.sin(math.radians(phi))
# y-Koordinate
height_over_time = v_0 * t * math.cos(math.radians(phi)) - (1/2) * g * (t ** 2)

# Plotte die Wurfparabel (x = Weite, y = Höhe)
bahnkurve = plt.plot(distance_over_time, height_over_time, color = (0, 0, 0, 1),label='Bahnkurve', zorder=1)


### Vektoren ###
# Skalierung
scale = 0.1

# Zeitabstände der Vektoren auf der Kurve in s
time_step = 0.2 

# Geschwindigkeitsvektor im Zeitverlauf
speed_distance = v_0 * math.sin(math.radians(phi))
speed_height = (v_0 * math.cos(math.radians(phi))) - (g * t)
speed_vecs = []

# Beschleunigungsvektor im Zeitverlauf
acc_height = -g
acc_vecs = []

# Finde die Geschwindigkeits- und Beschleunigungsvektoren in 0.2s Abständen
for step in range(int(t[-1] // time_step) + 1):
	# Zeitpunkt
	t = step * time_step

	# Vektorursprung zum Zeitpunkt
	origin = [distance_over_time, height_over_time]
	np.asarray(origin)
	x_origin = [origin[0][int(t // t_res)]]
	y_origin = [origin[1][int(t // t_res)]]

	# Erstelle die Geschwindigkeitsvektoren
	plt.quiver(x_origin, y_origin, [speed_distance], [speed_height[int(t // t_res)]], 
		color =(0.10, 0.50, 0.60, 0.7), angles='xy', scale_units='xy', scale=1//scale, zorder=10,
		headwidth=5, headlength=4.45, width=0.005) #5, 4.45

	# Erstelle die Beschleunigungsvektoren
	plt.quiver(x_origin, y_origin, [0], [acc_height], 
		color = (1, 0.50, 0.50, 0.9), angles='xy', scale_units='xy', scale=1//scale, zorder=3,
		headwidth=5, headlength=4.45, width=0.005)

	# Erstelle Ursprungspunkte
	plt.plot(x_origin, y_origin, "o",color = (0,0,0,1), zorder=60)


### Beschriftung ###
plt.xlabel("Weite in Metern")
plt.ylabel("Höhe in Metern")

plt.show()
