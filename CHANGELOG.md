# Changelog  
  
## v0.1.0 — 29/07/2026  
Foundation release establishing the core architecture and CLI tools.  
  
### Added  
- CLI menu system  
- Application entry point  
- Unit converter (length, temperature, mass, speed, volume, time, area, pressure, energy)  
- Scientific constants module  
- Engineering constants module  
- Mass balance calculator with CLI integration  
- Energy balance calculator with CLI integration  
- Input validation utilities  
- Formatting utilities (sections, labels, results, success/error messages)  
- Basic pytest suite  
- README documentation  
- MIT License  
  
### Changed  
- NA  
  
### Fixed  
- NA  
  
### Removed  
- NA  

## v0.1.1 — Planned
Quality & stability release focused on improving the foundation before adding new engineering features.

### Planned — Code Quality
- Add type hints across all modules
- Add consistent docstrings (NumPy/SciPy style)
- Apply Black formatting
- Run Ruff/Flake8 and resolve issues
- Remove unused imports and dead code

### Planned — Engineering Quality
- Add engineering assumptions for each calculator
- Add references for constants (CODATA, CRC Handbook, etc.)
- Verify unit consistency across modules
- Improve error messages for engineering inputs

### Planned — Testing
- Add invalid input tests (negative values, invalid units, strings, empty input)
- Add regression tests for any bugs found
- Increase test coverage
- Ensure tests pass in a clean environment

### Planned — CLI & UX
- Improve menu formatting and spacing
- Improve invalid input handling
- Standardise prompts and output formatting
- Optional: add colour and screen‑clearing

### Planned — Documentation
- Expand README with screenshots, examples, and project tree
- Standardise module documentation
- Add assumptions, equations, references, examples for each calculator
- Update CHANGELOG
- Review installation instructions from a fresh clone

### Planned — Release Engineering
- Configure GitHub Actions to run pytest automatically
- Add README status badges (optional)
- Tag and publish v0.1.1
- Write concise release notes summarising quality improvements
