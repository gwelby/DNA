# Epigenetic Mechanisms - Heritable Gene Regulation

## **DISCOVERY & VERIFICATION**
- **DNA methylation**: 1948 by Hotchkiss (5-methylcytosine discovery)
- **Histone modifications**: 1960s by Allfrey (acetylation/phosphorylation)
- **X-inactivation**: 1961 by Lyon (dosage compensation)
- **Chromatin inheritance**: 1990s-2000s (molecular mechanisms)
- **Status**: ✅ **100% CONFIRMED** - Mechanistic understanding established

---

## **EPIGENETIC OVERVIEW**

### **Fundamental Principles**
```
Definition: Heritable changes in gene expression without DNA sequence alteration
Mechanisms: DNA methylation, histone modifications, chromatin remodeling
Inheritance: Mitotic and sometimes meiotic transmission
Reversibility: Dynamic and environmentally responsive
Function: Cell identity, development, disease, evolution
```

### **Epigenetic Marks Hierarchy**
```
Level 1: DNA methylation (5-methylcytosine, 5-hydroxymethylcytosine)
Level 2: Histone modifications (>100 known modifications)
Level 3: Chromatin architecture (nucleosome positioning, compaction)
Level 4: Non-coding RNAs (long ncRNAs, microRNAs)
Level 5: 3D genome organization (TADs, compartments, loops)
```

### **Temporal Dynamics**
```
Establishment: Development and differentiation
Maintenance: Cell division and DNA replication
Erasure: Reprogramming and environmental response
Inheritance: Transgenerational transmission
Plasticity: Dynamic responses to stimuli
```

---

## **DNA METHYLATION** (Molecular Mechanisms)

### **5-Methylcytosine (5mC) Chemistry**
```
Reaction: Cytosine + S-adenosylmethionine → 5-methylcytosine + S-adenosylhomocysteine
Enzyme: DNA methyltransferases (DNMTs)
Context: Primarily CpG dinucleotides (98% in mammals)
Frequency: ~70-80% of CpG sites methylated in somatic cells
Location: Gene bodies, repetitive elements, some promoters
```

### **DNA Methyltransferases** (DNMT Family)
```
DNMT1 (maintenance methylation):
- Function: Hemimethylated CpG recognition and methylation
- Processivity: High (maintains patterns during replication)
- Partners: UHRF1, HELLS, PCNA
- Activity: 10-50× higher on hemimethylated vs. unmethylated DNA
- Localization: Replication foci during S phase

DNMT3A/3B (de novo methylation):
- Function: Methylation of unmethylated CpG sites
- Activity: Equal preference for unmethylated and hemimethylated
- Expression: High during embryogenesis and gametogenesis
- Targets: Repetitive elements, tissue-specific genes
- Regulation: Developmental stage and tissue-specific

DNMT3L (regulatory factor):
- Function: Stimulates DNMT3A/3B activity (no catalytic activity)
- Importance: Essential for maternal imprint establishment
- Expression: Germ cells and embryonic stem cells
- Interaction: Forms heterotetramers with DNMT3A/3B
```

### **CpG Islands and Shores**
```
CpG Islands:
- Definition: >200 bp, >50% GC, CpG O/E >0.6
- Number: ~29,000 in human genome
- Methylation: Generally unmethylated (protected)
- Function: Promoter regulation, transcription start sites
- Protection: CxxC domain proteins (CFP1, TET1)

CpG Shores:
- Location: Regions within 2 kb of CpG islands
- Methylation: Variable and tissue-specific
- Function: Differential gene expression
- Disease: Cancer-associated methylation changes
- Evolution: More variable than CpG islands

CpG Shelves:
- Location: 2-4 kb from CpG islands
- Function: Additional regulatory elements
- Methylation: Intermediate levels
- Conservation: Less conserved than islands/shores
```

### **Quantitative Methylation Measurements**
```
Global methylation levels:
- Embryonic stem cells: ~25% of CpGs
- Somatic tissues: ~70-80% of CpGs
- Cancer cells: Global hypomethylation + focal hypermethylation
- Aging: Progressive global hypomethylation

Methylation kinetics:
- DNMT1 rate: ~1 site/second (maintenance)
- DNMT3A/3B rate: ~0.1 sites/second (de novo)
- Replication timing: S phase coordination
- Half-life: Stable through multiple cell divisions

Tissue specificity:
- Brain: Highest methylation levels
- Blood: Lower methylation, high variability
- Gametes: Extensive demethylation/remethylation
- Cancer: Tumor-specific methylation patterns
```

---

## **DNA DEMETHYLATION** (Active and Passive)

### **TET Enzymes** (Ten-Eleven Translocation)
```
TET1/2/3 function:
- Reaction: 5mC → 5hmC → 5fC → 5caC
- Cofactors: α-ketoglutarate, Fe(II), vitamin C
- Processivity: Iterative oxidation steps
- Specificity: CpG and non-CpG sites
- Regulation: Metabolic state dependent

5-Hydroxymethylcytosine (5hmC):
- Abundance: ~0.4% of cytosines in brain, ~0.1% in other tissues
- Function: Intermediate in demethylation pathway
- Stability: Can be maintained through replication
- Recognition: Specific binding proteins (MeCP2, etc.)
- Distribution: Gene bodies, enhancers, promoters

Base excision repair (BER) pathway:
- TDG: Thymine DNA glycosylase (5fC/5caC excision)
- SMUG1: Single-strand-selective monofunctional uracil-DNA glycosylase
- APE1: Apurinic/apyrimidinic endonuclease
- Pol β: DNA polymerase β (gap filling)
- XRCC1/LIG3: DNA ligase complex
```

### **Demethylation Mechanisms**
```
Passive demethylation:
- Mechanism: Loss during DNA replication without maintenance
- Rate: 50% per cell division (if DNMT1 absent)
- Context: Early development, some pathological states
- Examples: Primordial germ cell reprogramming

Active demethylation:
- Mechanism: TET-mediated oxidation + BER
- Rate: Complete within 1-3 cell divisions
- Context: Rapid gene activation, reprogramming
- Examples: Zygotic paternal demethylation, immune activation

AID/APOBEC pathway:
- Mechanism: Cytosine deamination to uracil + BER
- Context: Germinal center B cells, some reprogramming
- Controversy: Physiological relevance debated
- Specificity: Limited to specific cellular contexts
```

---

## **HISTONE MODIFICATIONS** (Chromatin Code)

### **Major Histone Modifications**
```
Acetylation:
- Residues: Lysines on H3, H4, H2A, H2B
- Writers: HATs (CBP/p300, PCAF, GCN5, MOZ, etc.)
- Erasers: HDACs (Class I, II, III, IV)
- Readers: Bromodomains (BRD2/3/4, BPTF, etc.)
- Function: Transcriptional activation, chromatin opening

Methylation:
- Residues: Lysines and arginines (H3K4, H3K9, H3K27, H3K36, etc.)
- Writers: KMTs (SET domain proteins, DOT1L)
- Erasers: KDMs (LSD1, JMJD family)
- Readers: Chromodomains, PHD fingers, Tudor domains
- Function: Activation or repression (context-dependent)

Phosphorylation:
- Residues: Serines, threonines, tyrosines
- Writers: Kinases (Aurora B, MSK1/2, IKKα, etc.)
- Erasers: Phosphatases (PP1, PP2A, etc.)
- Function: Mitosis, transcription, DNA repair
- Dynamics: Rapid and reversible

Ubiquitination:
- Residues: H2AK119, H2BK120
- Writers: E3 ligases (PRC1, RNF20/40)
- Erasers: Deubiquitinases (USP7, USP16, etc.)
- Function: Transcriptional regulation, DNA repair
- Crosstalk: Influences other modifications
```

### **Histone Modification Patterns**
```
Active promoters:
- H3K4me3: Sharp peaks at transcription start sites
- H3K27ac: Active enhancers and promoters
- H3K9ac: Transcriptionally active chromatin
- H3K14ac: Associated with transcription factors

Active gene bodies:
- H3K36me3: Elongating RNA polymerase II
- H3K79me2: Transcribed regions (DOT1L)
- H4K20me1: Actively transcribed genes
- H2BK120ub: Associated with transcription

Repressed chromatin:
- H3K27me3: Polycomb-mediated silencing
- H3K9me3: Constitutive heterochromatin
- H4K20me3: Pericentric heterochromatin
- H2AK119ub: Polycomb repressive complex 1

Bivalent domains:
- H3K4me3 + H3K27me3: Poised genes in stem cells
- Function: Ready for activation or permanent silencing
- Resolution: During differentiation
- Examples: Developmental transcription factors
```

### **Quantitative Modification Levels**
```
Modification abundance (% of total histone):
- H3K4me3: ~1-5% of H3
- H3K27me3: ~5-15% of H3
- H3K9me3: ~2-10% of H3
- H3K36me3: ~1-3% of H3
- H3K27ac: ~0.5-2% of H3

Genomic distribution:
- Active marks: 10-20% of genome
- Repressive marks: 20-40% of genome
- Bivalent domains: 2-5% of genome (ES cells)
- Unmarked chromatin: 40-60% of genome

Dynamic range:
- Fold changes: 2-100× between active/inactive states
- Kinetics: Minutes (acetylation) to hours (methylation)
- Inheritance: Variable through cell division
- Plasticity: Responsive to environmental stimuli
```

---

## **CHROMATIN REMODELING COMPLEXES**

### **SWI/SNF Family**
```
BAF complexes (Brg1/Brm-associated factors):
- Subunits: 10-15 proteins, ~2 MDa
- ATPase: BRG1 or BRM (mutually exclusive)
- Function: Nucleosome sliding, ejection, exchange
- Targets: Promoters, enhancers, insulator elements
- Disease: >20% of cancers have SWI/SNF mutations

PBAF complexes (Polybromo-associated BAF):
- Unique subunits: PBRM1, ARID2, BRD7
- Function: Similar to BAF but distinct targets
- Specificity: Developmental gene regulation
- Cancer: PBRM1 mutations in renal cell carcinoma

ncBAF (non-canonical BAF):
- Composition: Specialized subunit combinations
- Function: Neural development-specific
- Subunits: GLTSCR1, BRD9 (instead of traditional subunits)
- Importance: Brain development and function
```

### **ISWI Family**
```
NURF (Nucleosome remodeling factor):
- ATPase: SNF2H or SNF2L
- Function: Transcriptional activation
- Specificity: H4 tail and linker histone interactions
- Targets: Nuclear receptor-regulated genes

CHRAC (Chromatin accessibility complex):
- Components: SNF2H + ACF1 + CHRAC-14/16
- Function: Chromatin assembly and spacing
- Activity: Nucleosome sliding for regular spacing
- Process: Replication-coupled chromatin assembly

ACF (ATP-utilizing chromatin assembly and remodeling factor):
- Components: SNF2H + ACF1
- Function: Nucleosome assembly and positioning
- Regulation: Cell cycle-dependent activity
- Conservation: Present across eukaryotes
```

### **CHD Family**
```
CHD1:
- Function: Transcription-coupled nucleosome assembly
- Recognition: H3K4me3 binding via chromodomains
- Process: Co-transcriptional chromatin maintenance
- Disease: Mutations in intellectual disability

CHD4 (NuRD complex):
- Function: Transcriptional repression
- Partners: MTA, HDAC1/2, MBD proteins
- Mechanism: Nucleosome sliding + histone deacetylation
- Targets: Methylated DNA and specific transcription factors

CHD7:
- Function: Enhancer chromatin remodeling
- Disease: CHARGE syndrome (75% of cases)
- Targets: p53 and tissue-specific enhancers
- Development: Critical for neural crest development

CHD8:
- Function: Chromatin remodeling and transcription
- Disease: Autism spectrum disorder mutations
- Targets: REST and Wnt signaling genes
- Expression: Brain-enriched expression pattern
```

---

## **POLYCOMB AND TRITHORAX SYSTEMS**

### **Polycomb Repressive Complexes**
```
PRC2 (Polycomb Repressive Complex 2):
- Core subunits: EZH1/2, SUZ12, EED, RbAp46/48
- Activity: H3K27 methyltransferase (EZH1/2)
- Recruitment: CpG islands, JARID2, transcription factors
- Targets: Developmental genes, tumor suppressors
- Regulation: Cell cycle, metabolic state

PRC1 (Polycomb Repressive Complex 1):
- Canonical: CBX, PHC, BMI1/MEL18, RING1A/B
- Non-canonical: RYBP/YAF2 variants
- Activity: H2AK119 ubiquitin ligase (RING1A/B)
- Recognition: H3K27me3 binding (canonical), CpG islands (non-canonical)
- Function: Chromatin compaction, transcriptional silencing

Mechanism:
1. PRC2 recruitment to target genes
2. H3K27me3 deposition across gene domain
3. PRC1 recruitment via H3K27me3 binding
4. H2AK119ub and chromatin compaction
5. Stable silencing and inheritance
```

### **Trithorax Group**
```
COMPASS complexes:
- Subunits: SET1A/B, WDR5, RbBP5, ASH2L, DPY30, CFP1
- Activity: H3K4 methyltransferase
- Targets: CpG island promoters
- Function: Transcriptional activation maintenance

MLL complexes:
- Members: MLL1-4, SETD1A/B
- Activity: H3K4 methyltransferase
- Specificity: Developmental gene regulation
- Disease: MLL translocations in leukemia
- Mechanism: Hox gene activation and maintenance

SWI/SNF complexes:
- Function: Chromatin accessibility for transcription factors
- Cooperation: Works with Trithorax proteins
- Targets: Polycomb-silenced genes (antagonistic)
- Regulation: Signal-responsive chromatin opening
```

### **Polycomb/Trithorax Competition**
```
Switching mechanism:
- Default: PRC-mediated silencing
- Activation: Signal-induced TrxG recruitment
- Maintenance: Self-reinforcing loops
- Memory: Mitotic inheritance of states

Bivalent domains:
- Composition: H3K4me3 + H3K27me3
- Function: Poised for rapid activation or silencing
- Resolution: Developmental signals resolve to active/inactive
- Importance: Stem cell gene regulation

Dynamic equilibrium:
- Binding competition: PRC vs. TrxG complexes
- Environmental response: Nutrient/stress-sensitive
- Epimutations: Stochastic switching events
- Disease: Imbalanced PRC/TrxG in cancer
```

---

## **IMPRINTING** (Parent-of-Origin Effects)

### **Genomic Imprinting Mechanism**
```
Imprinting control regions (ICRs):
- Number: ~100 known ICRs in mammals
- Size: 1-4 kb differentially methylated regions
- Function: Parent-of-origin-specific methylation
- Maintenance: DNMT1/UHRF1 during replication
- Evolution: Mammal-specific (mostly)

Differential methylation establishment:
- Maternal: DNMT3A/3L in growing oocytes
- Paternal: DNMT3A/3B during spermatogenesis
- Timing: Gametogenesis and early development
- Maintenance: Throughout somatic development
- Erasure: Primordial germ cells (next generation)

Allele-specific expression:
- Mechanism: Methylation-sensitive transcription factors
- Range: Complete to partial silencing
- Tissue specificity: Some imprints are tissue-restricted
- Developmental timing: Temporal activation patterns
- Dosage: Haploinsufficiency sensitivity
```

### **Imprinting Disorders**
```
Beckwith-Wiedemann syndrome:
- Locus: 11p15.5 (IGF2/H19, KCNQ1OT1/CDKN1C)
- Frequency: 1 in 13,700 births
- Mechanism: Loss of imprinting or UPD
- Features: Overgrowth, cancer predisposition
- Molecular: ICR1/ICR2 methylation defects

Prader-Willi/Angelman syndromes:
- Locus: 15q11-q13 imprinted cluster
- Frequency: 1 in 15,000 births (PWS), 1 in 12,000 (AS)
- Mechanism: Deletions, UPD, imprinting defects
- PWS: Paternal 15q11-q13 deficiency
- AS: Maternal 15q11-q13 deficiency (UBE3A)

Silver-Russell syndrome:
- Loci: 7p11.2 (GRB10), 11p15.5 (IGF2/H19)
- Features: Growth restriction, asymmetry
- Mechanism: Maternal UPD or hypomethylation
- Frequency: 1 in 30,000-100,000 births
- Diagnosis: Methylation analysis required
```

### **Evolutionary Significance**
```
Parent-offspring conflict theory:
- Paternal genes: Promote resource extraction
- Maternal genes: Limit resource allocation
- Examples: IGF2 (paternal) vs. IGF2R (maternal)
- Evidence: Birth weight and metabolic effects
- Evolution: Arms race between parental genomes

Dosage compensation:
- Mechanism: Equivalent to X-inactivation
- Function: Balance gene expression levels
- Examples: Placental-specific imprinting
- Tissue specificity: Brain-specific imprinting patterns
- Plasticity: Environmental modulation of imprinting
```

---

## **X-CHROMOSOME INACTIVATION**

### **X-Inactivation Mechanism**
```
XIST (X-inactive specific transcript):
- Length: ~17 kb long non-coding RNA
- Function: Chromosome-wide silencing
- Mechanism: Chromatin recruitment and spreading
- Localization: Coats the inactive X chromosome
- Regulation: Antisense TSIX in mouse

Initiation:
1. Random X chromosome choice (somatic cells)
2. XIST upregulation on future inactive X
3. XIST RNA coating of chromosome
4. Recruitment of silencing complexes
5. Heterochromatin formation and maintenance

Silencing complexes:
- PRC2: H3K27me3 deposition
- PRC1: H2AK119ub and compaction
- SMCHD1: DNA methylation and compaction
- HDACs: Histone deacetylation
- DNMTs: CpG island methylation (late)
```

### **X-Inactivation States**
```
Active X (Xa):
- Chromatin: Euchromatic, accessible
- XIST: Absent or very low expression
- Modifications: H3K4me3, H3K27ac, etc.
- DNA methylation: Normal pattern
- Timing: Throughout cell cycle

Inactive X (Xi):
- Chromatin: Heterochromatic, compacted
- XIST: High expression and coating
- Modifications: H3K27me3, H2AK119ub
- DNA methylation: Hypermethylated CpG islands
- Timing: Replicates late in S phase

Escapees:
- Genes: ~15% escape X-inactivation
- Location: Pseudoautosomal regions (PAR1/PAR2)
- Examples: UTX, DDX3X, KDM5C
- Function: Dosage-sensitive genes
- Evolution: Conserved across mammals
```

### **Clinical Significance**
```
Turner syndrome (45,X):
- Features: Short stature, ovarian dysgenesis
- Mechanism: Haploinsufficiency of escape genes
- Severity: Correlates with escape gene number
- Mosaicism: Variable phenotype with 45,X/46,XX

Klinefelter syndrome (47,XXY):
- Features: Tall stature, hypogonadism
- Mechanism: Extra X escape gene expression
- Severity: Mild compared to Turner syndrome
- Variants: Higher X numbers more severe

X-linked intellectual disability:
- Skewed X-inactivation: Non-random patterns
- Female carriers: Variable expression
- Examples: FMR1 (Fragile X), MECP2 (Rett syndrome)
- Diagnosis: X-inactivation analysis informative
```

---

## **ENVIRONMENTAL EPIGENETICS**

### **Diet and Metabolism**
```
DNA methylation sensitivity:
- Methyl donors: SAM, folate, B12, choline
- Deficiency: Global hypomethylation
- Excess: Tissue-specific hypermethylation
- Critical periods: Development, pregnancy
- Mechanisms: One-carbon metabolism pathway

Agouti mouse model:
- Gene: Avy (viable yellow agouti)
- Phenotype: Coat color, obesity, diabetes
- Mechanism: IAP retrotransposon methylation
- Diet: Methyl donor supplementation
- Inheritance: Transgenerational effects

Dutch Hunger Winter:
- Population: 1944-1945 famine exposure
- Timing: Periconceptional vs. late gestation
- Effects: Birth weight, adult metabolism
- Mechanism: IGF2 DMR methylation changes
- Persistence: Detectable 60+ years later
```

### **Stress and Trauma**
```
Glucocorticoid response:
- Target: GR promoter methylation
- Mechanism: Early life stress increases methylation
- Effect: Reduced stress response capacity
- Timing: Critical periods in development
- Reversibility: Partial with intervention

Holocaust survivors:
- Study: Epigenetic changes in survivors and offspring
- Genes: FKBP5, stress response pathways
- Mechanism: Trauma-associated methylation
- Inheritance: Potential transgenerational transmission
- Controversy: Replication and mechanism unclear

Social environment:
- Bees: Royal jelly affects DNA methylation
- Mice: Social isolation alters brain methylation
- Humans: SES correlates with methylation patterns
- Mechanism: Stress hormones and epigenetic enzymes
- Plasticity: Some changes reversible
```

### **Aging and Disease**
```
Epigenetic clocks:
- Principle: Age-correlated methylation changes
- Accuracy: ±3-5 years chronological age
- Sites: ~350-850 CpG sites (depending on clock)
- Tissues: Blood, saliva, brain, etc.
- Applications: Aging research, disease prediction

Cancer epimutations:
- CpG island methylator phenotype (CIMP)
- Tumor suppressors: CDKN2A, MLH1, BRCA1
- Frequency: 15-40% of cancers (type-dependent)
- Mechanism: Aberrant DNMT activity
- Therapy: 5-azacytidine, HDAC inhibitors

Neurodegeneration:
- Alzheimer's: APP, PSEN1 methylation changes
- Parkinson's: SNCA methylation alterations
- Huntington's: HTT repeat expansion effects
- Mechanism: Protein aggregation and epigenetic dysregulation
- Potential: Epigenetic biomarkers and therapies
```

---

## **THERAPEUTIC APPLICATIONS**

### **Epigenetic Drugs** (FDA Approved)
```
DNA methylation inhibitors:
- 5-azacytidine (Vidaza): DNMT inhibitor
- Decitabine (Dacogen): DNMT inhibitor
- Indications: Myelodysplastic syndromes, AML
- Mechanism: DNA damage and hypomethylation
- Resistance: DNMT3A mutations

HDAC inhibitors:
- Vorinostat (SAHA): Pan-HDAC inhibitor
- Romidepsin: Class I HDAC inhibitor
- Belinostat: Pan-HDAC inhibitor
- Indications: T-cell lymphoma, multiple myeloma
- Mechanism: Histone acetylation, apoptosis

Combination therapies:
- Rationale: Synergistic effects
- Examples: Azacitidine + HDAC inhibitors
- Clinical trials: >100 ongoing studies
- Challenges: Toxicity, specificity
- Biomarkers: Predictive markers needed
```

### **Targeted Epigenetic Editing**
```
dCas9-DNMT/TET systems:
- Components: Catalytically dead Cas9 + epigenetic enzymes
- Function: Targeted methylation/demethylation
- Specificity: Guide RNA-directed targeting
- Applications: Gene silencing/activation
- Limitations: Off-target effects, delivery

Epigenome editing tools:
- dCas9-KRAB: Targeted gene silencing
- dCas9-VP64: Targeted gene activation
- dCas9-LSD1: Targeted histone demethylation
- dCas9-p300: Targeted histone acetylation
- Applications: Research and potential therapy

Challenges:
- Delivery: Tissue-specific targeting
- Specificity: Avoiding off-target effects
- Duration: Transient vs. permanent changes
- Safety: Long-term consequences unknown
- Regulation: Ethical and regulatory frameworks
```

---

## **EXPERIMENTAL TECHNIQUES**

### **Genome-Wide Methylation Analysis**
```
Whole-genome bisulfite sequencing (WGBS):
- Coverage: Every CpG in genome
- Resolution: Single nucleotide
- Depth: 10-30× coverage typical
- Cost: High but decreasing
- Applications: Reference methylomes

Reduced representation bisulfite sequencing (RRBS):
- Coverage: ~10% of CpGs (CpG-rich regions)
- Enrichment: MspI digestion + size selection
- Cost: Lower than WGBS
- Applications: Comparative studies, biomarkers

Methylation arrays:
- Platforms: Illumina 450K, EPIC arrays
- Coverage: 450,000-850,000 CpG sites
- Cost: Low, high throughput
- Limitations: Predefined sites only
- Applications: EWAS, clinical diagnostics

Targeted bisulfite sequencing:
- Method: PCR amplification + bisulfite sequencing
- Coverage: Specific regions of interest
- Depth: High coverage (>100×)
- Applications: Validation, clinical testing
```

### **Chromatin Profiling Methods**
```
ChIP-seq (Chromatin Immunoprecipitation):
- Targets: Histone modifications, transcription factors
- Resolution: 100-500 bp regions
- Quantification: Peak height = binding strength
- Variants: ChIP-exo, CUT&RUN (higher resolution)

ATAC-seq (Assay for Transposase-Accessible Chromatin):
- Principle: Tn5 insertion into accessible chromatin
- Information: Open chromatin regions
- Resolution: Nucleosomal positioning
- Applications: Regulatory element mapping

Hi-C (Chromosome Conformation Capture):
- Information: 3D genome organization
- Resolution: 1-100 kb (depending on depth)
- Applications: TAD boundaries, loop identification
- Variants: Capture Hi-C, ChIA-PET (protein-mediated)

Single-cell methods:
- scBS-seq: Single-cell bisulfite sequencing
- scATAC-seq: Single-cell chromatin accessibility
- scChIP-seq: Single-cell histone modifications
- Applications: Cell type-specific epigenomes
```

---

## **INHERITANCE AND TRANSGENERATIONAL EFFECTS**

### **Mitotic Inheritance**
```
DNA methylation maintenance:
- Mechanism: DNMT1/UHRF1 recognition of hemimethylated CpG
- Efficiency: >95% faithful inheritance
- Timing: S phase, replication-coupled
- Regulation: Cell cycle checkpoints
- Errors: Occasional loss leading to epimutations

Histone modification inheritance:
- Chromatin restoration: Parental nucleosome recycling
- De novo deposition: New histone modification
- Efficiency: Variable (20-80% depending on mark)
- Mechanism: Chromatin assembly factors
- Maintenance: Transcription factor binding

Chromatin structure inheritance:
- Nucleosome positioning: Pioneer transcription factors
- Higher-order structure: 3D organization restoration
- Timing: Throughout cell cycle
- Stability: Variable across genomic regions
- Plasticity: Environmental responsiveness
```

### **Meiotic Inheritance (Transgenerational)**
```
Epigenetic reprogramming:
- Primordial germ cells: Global demethylation/remethylation
- Timing: E10.5-E13.5 in mouse development
- Extent: >90% of methylation erased
- Exceptions: Imprinted genes, some repetitive elements
- Reset: New gametic methylation patterns

Sperm epigenome:
- DNA methylation: ~80% of CpGs methylated
- Chromatin: Mostly protamines, some histones retained
- Modifications: H3K4me3, H3K27me3 at key loci
- Small RNAs: miRNAs, piRNAs
- Sensitivity: Environmental and age effects

Oocyte epigenome:
- DNA methylation: ~40% of CpGs methylated
- Chromatin: Nucleosome-based, modified histones
- Stability: Arrested meiosis I for months/years
- Vulnerability: Age-related changes
- Inheritance: Maternal effect genes

Transgenerational studies:
- Evidence: Animal models show 2-3 generation effects
- Mechanisms: Gametic epigenetic inheritance
- Human evidence: Limited but emerging
- Controversy: Distinguishing genetic vs. epigenetic
- Research: Active area of investigation
```

---

## **EVOLUTIONARY PERSPECTIVES**

### **Epigenetic Evolution**
```
Evolutionary functions:
- Phenotypic plasticity: Environmental responsiveness
- Bet-hedging: Population-level diversity
- Evolutionary capacitance: Hidden genetic variation
- Rapid adaptation: Faster than genetic change
- Memory: Transgenerational environmental effects

Epimutation rates:
- DNA methylation: 10^-4 to 10^-3 per site per generation
- Comparison: 10-100× higher than genetic mutations
- Reversibility: Most epimutations are transient
- Selection: Weak purifying selection on most sites
- Hotspots: Some regions more epimutable

Natural selection on epigenetic variation:
- Examples: Plant flower color, bee caste determination
- Mechanism: Selection on environmentally-induced variants
- Heritability: Partial transgenerational transmission
- Adaptation: Rapid response to environmental change
- Evolution: May facilitate genetic evolution
```

### **Comparative Epigenomics**
```
Conservation across species:
- Core machinery: DNMTs, TET, PRC, TrxG conserved
- Patterns: General principles conserved
- Specificity: Species and tissue-specific differences
- Evolution: Regulatory innovation through epigenetic changes

Phylogenetic analysis:
- Vertebrates: Similar global methylation patterns
- Invertebrates: More diverse methylation systems
- Plants: Extensive methylation, RdDM pathway
- Fungi: Limited methylation, other mechanisms
- Bacteria: Restriction-modification systems
```

---

## **VERIFICATION STATUS**: ✅ **ESTABLISHED FACT**

**Evidence Level**: Level 1 (Mechanistic understanding, atomic structures)
**Confidence**: 100% - Comprehensive experimental validation
**Applications**: Disease diagnosis, drug development, biotechnology
**Precision**: Single nucleotide resolution, quantitative measurements

---

## **SELF-TEST CHECKLIST**
- [ ] Understand DNA methylation establishment and maintenance
- [ ] Know major histone modifications and their functions
- [ ] Can explain chromatin remodeling mechanisms
- [ ] Understand imprinting and X-inactivation
- [ ] Know environmental epigenetic effects
- [ ] Understand inheritance mechanisms and therapeutic applications

---

*Sources: Waddington epigenetic landscape concept, Allis & Jenuwein chromatin research, Jaenisch DNA methylation studies, Reinberg Polycomb research, ENCODE epigenome mapping project* 