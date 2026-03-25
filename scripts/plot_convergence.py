#!/usr/bin/env python3
"""
Generate convergence plots for Si and Ge DFT calculations.
Produces:
  1. Si k-point convergence
  2. Si energy cutoff convergence
  3. Ge k-point convergence
  4. Ge energy cutoff convergence
"""

import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

RESULTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'results')
PLOTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'plots')
os.makedirs(PLOTS_DIR, exist_ok=True)

# Conversion: 1 Ry = 13605.693 meV
RY_TO_MEV = 13605.693

def read_csv(filename):
    path = os.path.join(RESULTS_DIR, filename)
    x, y = [], []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            keys = list(row.keys())
            x.append(float(row[keys[0]]))
            y.append(float(row[keys[1]]))
    return np.array(x), np.array(y)


def plot_convergence(x, y, xlabel, ylabel, title, filename, threshold_mev=1.0):
    """Plot energy convergence with a threshold line."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Left: Total energy vs parameter
    ax1.plot(x, y, 'o-', color='#2563eb', linewidth=2, markersize=8)
    ax1.set_xlabel(xlabel, fontsize=12)
    ax1.set_ylabel('Total Energy (Ry)', fontsize=12)
    ax1.set_title(f'{title} — Total Energy', fontsize=13, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.ticklabel_format(useOffset=False)

    # Right: Energy difference (meV/atom) vs parameter
    # 2 atoms per cell
    delta_E = np.abs(np.diff(y)) * RY_TO_MEV / 2.0
    x_mid = x[1:]
    ax2.plot(x_mid, delta_E, 's-', color='#dc2626', linewidth=2, markersize=8)
    ax2.axhline(y=threshold_mev, color='#16a34a', linestyle='--', linewidth=1.5,
                label=f'Threshold ({threshold_mev} meV/atom)')
    ax2.set_xlabel(xlabel, fontsize=12)
    ax2.set_ylabel('ΔE (meV/atom)', fontsize=12)
    ax2.set_title(f'{title} — Energy Difference', fontsize=13, fontweight='bold')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=10)

    plt.tight_layout()
    outpath = os.path.join(PLOTS_DIR, filename)
    plt.savefig(outpath, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'Saved: {outpath}')


# --- Si k-point convergence ---
x, y = read_csv('Si_kpoint_convergence.csv')
plot_convergence(x, y, 'k-point mesh (m×m×m)', 'Total Energy (Ry)',
                 'Silicon — k-point Convergence', 'Si_kpoint_convergence.png')

# --- Si cutoff convergence ---
x, y = read_csv('Si_cutoff_convergence.csv')
plot_convergence(x, y, 'ecutwfc (Ry)', 'Total Energy (Ry)',
                 'Silicon — Energy Cutoff Convergence', 'Si_cutoff_convergence.png')

# --- Ge k-point convergence ---
x, y = read_csv('Ge_kpoint_convergence.csv')
plot_convergence(x, y, 'k-point mesh (m×m×m)', 'Total Energy (Ry)',
                 'Germanium — k-point Convergence', 'Ge_kpoint_convergence.png')

# --- Ge cutoff convergence ---
x, y = read_csv('Ge_cutoff_convergence.csv')
plot_convergence(x, y, 'ecutwfc (Ry)', 'Total Energy (Ry)',
                 'Germanium — Energy Cutoff Convergence', 'Ge_cutoff_convergence.png')

print('\nAll plots generated successfully!')
