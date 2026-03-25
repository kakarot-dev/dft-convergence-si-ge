# TODO: Finalize DFT Convergence Report

## What's Already Done
- [x] Si baseline SCF calculation
- [x] Si k-point convergence study (k = 2, 4, 6, 8, 10, 12)
- [x] Si energy cutoff convergence study (ecutwfc = 20, 30, 40, 50, 60, 80, 100)
- [x] Si charge density and ELF XSF files generated
- [x] Ge k-point convergence study (k = 2, 4, 6, 8, 10, 12)
- [x] Ge energy cutoff convergence study (ecutwfc = 20, 30, 40, 50, 60, 80, 100)
- [x] Ge charge density and ELF XSF files generated
- [x] All convergence plots (4 PNGs in plots/)
- [x] All CSV result files (4 CSVs in results/)
- [x] Report draft with all text, tables, and Q&A (report/DFT_Convergence_Report.md)
- [x] All input/output files preserved

## What You Still Need To Do

### 1. Take VESTA Screenshots (6 total)
Open each XSF file from `C:\Users\kakar\Documents\` in VESTA:
- [ ] `Si_rho.xsf` — screenshot of Si crystal structure + charge density isosurface
- [ ] `Si_elf.xsf` — screenshot of Si ELF isosurface (set isolevel to 0.75)
- [ ] `Ge_rho.xsf` — screenshot of Ge crystal structure + charge density isosurface
- [ ] `Ge_elf.xsf` — screenshot of Ge ELF isosurface (set isolevel to 0.75)
- [ ] Si structure only (open any Si XSF, screenshot before adding isosurface)
- [ ] Ge structure only (open any Ge XSF, screenshot before adding isosurface)

To add isosurface: Objects > Volumetric Data > Isosurfaces > set level to 0.75 > OK

### 2. Create Word Document
- [ ] Open Word, create new document
- [ ] Copy text from `report/DFT_Convergence_Report.md` into Word
- [ ] Replace your name and MIS number at the top
- [ ] Format:
  - Font: Times New Roman
  - Body text: size 11 or 12
  - Section headers: bold
  - Title: size 14, bold
  - Line spacing: 1.15 or 1.5
  - Header: Date (left), Name (center), MIS No. (right)

### 3. Insert Images Into Word
Plots are in `C:\Users\kakar\Documents\`:
- [ ] `Si_kpoint_convergence.png` — after Si k-point table
- [ ] `Si_cutoff_convergence.png` — after Si cutoff table
- [ ] `Ge_kpoint_convergence.png` — after Ge k-point table
- [ ] `Ge_cutoff_convergence.png` — after Ge cutoff table
- [ ] Insert your 6 VESTA screenshots at the `[INSERT VESTA SCREENSHOT: ...]` placeholders

### 4. Final Review
- [ ] Make sure all tables are properly formatted
- [ ] Check that figure captions are below each image
- [ ] Verify name and MIS number are correct
- [ ] Save as PDF for submission

## File Locations
- Report text: `report/DFT_Convergence_Report.md`
- Plots: `plots/*.png` (also copied to `C:\Users\kakar\Documents\`)
- XSF files for VESTA: `C:\Users\kakar\Documents\` (Si_rho.xsf, Si_elf.xsf, Ge_rho.xsf, Ge_elf.xsf)
- All QE input files: `Si/kpoints/`, `Si/cutoff/`, `Ge/kpoints/`, `Ge/cutoff/`
- All QE output files: same directories as above
- CSV data: `results/`
