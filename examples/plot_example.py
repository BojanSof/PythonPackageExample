import numpy as np

from package_example.plot.plotter import plot_sine_from_bytes


if __name__ == '__main__':
    sine = (32768 * np.sin(
            2 * np.pi * 50 * np.linspace(0, 0.1, 100))
            + 32767).astype(np.uint16)
    sine_bytes = sine.tobytes()
    plot_sine_from_bytes(sine_bytes)
