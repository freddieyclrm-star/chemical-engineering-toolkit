# 📘 ROADMAP.md (v0.1.1 → v0.2.0)  
## Overview  
This roadmap outlines the planned development path for the Chemical Engineering Toolkit from v0.1.1 (Quality Release) through v0.2.0 (Feature Expansion).  
The goal is to strengthen code quality, engineering correctness, documentation, and testing before introducing new calculators or modules.  

## v0.1.1 — Quality & Stability Release  
Theme: Professionalise the foundation before adding new engineering features.  
Estimated Duration: 2–3 weeks  
Difficulty: Medium (5/10)  
  
### Phase 1 — Code Quality  
- Add type hints across all modules  

- Add consistent docstrings (NumPy/SciPy style)  

- Apply Black formatting  

- Run Ruff/Flake8 and resolve issues  

- Remove unused imports and dead code  

### Phase 2 — Engineering Quality  
- Add engineering assumptions for each calculator  

- Add references for constants (CODATA, CRC Handbook, etc.)  

- Verify unit consistency across modules  

- Improve error messages for engineering inputs  

### Phase 3 — Testing  
- Add invalid input tests (negative values, invalid units, strings, empty input)  

- Add regression tests for any bugs found  

- Increase test coverage  

- Ensure tests pass in a clean environment  

### Phase 4 — CLI & UX Improvements  
- Improve menu formatting and spacing  

- Improve invalid input handling  

- Standardise prompts and output formatting  

- Optional: add colour and screen‑clearing  

### Phase 5 — Documentation  
- Expand README with screenshots, examples, and project tree  

- Standardise module documentation  

- Add assumptions, equations, references, examples for each calculator  

- Update CHANGELOG  

- Review installation instructions from a fresh clone  

### Release Engineering  
- Configure GitHub Actions to run pytest automatically  

- Add README status badges (optional)  

- Tag and publish v0.1.1  

- Write concise release notes summarising quality improvements  

## Stretch Goals (Optional)  
- Pre‑commit hooks (Black + Ruff)  

- Additional CLI polish  

- Automated formatting checks  

- More detailed engineering references  