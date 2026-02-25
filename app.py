import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

st.title("Voltage Prediction vs Height")

# -------------------------------
# Experimental data
# -------------------------------
height = np.array([10, 20, 30, 40, 50, 60, 70])  # cm

max_voltage_1200 = np.array([1.57, 2.09, 2.43, 2.76, 3.03, 3.23, 3.46])
min_voltage_1200 = np.array([-1.16, -1.78, -2.19, -2.54, -2.85, -3.06, -3.32])

max_voltage_600 = np.array([0.7, 0.93, 1.1, 1.25, 1.38, 1.5, 1.58])
min_voltage_600 = np.array([-0.52, -0.79, -0.99, -1.16, -1.31, -1.45, -1.52])

# -------------------------------
# Cubic spline interpolation
# -------------------------------
cs_max_1200 = CubicSpline(height, max_voltage_1200)
cs_min_1200 = CubicSpline(height, min_voltage_1200)
cs_max_600 = CubicSpline(height, max_voltage_600)
cs_min_600 = CubicSpline(height, min_voltage_600)

# -------------------------------
# User input
# -------------------------------
H_new = st.slider("Choose height (cm)", 10.0, 70.0, 30.0, 0.5)

# -------------------------------
# Predictions
# -------------------------------
V_spline_max_1200 = cs_max_1200(H_new)
V_spline_min_1200 = cs_min_1200(H_new)

V_spline_max_600 = cs_max_600(H_new)
V_spline_min_600 = cs_min_600(H_new)

st.subheader(f"Prediction for height {H_new} cm")

st.write(
    f"**1200 turns →** max {V_spline_max_1200:.2f} V, min {V_spline_min_1200:.2f} V"
)

st.write(
    f"**600 turns →** max {V_spline_max_600:.2f} V, min {V_spline_min_600:.2f} V"
)

# -------------------------------
# Plot
# -------------------------------
H_plot = np.linspace(10, 70, 200)

fig, ax = plt.subplots()

ax.plot(height, max_voltage_1200, "o", label="1200 max data")
ax.plot(height, min_voltage_1200, "o", label="1200 min data")
ax.plot(H_plot, cs_max_1200(H_plot), label="1200 max spline")
ax.plot(H_plot, cs_min_1200(H_plot), label="1200 min spline")

ax.plot(height, max_voltage_600, "s", label="600 max data")
ax.plot(height, min_voltage_600, "s", label="600 min data")
ax.plot(H_plot, cs_max_600(H_plot), label="600 max spline")
ax.plot(H_plot, cs_min_600(H_plot), label="600 min spline")

ax.set_xlabel("Height (cm)")
ax.set_ylabel("Voltage (V)")
ax.legend()

st.pyplot(fig)
