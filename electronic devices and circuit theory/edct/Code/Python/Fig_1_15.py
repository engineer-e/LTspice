import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Physical constants
k = 1.380649e-23
q = 1.60217663e-19

# Initial parameters
Is_init = 1e-11
n_init = 1.5
Rb_init = 5
T_init = 25  # Celsius

# Voltage sweep
V = np.linspace(-1.5, 1.5, 1000)

def diode_current_real(Vapp, Is, n, Rb, T):
    T = T + 273.15
    Vt = k * T / q

    Vd = Vapp.copy()

    # Newton-Raphson solve for diode internal voltage
    for _ in range(20):
        I = Is * (np.exp(Vd / (n * Vt)) - 1)
        f = Vd + I * Rb - Vapp
        df = 1 + (Is / (n * Vt)) * np.exp(Vd / (n * Vt)) * Rb
        Vd = Vd - f / df

    return Is * (np.exp(Vd / (n * Vt)) - 1)


def diode_current_ideal(V, Is, n, T):
    T = T + 273.15
    Vt = k * T / q
    return Is * (np.exp(V / (n * Vt)) - 1)


# Initial curves
I_real = diode_current_real(V, Is_init, n_init, Rb_init, T_init)
I_ideal = diode_current_ideal(V, Is_init, n_init, T_init)

# Figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

line_real, = ax.plot(V, I_real * 1e3, label="Real (with Rb)", color="cyan", linewidth=2)
line_ideal, = ax.plot(V, I_ideal * 1e3, label="Ideal diode", linestyle="--", color="gray")

ax.set_title("Diode I–V Characteristic Simulator")
ax.set_xlabel("Voltage Vd (V)")
ax.set_ylabel("Current (mA)")
ax.grid(True)
ax.legend()

# Sliders
ax_Is = plt.axes([0.15, 0.25, 0.65, 0.03])
ax_n  = plt.axes([0.15, 0.20, 0.65, 0.03])
ax_Rb = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_T  = plt.axes([0.15, 0.10, 0.65, 0.03])

s_Is = Slider(ax_Is, "Is", 1e-13, 1e-8, valinit=Is_init, valfmt="%.1e")
s_n  = Slider(ax_n,  "n", 1.0, 2.0, valinit=n_init)
s_Rb = Slider(ax_Rb, "Rb", 0.0, 25.0, valinit=Rb_init)
s_T  = Slider(ax_T,  "Temp (°C)", -75, 125, valinit=T_init)


def update(val):
    Is = s_Is.val
    n = s_n.val
    Rb = s_Rb.val
    T = s_T.val

    I_real = diode_current_real(V, Is, n, Rb, T)
    I_ideal = diode_current_ideal(V, Is, n, T)

    line_real.set_ydata(I_real * 1e3)
    line_ideal.set_ydata(I_ideal * 1e3)

    fig.canvas.draw_idle()


s_Is.on_changed(update)
s_n.on_changed(update)
s_Rb.on_changed(update)
s_T.on_changed(update)


# Hover readout (like your HUD)
annot = ax.annotate("", xy=(0,0), xytext=(20,20),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="black", alpha=0.7),
                    color="white")

annot.set_visible(False)


def on_move(event):
    if event.inaxes == ax and event.xdata is not None:
        Vd = event.xdata

        Is = s_Is.val
        n = s_n.val
        Rb = s_Rb.val
        T = s_T.val

        I = diode_current_real(np.array([Vd]), Is, n, Rb, T)[0] * 1e3

        annot.xy = (Vd, I)
        annot.set_text(f"Vd={Vd:.3f} V\nId={I:.3e} mA")
        annot.set_visible(True)
        fig.canvas.draw_idle()
    else:
        annot.set_visible(False)
        fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", on_move)

plt.show()