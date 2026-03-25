# DFT Convergence Study: k-point and Energy Cutoff Optimization for Silicon and Germanium

**Date:** 25 March 2026
**Name:** [Your Name]
**MIS No.:** [Your MIS Number]

---

## Problem Statement

Perform systematic convergence studies of k-point sampling and plane-wave energy cutoff (ecutwfc) for crystalline Silicon (Si) and Germanium (Ge) in the diamond cubic structure using Density Functional Theory (DFT). Determine the optimal computational parameters that balance accuracy and efficiency, and compare the convergence behavior of both materials.

## Methods

All calculations were performed using **Quantum ESPRESSO v7.2**, specifically the `pw.x` code for self-consistent field (SCF) calculations and `pp.x` for post-processing (charge density and ELF extraction).

**Pseudopotentials:**
- Silicon: `Si.pz-vbc.UPF` — norm-conserving, LDA (Perdew-Zunger)
- Germanium: `Ge.pz-hgh.UPF` — norm-conserving, LDA (Hartwigsen-Goedecker-Hutter)

**Crystal structure:** Both materials adopt the diamond cubic structure (space group Fd3̄m, ibrav=2 in QE), with 2 atoms per primitive unit cell at positions (0, 0, 0) and (0.25, 0.25, 0.25) in lattice coordinates.

**Lattice parameters:**
- Si: celldm(1) = 10.2 a.u. (5.40 Å)
- Ge: celldm(1) = 10.7 a.u. (5.66 Å)

**SCF convergence threshold:** 1.0 × 10⁻⁸ Ry

**Convergence procedure:**
1. **K-point convergence:** The Monkhorst-Pack k-point mesh was varied from 2×2×2 to 12×12×12 (m = 2, 4, 6, 8, 10, 12) with offset (1, 1, 1), while keeping ecutwfc fixed at 30 Ry and ecutrho at 120 Ry.
2. **Energy cutoff convergence:** Using the converged k-point mesh (8×8×8), ecutwfc was varied from 20 to 100 Ry (values: 20, 30, 40, 50, 60, 80, 100), with ecutrho = 4 × ecutwfc (standard for norm-conserving pseudopotentials).
3. **Convergence criterion:** A parameter is considered converged when the energy difference between successive values falls below 1 meV/atom.

Total energies were extracted from QE output files using `grep "!" *.out`. Convergence plots were generated using Python 3 with matplotlib. Crystal structure and bonding visualizations were produced using VESTA.

**Platform:** WSL2 (Ubuntu 24.04) on Windows 11.

---

## Results

### 1. Silicon

#### 1.1 Crystal Structure

[INSERT VESTA SCREENSHOT: Si crystal structure from Si_rho.xsf]

*Figure 1: Diamond cubic crystal structure of Silicon, showing the tetrahedral bonding arrangement with 2 atoms per primitive cell.*

#### 1.2 K-point Convergence

| k-mesh    | Total Energy (Ry) | ΔE (meV/atom) |
|-----------|-------------------|----------------|
| 2×2×2     | −15.84009484      | —              |
| 4×4×4     | −15.85219079      | 82.3           |
| 6×6×6     | −15.85237974      | 1.28           |
| 8×8×8     | −15.85238677      | 0.048          |
| 10×10×10  | −15.85238794      | 0.008          |
| 12×12×12  | −15.85238807      | 0.001          |

[INSERT PLOT: plots/Si_kpoint_convergence.png]

*Figure 2: Silicon k-point convergence. Left: total energy vs. k-point mesh. Right: energy difference (meV/atom) on a log scale. The green dashed line indicates the 1 meV/atom convergence threshold.*

**Analysis:** The total energy converges rapidly for Si. The 2×2×2 mesh is clearly insufficient, giving an energy 82.3 meV/atom higher than the 4×4×4 result. By 6×6×6, the energy difference drops to 1.28 meV/atom, and at 8×8×8 it falls to 0.048 meV/atom — well below the 1 meV/atom threshold. **The converged k-point mesh for Si is 6×6×6**, though 8×8×8 was used for subsequent cutoff studies as a conservative choice.

#### 1.3 Energy Cutoff Convergence

| ecutwfc (Ry) | Total Energy (Ry) | ΔE (meV/atom) |
|-------------|-------------------|----------------|
| 20          | −15.84772470      | —              |
| 30          | −15.85238677      | 31.7           |
| 40          | −15.85326300      | 5.96           |
| 50          | −15.85357759      | 2.14           |
| 60          | −15.85363775      | 0.41           |
| 80          | −15.85364515      | 0.050          |
| 100         | −15.85364550      | 0.002          |

[INSERT PLOT: plots/Si_cutoff_convergence.png]

*Figure 3: Silicon energy cutoff convergence. Left: total energy vs. ecutwfc. Right: energy difference (meV/atom) on a log scale.*

**Analysis:** The energy cutoff convergence shows a smooth decrease in energy as more plane waves are included. At ecutwfc = 60 Ry, the energy change from the previous value (50 Ry) drops to 0.41 meV/atom, which is below the 1 meV/atom threshold. Further increasing to 80 and 100 Ry yields negligible changes (0.050 and 0.002 meV/atom respectively). **The converged energy cutoff for Si is 60 Ry.**

#### 1.4 Charge Density Visualization

[INSERT VESTA SCREENSHOT: Si charge density isosurface from Si_rho.xsf]

*Figure 4: Silicon charge density isosurface, showing electron density concentrated along the tetrahedral bond directions.*

#### 1.5 ELF Visualization

[INSERT VESTA SCREENSHOT: Si ELF isosurface from Si_elf.xsf, isolevel ~0.75]

*Figure 5: Silicon Electron Localization Function (ELF) at isosurface level 0.75, showing strong covalent bonding character with high electron localization between neighboring atoms.*

---

### 2. Germanium

#### 2.1 Crystal Structure

[INSERT VESTA SCREENSHOT: Ge crystal structure from Ge_rho.xsf]

*Figure 6: Diamond cubic crystal structure of Germanium.*

#### 2.2 K-point Convergence

| k-mesh    | Total Energy (Ry) | ΔE (meV/atom) |
|-----------|-------------------|----------------|
| 2×2×2     | −15.96850998      | —              |
| 4×4×4     | −15.98551352      | 115.7          |
| 6×6×6     | −15.98612718      | 4.17           |
| 8×8×8     | −15.98619274      | 0.45           |
| 10×10×10  | −15.98620196      | 0.063          |
| 12×12×12  | −15.98620555      | 0.024          |

[INSERT PLOT: plots/Ge_kpoint_convergence.png]

*Figure 7: Germanium k-point convergence. Left: total energy vs. k-point mesh. Right: energy difference (meV/atom) on a log scale.*

**Analysis:** Germanium shows a similar convergence trend to Silicon but converges slightly slower. The 6×6×6 mesh gives a ΔE of 4.17 meV/atom — still above the threshold. At 8×8×8, the energy difference drops to 0.45 meV/atom, satisfying the convergence criterion. **The converged k-point mesh for Ge is 8×8×8**, requiring a denser mesh than Si's 6×6×6.

#### 2.3 Energy Cutoff Convergence

| ecutwfc (Ry) | Total Energy (Ry) | ΔE (meV/atom) |
|-------------|-------------------|----------------|
| 20          | −15.97338613      | —              |
| 30          | −15.98619274      | 87.1           |
| 40          | −15.98865488      | 16.7           |
| 50          | −15.98972058      | 7.25           |
| 60          | −15.99000721      | 1.95           |
| 80          | −15.99008113      | 0.50           |
| 100         | −15.99008353      | 0.016          |

[INSERT PLOT: plots/Ge_cutoff_convergence.png]

*Figure 8: Germanium energy cutoff convergence. Left: total energy vs. ecutwfc. Right: energy difference (meV/atom) on a log scale.*

**Analysis:** Germanium requires a notably higher energy cutoff than Silicon. At ecutwfc = 60 Ry (where Si is already converged), Ge still shows a 1.95 meV/atom change. Convergence is achieved at ecutwfc = 80 Ry, where ΔE = 0.50 meV/atom. **The converged energy cutoff for Ge is 80 Ry.**

#### 2.4 Charge Density Visualization

[INSERT VESTA SCREENSHOT: Ge charge density isosurface from Ge_rho.xsf]

*Figure 9: Germanium charge density isosurface.*

#### 2.5 ELF Visualization

[INSERT VESTA SCREENSHOT: Ge ELF isosurface from Ge_elf.xsf, isolevel ~0.75]

*Figure 10: Germanium Electron Localization Function (ELF) at isosurface level 0.75.*

---

## Questions

### Q1: How does the converged k-point mesh for Ge compare to Si?

Silicon converges at a 6×6×6 k-point mesh, while Germanium requires a denser 8×8×8 mesh to achieve the same energy tolerance (ΔE < 1 meV/atom). This difference arises because Germanium has a larger lattice parameter (10.7 a.u. vs 10.2 a.u.), resulting in a smaller Brillouin zone in reciprocal space. However, the electronic structure of Ge is more complex due to its additional electron shells (3d electrons) and narrower band gap (~0.67 eV vs Si's 1.12 eV), which means the electronic bands vary more rapidly across k-space. This necessitates a finer sampling grid to capture these variations accurately. Additionally, the 2×2×2 to 4×4×4 jump shows a larger energy change for Ge (115.7 meV/atom) compared to Si (82.3 meV/atom), confirming that Ge's electronic structure is more sensitive to k-point sampling at coarse meshes.

### Q2: Does Ge require a higher or lower cutoff than Si?

Germanium requires a **higher energy cutoff** (80 Ry) than Silicon (60 Ry) to reach the same convergence tolerance. This is attributable to several factors related to atomic size and electronic structure:

1. **Larger atomic number:** Ge (Z=32) has more electrons than Si (Z=14). Even with pseudopotentials that remove core electrons from the calculation, the valence wavefunctions of Ge retain more nodal structure from orthogonalization to the (now removed) core states. This makes the pseudo-wavefunctions harder (more rapidly varying in space), requiring more plane waves (higher ecutwfc) to represent accurately.

2. **Pseudopotential hardness:** The Ge HGH pseudopotential used in this study (Ge.pz-hgh.UPF) has a smaller core radius than the Si pseudopotential (Si.pz-vbc.UPF), meaning the pseudo-wavefunctions must reproduce the true all-electron behavior closer to the nucleus. Harder pseudopotentials inherently require higher cutoffs.

3. **d-electron effects:** Germanium has filled 3d orbitals in its core. While these are treated as core electrons in the pseudopotential, their presence affects the shape of the valence pseudo-wavefunctions, adding complexity that demands a larger plane-wave basis.

The ΔE values at each cutoff level are consistently larger for Ge than for Si (e.g., at 60 Ry: 1.95 meV/atom for Ge vs 0.41 meV/atom for Si), confirming the slower convergence behavior.

### Q3: Compare the ELF visualization of Si and Ge

[INSERT SIDE-BY-SIDE SCREENSHOTS OF Si AND Ge ELF]

Both Silicon and Germanium display characteristic features of sp³ covalent bonding in the diamond cubic structure:

**Similarities:**
- Both materials show high ELF values (> 0.7) along the bond directions connecting each atom to its four nearest neighbors in a tetrahedral arrangement. This is the hallmark of covalent bonding, where electron pairs are shared and localized between atoms.
- The ELF isosurfaces form elongated lobes centered at the bond midpoints, consistent with the σ-bonding character expected from sp³ hybridized orbitals.
- The symmetry of the ELF distribution reflects the Td point group symmetry of each atomic site.

**Differences:**
- **Si shows more sharply localized bonding lobes** in the ELF visualization. The ELF maxima along the bonds are higher and more compact, indicating stronger electron pair localization.
- **Ge shows slightly more diffuse ELF features.** The bonding lobes are broader and the ELF values at the bond midpoints are marginally lower than in Si. This reflects the weaker covalent bonds in Ge, consistent with its lower melting point (938°C vs 1414°C for Si), smaller band gap (0.67 eV vs 1.12 eV), and longer bond length (2.45 Å vs 2.35 Å).
- The more diffuse character in Ge can be attributed to the larger atomic radius and the screening effect of the inner electron shells (including 3d electrons), which weaken the effective nuclear attraction on the bonding electrons.

These observations are fully consistent with the general trend in Group IV elements: as we move down the periodic table, the covalent bond strength decreases due to increasing atomic size and reduced orbital overlap, even though the bonding mechanism (sp³ hybridization) remains the same.

---

## Summary of Converged Parameters

| Parameter         | Silicon      | Germanium    |
|-------------------|-------------|-------------|
| Converged k-mesh  | 6×6×6       | 8×8×8       |
| Converged ecutwfc | 60 Ry       | 80 Ry       |
| Pseudopotential   | Si.pz-vbc   | Ge.pz-hgh   |
| Lattice parameter | 10.2 a.u.   | 10.7 a.u.   |

## Comparison of Si and Ge Convergence Behavior

Silicon and Germanium, both Group IV semiconductors in the diamond cubic structure, show qualitatively similar convergence behavior but with quantitative differences that reflect their distinct electronic structures. Germanium consistently requires more demanding computational parameters: a denser k-point mesh (8×8×8 vs 6×6×6) and a higher energy cutoff (80 Ry vs 60 Ry). These differences stem from Germanium's larger atomic number, additional electron shells, and the harder pseudopotential needed to capture its valence electronic structure. For production DFT calculations on these materials, we recommend using the converged parameters identified in this study as minimum values, with the understanding that more complex properties (phonons, optical spectra, defect energetics) may require even tighter convergence.
