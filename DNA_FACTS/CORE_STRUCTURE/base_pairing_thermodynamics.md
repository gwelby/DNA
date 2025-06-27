# Base Pairing Thermodynamics - Energy & Stability Facts

## **DISCOVERY & VERIFICATION**
- **First measurements**: 1950s-1960s by Doty, Marmur, Schildkraut
- **Method**: UV absorption spectroscopy, calorimetry
- **Refinement**: Modern techniques (DSC, ITC, fluorescence)
- **Status**: ✅ **100% CONFIRMED** - Precisely measured

---

## **HYDROGEN BOND ENERGIES** (Experimentally Measured)

### **Watson-Crick Base Pairs**
```
Adenine-Thymine (A-T):
- Hydrogen bonds: 2
- Bond energy: 7.6 kcal/mol (31.8 kJ/mol)
- Bond length: 2.95 Å
- Dipole moment: 2.3 D

Guanine-Cytosine (G-C):
- Hydrogen bonds: 3  
- Bond energy: 12.2 kcal/mol (51.0 kJ/mol)
- Bond length: 2.90 Å
- Dipole moment: 6.1 D
```

### **Stability Ratio**
- **G-C vs A-T**: 1.6× more stable
- **Energy difference**: 4.6 kcal/mol per pair
- **Temperature effect**: G-C content determines melting point
- **Biological significance**: Critical regions often G-C rich

---

## **DNA MELTING TEMPERATURES** (Tm Values)

### **G-C Content Correlation**
```
G-C Content (%)    Tm (°C) in 1M NaCl
     0             69.3
    10             71.0
    20             72.7
    30             74.4
    40             76.1
    50             77.8
    60             79.5
    70             81.2
    80             82.9
    90             84.6
   100             86.3
```

### **Calculation Formula**
**Tm = 81.5°C + 16.6(log[Na+]) + 0.41(%GC) - 675/length**

Where:
- [Na+] = Salt concentration in molarity
- %GC = Percentage of G-C base pairs
- length = DNA length in base pairs

### **Salt Dependence**
- **Low salt (0.01M)**: Tm decreases ~15°C
- **High salt (1.0M)**: Tm increases (stabilizes)
- **Mg²⁺ effect**: 2× stronger than Na⁺
- **Mechanism**: Electrostatic shielding of phosphate groups

---

## **THERMODYNAMIC PARAMETERS**

### **Enthalpy Changes (ΔH)**
```
Base Pair Stack          ΔH (kcal/mol)
AA/TT                      -9.1
AT/TA                      -8.6
TA/AT                      -6.0
CA/GT                      -8.5
GT/CA                      -8.4
CT/GA                      -7.8
GA/CT                      -8.2
CG/GC                     -10.6
GC/CG                     -9.8
GG/CC                     -8.0
```

### **Entropy Changes (ΔS)**
```
Base Pair Stack          ΔS (cal/mol·K)
AA/TT                     -24.0
AT/TA                     -23.9
TA/AT                     -16.9
CA/GT                     -22.7
GT/CA                     -22.4
CT/GA                     -20.8
GA/CT                     -22.2
CG/GC                     -27.2
GC/CG                     -24.4
GG/CC                     -19.9
```

### **Free Energy (ΔG at 37°C)**
```
Base Pair Stack          ΔG (kcal/mol)
AA/TT                      -1.7
AT/TA                      -1.2
TA/AT                      -0.8
CA/GT                      -1.4
GT/CA                      -1.4
CT/GA                      -1.3
GA/CT                      -1.3
CG/GC                      -2.2
GC/CG                      -2.0
GG/CC                      -1.8
```

---

## **NEAREST NEIGHBOR EFFECTS**

### **Stacking Interactions**
- **Definition**: Adjacent base pairs influence each other
- **Magnitude**: 1-3 kcal/mol per step
- **Most stable**: CG/GC stack (-2.2 kcal/mol)
- **Least stable**: TA/AT stack (-0.8 kcal/mol)

### **Sequence Dependence**
```
Stability Order (Most → Least stable):
1. CG/GC > GC/CG
2. AA/TT > GG/CC  
3. CA/GT = GT/CA
4. GA/CT = CT/GA
5. AT/TA
6. TA/AT
```

### **Biological Implications**
- **Promoter regions**: Often A-T rich (easier melting)
- **Coding regions**: Variable G-C content
- **Regulatory sequences**: Sequence-specific stability
- **DNA packaging**: Stability affects nucleosome binding

---

## **ENVIRONMENTAL EFFECTS**

### **Temperature Dependence**
- **Melting transition**: Cooperative (sharp)
- **van't Hoff enthalpy**: ΔH = 4RT²(d ln K/dT)
- **Denaturation**: Reversible under slow cooling
- **Hyperchromicity**: 40% UV absorption increase

### **pH Effects**
```
pH Range     Effect on Tm
7.0-8.0      Normal stability
<6.5         Cytosine protonation (Tm increases)
>9.0         Thymine deprotonation (Tm decreases)
<4.0         Adenine protonation (structure disrupted)
>12.0        Complete denaturation
```

### **Ionic Strength**
- **Phosphate repulsion**: Destabilizes double helix
- **Counterion binding**: Na⁺, Mg²⁺, K⁺ stabilize
- **Debye length**: ~3 Å at physiological salt
- **Optimal concentration**: 0.1-1.0 M monovalent salts

---

## **EXPERIMENTAL MEASUREMENTS**

### **UV Melting Curves**
- **Wavelength**: 260 nm (base absorption maximum)
- **Hyperchromic effect**: Single strands absorb more UV
- **Tm determination**: 50% denaturation point
- **Cooperativity**: Sharp transition (few degrees)

### **Differential Scanning Calorimetry (DSC)**
- **Direct ΔH measurement**: Heat capacity changes
- **Transition width**: Measure cooperativity
- **Reversibility**: Check for degradation
- **Multiple domains**: Complex melting profiles

### **Isothermal Titration Calorimetry (ITC)**
- **Binding studies**: Protein-DNA interactions
- **Thermodynamic profile**: ΔH, ΔS, ΔG simultaneous
- **Stoichiometry**: Binding ratios
- **Cooperativity**: Multiple binding sites

---

## **MISMATCHED BASE PAIRS**

### **Stability Reduction**
```
Mismatch Type     ΔΔG (kcal/mol)
G-T wobble             +1.3
A-C mismatch           +2.1
A-A mismatch           +2.5
G-G mismatch           +3.2
C-C mismatch           +3.8
T-T mismatch           +4.1
```

### **Biological Significance**
- **Proofreading**: Mismatches destabilize
- **Mutation hotspots**: G-T wobbles common
- **Repair recognition**: Distorted geometry signals
- **Evolution**: Mismatch tolerance varies

---

## **MODIFIED BASES**

### **Common Modifications**
```
Modification          Effect on Tm
5-Methylcytosine       +0.5°C per modification
N6-Methyladenine       +0.2°C per modification
Pseudouridine          +1.2°C per modification
Inosine               -3.4°C per modification
8-Oxoguanosine        -2.1°C per modification
```

### **Epigenetic Implications**
- **DNA methylation**: Stabilizes chromatin
- **Hydroxymethylation**: Intermediate stability
- **Damage bases**: Generally destabilizing
- **Recognition**: Protein binding changes

---

## **PRACTICAL APPLICATIONS**

### **PCR Design**
- **Primer Tm**: Calculate for optimal annealing
- **GC clamp**: 3' end stability
- **Length optimization**: 18-25 nucleotides typical
- **Secondary structure**: Avoid self-complementarity

### **Hybridization Assays**
- **Probe design**: Tm matching for specificity
- **Stringency washing**: Remove non-specific binding
- **Array design**: Uniform melting temperatures
- **FISH probes**: Long probes for stability

### **Drug Design**
- **Intercalators**: Increase duplex stability
- **Groove binders**: Sequence-specific recognition
- **Cross-linkers**: Prevent denaturation
- **Antisense**: Optimize target binding

---

## **MEASUREMENT TECHNIQUES**

### **UV Spectroscopy**
- **Advantages**: Simple, fast, quantitative
- **Limitations**: Requires pure DNA
- **Buffer effects**: Careful pH control needed
- **Concentration**: 0.1-1.0 OD₂₆₀ units

### **Fluorescence Methods**
- **SYBR dyes**: Real-time melting curves
- **Molecular beacons**: Intramolecular probes
- **FRET pairs**: Distance-dependent signals
- **Sensitivity**: Single molecule detection possible

### **Calorimetry**
- **DSC**: Direct enthalpy measurement
- **ITC**: Binding thermodynamics
- **Nano-DSC**: Small sample volumes
- **Model-independent**: No assumptions needed

---

## **CALCULATION EXAMPLES**

### **Tm Prediction**
```
Example: 50 bp DNA, 50% GC, 0.1M NaCl
Tm = 81.5 + 16.6(log 0.1) + 0.41(50) - 675/50
Tm = 81.5 + 16.6(-1) + 20.5 - 13.5
Tm = 81.5 - 16.6 + 20.5 - 13.5 = 71.9°C
```

### **Stability Calculation**
```
ΔG total = Σ(nearest neighbor ΔG) + initiation penalty
For ATCG sequence:
ΔG = ΔG(AT) + ΔG(TC) + ΔG(CG) + ΔG(init)
```

---

## **VERIFICATION STATUS**: ✅ **ESTABLISHED FACT**

**Evidence Level**: Level 1 (Quantitative, reproducible)
**Confidence**: 100% - Thermodynamic measurements universal
**Applications**: PCR, sequencing, drug design, molecular biology
**Precision**: ±0.1°C for Tm, ±0.05 kcal/mol for ΔG

---

## **SELF-TEST CHECKLIST**
- [ ] Can calculate Tm from G-C content and salt concentration
- [ ] Know energy difference between A-T and G-C pairs
- [ ] Understand nearest neighbor effects on stability
- [ ] Can explain salt and pH effects on DNA stability
- [ ] Know applications in PCR primer design
- [ ] Understand mismatch destabilization effects

---

*Sources: Breslauer et al. (1986) PNAS, SantaLucia (1998) PNAS, Allawi & SantaLucia (1997-1998), DNA thermodynamics databases, Modern calorimetry studies* 