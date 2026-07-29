# ⭐ Chemical Engineering Toolkit — Version 0.1.0
*A foundational engineering software platform developed alongside my Chemical Engineering degree.*

## 📘 About
The **Chemical Engineering Toolkit** is a growing collection of engineering utilities built in Python.  
This project will expand throughout my degree into thermodynamics, fluid mechanics, heat transfer, reaction engineering, and process design.

## ⚙️ Features (v0.1.0)
1. **Command‑Line Interface**
A simple, modular CLI that acts as the entry point for all tools.

2. **Unit Converter**
Supports essential engineering conversions:

    - Temperature (°C, K, °F)

    - Pressure (Pa, kPa, bar, atm, psi, MPa, torr)

    - Mass (g, kg, tonne, mg, oz, lb)

    - Energy (J, kJ, MJ, kWh, Wh, cal, kcal)

    - Length (mm, cm, m, km, in, ft, yard, mile)

    - Speed (m/s, km/h, mph)

    - Volume (mL, L, m3, gallon, quart, pint, cup)

    - Time (s, min, h, day, week, month, year)

    - Area (mm2, cm2, m2, km2, ft2, in2, ha, acre, mi2)

3. **Scientific Constants**
Includes core scientific constants with documentation:

    - Gas constant

    - Avogadro’s number

    - Boltzmann constant

    - Planck constant

    - Speed of light

    - Newton's Gravitational Constant

    - Stefan-Boltzmann Constant

    - Elementary Charge

    - Mass of Electron

    - Mass of Proton

    - Mass of Neutron

4. **Engineering Constants**
Common reference values with assumptions:

    - Water density (20°C)

    - Air density

    - Atmospheric pressure

    - Specific heat capacities

5. **Mass Balance Calculator**
Steady‑state mass balance:

    - Single stream

    - Multiple streams

    - Reaction stoichiometry balance

    - Component mass fractions

    - Mixture mass flow calculations

6. **Energy Balance Calculator**
Basic heating calculation:

    - *Q = mcΔT* Calculation

    - Latent Heat Calculation

    - Reaction Enthalpy

    - Specific Heat Capacity Calculation

    - Heat Exchanger Energy Balance

    - Two Streams Heat Exchanger Balance

7. **Automated Tests**
Basic pytest suite covering:

    - Unit conversions

    - Mass balance

    - Energy balance

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
Version 0.1.0
================================
Please select an option:
0. Exit
1. Unit Converter
2. Scientific Constants
3. Engineering Constants
4. Mass Balance
5. Energy Balance
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
Version 0.1.0 demonstrates:

- Structured Python

- Git/GitHub workflow

- Engineering equation translation

- Documentation

- Testing

- Maintainable architecture