# Project Progress: DFT Convergence Study

## Completed Work

### Calculations
- [x] Baseline SCF calculation for Si (diamond cubic, ibrav=2)
- [x] Si k-point convergence study (Monkhorst-Pack grids: 2×2×2 through 12×12×12)
- [x] Si energy cutoff convergence study (ecutwfc: 20, 30, 40, 50, 60, 80, 100 Ry)
- [x] Generated Si charge density and ELF visualization files (XSF format)
- [x] Ge k-point convergence study (Monkhorst-Pack grids: 2×2×2 through 12×12×12)
- [x] Ge energy cutoff convergence study (ecutwfc: 20, 30, 40, 50, 60, 80, 100 Ry)
- [x] Generated Ge charge density and ELF visualization files (XSF format)

### Analysis & Documentation
- [x] Extracted total energies and computed ΔE (meV/atom) for all runs
- [x] Produced convergence plots (energy vs k-mesh, energy vs ecutwfc) for both materials
- [x] Exported results to CSV for reproducibility
- [x] Drafted full report with methods, results, tables, and discussion
- [x] Answered all three assignment questions (k-point comparison, cutoff comparison, ELF comparison)

## Remaining Work

### VESTA Visualizations
- [ ] Open `Si_rho.xsf` in VESTA and capture a screenshot of the Si crystal structure
- [ ] Open `Si_rho.xsf` in VESTA, add charge density isosurface, and capture a screenshot
- [ ] Open `Si_elf.xsf` in VESTA, add ELF isosurface (level = 0.75), and capture a screenshot
- [ ] Open `Ge_rho.xsf` in VESTA and capture a screenshot of the Ge crystal structure
- [ ] Open `Ge_rho.xsf` in VESTA, add charge density isosurface, and capture a screenshot
- [ ] Open `Ge_elf.xsf` in VESTA, add ELF isosurface (level = 0.75), and capture a screenshot

Isosurface path in VESTA: Objects > Volumetric Data > Isosurfaces > set level to 0.75 > OK

### Report Formatting
- [ ] Copy report text from `report/DFT_Convergence_Report.md` into a Word document
- [ ] Fill in student name and MIS number in the header
- [ ] Apply formatting: Times New Roman, body size 11–12, title size 14 bold, line spacing 1.15–1.5
- [ ] Set header layout: date (left), name (center), MIS number (right)
- [ ] Insert the 4 convergence plots at their marked locations
- [ ] Insert the 6 VESTA screenshots at their `[INSERT VESTA SCREENSHOT]` placeholders
- [ ] Review all tables, figure captions, and text for correctness
- [ ] Export final document as PDF for submission

## File Reference
| What | Where |
|------|-------|
| Report draft | `report/DFT_Convergence_Report.md` |
| Convergence plots | `plots/*.png` |
| Result data | `results/*.csv` |
| QE input/output | `Si/kpoints/`, `Si/cutoff/`, `Ge/kpoints/`, `Ge/cutoff/` |
| XSF files for VESTA | `Si/visualization/`, `Ge/visualization/` |
| Plotting script | `scripts/plot_convergence.py` |
