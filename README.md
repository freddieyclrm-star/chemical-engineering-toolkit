# ⭐ Chemical Engineering Toolkit — Version 0.1.1
![Tests](https://github.com/freddieyclrm-star/chemical-engineering-toolkit/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![License](https://img.shields.io/github/license/freddieyclrm-star/chemical-engineering-toolkit.svg)  
*A foundational engineering software platform developed alongside my Chemical Engineering degree.*

## 📘 About
The Engineering Toolkit provides a growing collection of engineering utilities built in Python.
Version 0.1.1 focuses on:

- Correctness

- Documentation quality

- Validation

- Testing

- CLI user experience

- Code style consistency

- Automation (CI + pre‑commit)

This release prepares the foundation for larger engineering modules in future versions.

## ⚙️ Features (v0.1.1)
⚙️ Features (v0.1.1)  
🔹 Full Type Hint Coverage
All public functions now include complete type annotations:

- parameters

- return types

- helper functions

- CLI menu functions

- Improves readability, IDE support, and static analysis.

🔹 Improved Docstrings (NumPy/SciPy Style)
Every calculator, converter, and public function now includes:

- Purpose

- Equation

- Assumptions

- Inputs

- Outputs

- Raises

- References

- Example

This brings the toolkit up to academic documentation standards.

🔹 Engineering Assumptions & References
All engineering functions now document:

- physical assumptions

- modelling simplifications

- reference values

- scientific sources

🔹 Expanded Validation
Validators now cover:

- mass flow

- cp

- temperature direction

- absolute zero

- unit support

- stoichiometric species

- reaction coefficients

Engineering validators raise precise exceptions, while CLI validators provide user‑friendly messages.

🔹 Testing & Regression Suite
v0.1.1 introduces a full testing framework:

- tests for every validator

- tests for every engineering function

- tests for unit conversion

- tests for reaction stoichiometry

- regression tests for all calculators

- “Why this fails” documentation for error cases

This ensures long‑term stability and prevents silent regressions.

🔹 CLI Improvements
The command‑line interface now includes:

- colour‑coded output

- spacing helpers

- section formatting

- invalid choice handling

- screen clearing

- safe_run() wrapper for crash‑proof execution

The CLI is now clean, readable, and professional.

🔹 Code Quality & Style
v0.1.1 introduces:

- full PEP 8 cleanup

- Black auto‑formatting

- Ruff linting

- optional flake8 support

- pre‑commit hooks to enforce formatting before every commit

Your codebase is now consistent and maintainable.

🔹 Continuous Integration
GitHub Actions automatically runs pytest on:

- every push

- every pull request

This ensures the toolkit remains stable as it grows.

## 📂 Project Structure
```python
chemical-engineering-toolkit/  
│  
├── src/  
│   ├── main.py  
│   └── toolkit/  
│       ├── units/  
│       ├── balances/  
│       ├── constants/  
│       ├── core/  
│       └── utils/  
│  
├── tests/  
│   ├── test_units.py  
│   ├── test_mass_balance.py  
│   └── test_energy_balance.py  
│  
└── docs/  
  ```
## 🚀 Installation
1. Clone the repository  
```python 
git clone https://github.com/freddieyclrm-star/chemical-engineering-toolkit.git   
cd chemical-engineering-toolkit  
```  
2. Install dependencies  
```python
pip install -r requirements.txt
```  

## ▶️ How to Run
From the project root:

```python
python src/main.py
```
You will see:  

```python

================================
Chemical Engineering Toolkit
Version 0.1.1
================================
Please select an option:
0. Exit
1. Unit Converter
2. Scientific Constants
3. Engineering Constants
4. Mass Balance
5. Energy Balance

```
## Tests
```python
python -m pytest
```
## 📚 Examples
### **Unit Conversion**
```python
Enter the value to convert: 5  
Enter the unit to convert from: bar  
Enter the unit to convert to: Pa  
--- Inputs ---   
  
From unit:          5.000 bar  
--- Results ---  
  
Converted:          500000.000 Pa  
  
Calculation completed successfully.  
```

### **Mass Balance**
```python
Enter inlet mass flows rate (kg/s), separated by commas:  
Inlet streams: 100  
  
Enter outlet mass flows rate (kg/s), separated by commas:  
Outlet streams: 50  
Net mass balance: 50.0 kg/s  
```
### **Energy Balance**
```python
=== Sensible Heat Calculation ===  
Enter mass flow rate (kg/s): 10  
Enter specific heat capacity (J/kg•K): 4184 J/kg•K  
Enter inlet temperature (°C): 10  
Enter outlet temperature (°C): 30  
--- Results ---  
  
Sensible heat duty: 836800.000 W  
  
Calculation completed successfully.  
```

## 🛠️ Roadmap
### Coming Next (v0.2.x)
- Improved CLI navigation

- More unit conversions

- Additional engineering constants

- Better error handling

### Long‑Term (Degree Roadmap)
- Thermodynamics

- Fluid mechanics

- Heat transfer

- Reaction engineering

- Process design tools

## 📄 License
MIT License — see ```LICENSE``` for details.

## 🎓 Purpose
This toolkit is part of my preparation for studying Chemical Engineering (MEng) at the University of Bath.
Version 0.1.1 demonstrates:

- Professional documentation

- Robust engineering validation

- Full type hinting

- Regression‑tested engineering functions

- Clean CLI UX

- Automated CI

- Maintainable architecture

## 📍 Roadmap

The Chemical Engineering Toolkit follows a structured, professional release cycle designed to build a strong foundation before expanding into more advanced engineering features.

### 🔹 v0.1.2 — PLANNING
