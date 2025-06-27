# Post-Transcriptional Control - RNA Processing and Regulation

## **DISCOVERY & VERIFICATION**
- **RNA splicing**: 1977 by Roberts and Sharp (Nobel Prize 1993)
- **5' capping**: 1975 by Shatkin and colleagues
- **Polyadenylation**: 1970s by Edmonds and colleagues
- **MicroRNAs**: 1993 by Lee, Feinbaum, and Ambros
- **Status**: ✅ **100% CONFIRMED** - Mechanistic precision established

---

## **POST-TRANSCRIPTIONAL OVERVIEW**

### **Processing Steps Hierarchy**
```
Primary transcript (pre-mRNA): Initial RNA pol II product
5' Capping: 7-methylguanosine cap addition (co-transcriptional)
Splicing: Intron removal and exon joining
3' Processing: Cleavage and polyadenylation
Nuclear export: Mature mRNA transport to cytoplasm
Translation regulation: ribosome recruitment and control
mRNA decay: Degradation and quality control
```

### **Temporal Coordination**
```
Co-transcriptional processing: Capping, splicing during transcription
Post-transcriptional: 3' processing, nuclear export
Cytoplasmic regulation: Translation control, decay
Timeline: Minutes (processing) to hours/days (mRNA stability)
Quality control: Multiple checkpoints ensure fidelity
```

---

## **5' CAPPING MECHANISM** (Atomic Detail)

### **Capping Chemistry**
```
Reaction sequence:
1. Phosphatase: 5'-triphosphate → 5'-diphosphate (RNGTT)
2. Guanylyltransferase: GMP addition forming unusual 5'-5' linkage
3. Methyltransferase 1: N7-methylation of terminal guanosine
4. Methyltransferase 2: 2'-O-methylation of first transcribed nucleotide

Chemical structure: 7mG(5')ppp(5')N1m-N2m-
Energy requirement: 2 ATP equivalents
Speed: ~30 seconds after transcription initiation
Efficiency: >99% of RNA pol II transcripts
```

### **Cap-Binding Proteins**
```
Nuclear cap-binding complex (CBC):
- CBP80: Large subunit (80 kDa)
- CBP20: Small subunit (20 kDa)
- Function: Nuclear export, nonsense-mediated decay
- Binding affinity: Kd = 0.1-1 nM

Cytoplasmic cap-binding:
- eIF4E: Translation initiation factor
- Binding: 7-methylguanosine cap recognition
- Regulation: 4E-BP proteins compete for binding
- Affinity: Kd = 50-200 nM (cap-dependent)
```

### **Cap Functions**
```
Translation enhancement: 10-100× increase in efficiency
mRNA stability: Protection from 5' exonuclease degradation
Nuclear export: Recognition by export machinery
Quality control: Nonsense-mediated decay regulation
Viral hijacking: Many viruses target cap structure
```

---

## **RNA SPLICING MECHANISMS** (Spliceosome Detail)

### **Splice Site Recognition**
```
5' splice site (donor):
- Consensus: (A/C)AG|GURAGU (R = purine)
- Recognition: U1 snRNP base pairing
- Conservation: GT dinucleotide (>99.5% of introns)
- Strength: Scoring matrices for prediction

3' splice site (acceptor):
- Consensus: Yn(C/T)AG|G (Yn = pyrimidine tract)
- Recognition: U2AF proteins bind polypyrimidine tract
- Branch point: Adenosine ~20-50 nt upstream of 3' site
- Conservation: AG dinucleotide (>99.5% of introns)

Branch point sequence:
- Consensus: YNYURAC (underlined A = branch point)
- Distance: 18-40 nucleotides from 3' splice site
- Function: Nucleophile for first transesterification
- Recognition: U2 snRNP and SF1/BBP proteins
```

### **Spliceosome Assembly** (Stepwise Mechanism)
```
E complex (early commitment):
- U1 snRNP binds 5' splice site
- SR proteins recognize exonic splicing enhancers
- Time: Seconds after transcription

A complex (pre-spliceosome):
- U2AF65/35 bind polypyrimidine tract and AG
- U2 snRNP binds branch point (ATP-dependent)
- SF1 displaced by U2 snRNP
- Formation time: 1-2 minutes

B complex (pre-catalytic spliceosome):
- U4/U6•U5 tri-snRNP recruitment
- U4/U6 base pairing disrupted
- U6 snRNA catalytic center formation
- Assembly time: 2-5 minutes

B* complex (activated spliceosome):
- U1 and U4 snRNPs released
- U6/U5 snRNPs form catalytic core
- First transesterification ready
- Activation: 30 seconds

C complex (catalytic spliceosome):
- First transesterification: 5' exon cleavage
- Lariat intermediate formation
- Second transesterification: Exon ligation
- Splicing time: 1-10 minutes per intron
```

### **Spliceosome Composition**
```
snRNPs (small nuclear ribonucleoproteins):
- U1: 165 nucleotides, 10 proteins
- U2: 188 nucleotides, 17 proteins  
- U4: 145 nucleotides, 9 proteins
- U5: 116 nucleotides, 8 proteins
- U6: 107 nucleotides, 7 proteins

Total spliceosome:
- RNA components: ~350 nucleotides
- Protein components: ~150 proteins
- Mass: ~12 MDa (ribosome-sized)
- Dynamics: Assembly/disassembly per intron
```

### **Splicing Kinetics** (Quantitative Measurements)
```
Splicing efficiency:
- Constitutional exons: >95% inclusion
- Alternative exons: 5-95% inclusion (regulated)
- Pseudo-exons: <1% inclusion (quality control)

Splicing rates:
- Fast introns: 0.5-2 minutes
- Slow introns: 5-30 minutes
- Gene length effect: Longer genes = slower average
- Co-transcriptional: Most splicing during transcription

Error rates:
- Splice site selection: <0.1% error rate
- Quality control: Nonsense-mediated decay removes errors
- Evolutionary pressure: Strong conservation of splice sites
```

---

## **ALTERNATIVE SPLICING** (Regulatory Complexity)

### **Splicing Patterns**
```
Exon skipping (cassette exons): 40% of alternative events
- Mechanism: Weak splice sites, regulatory elements
- Examples: DSCAM (38,016 isoforms), muscle troponin T
- Regulation: SR proteins vs. hnRNPs

Intron retention: 25% of alternative events
- Mechanism: Weak splice sites, retained in nucleus
- Function: Often reduces protein levels
- Tissue specificity: High in brain and testis

Alternative 5'/3' splice sites: 20% of alternative events
- Mechanism: Multiple weak splice sites compete
- Effect: Small insertions/deletions in protein
- Examples: FGFR2, CD44 variable exons

Mutually exclusive exons: 5% of alternative events
- Mechanism: Only one of several exons included
- Examples: DSCAM exons 6, 9, 17
- Regulation: Complex splicing enhancer networks
```

### **Regulatory Elements**
```
Exonic splicing enhancers (ESEs):
- Location: Within exons
- Function: Promote exon inclusion
- Proteins: SR proteins (SRSF1, SRSF2, etc.)
- Sequences: Purine-rich motifs

Exonic splicing silencers (ESSs):
- Location: Within exons
- Function: Promote exon skipping
- Proteins: hnRNPs (hnRNPA1, PTB, etc.)
- Sequences: Pyrimidine-rich motifs

Intronic splicing enhancers (ISEs):
- Location: Within introns
- Function: Strengthen weak splice sites
- Examples: Branch point enhancers

Intronic splicing silencers (ISSs):
- Location: Within introns
- Function: Weaken splice site recognition
- Mechanism: Compete with spliceosome assembly
```

### **Tissue-Specific Splicing**
```
Neuronal splicing:
- Nova proteins: Regulate GABA receptor splicing
- RBFOX proteins: Coordinate neuronal exon networks
- PTBP2: Neuronal-specific splicing regulator
- Examples: GRIN1, CACNA1C alternative splicing

Muscle splicing:
- MBNL proteins: Regulate muscle-specific isoforms
- CELF proteins: Developmental splicing transitions
- Disease: Myotonic dystrophy (CUG repeat expansion)
- Examples: Cardiac troponin T, insulin receptor

Sex-specific splicing:
- Drosophila doublesex: Master sex determination switch
- SR proteins: Sex-specific expression patterns
- X-inactivation: Alternative splicing involvement
```

---

## **3' END PROCESSING** (Cleavage and Polyadenylation)

### **Polyadenylation Signals**
```
AAUAAA hexamer:
- Position: 10-30 nucleotides upstream of cleavage site
- Conservation: >90% of human genes contain variant
- Recognition: CPSF1 (CFI-25) subunit
- Variants: AUUAAA, UAUAAA (reduced efficiency)

GU/U-rich element:
- Position: 10-30 nucleotides downstream of cleavage site
- Function: CstF binding and cleavage stimulation
- Variability: Less conserved than AAUAAA
- Strength: Correlates with polyadenylation efficiency

Cleavage site:
- Consensus: CA|A (cleavage between C and A)
- Precision: Single nucleotide accuracy
- Variation: Some genes have multiple sites
- Efficiency: Strong signals = 90-95% usage
```

### **Polyadenylation Machinery**
```
CPSF (Cleavage and Polyadenylation Specificity Factor):
- Subunits: CPSF1, CPSF2, CPSF3, CPSF4, Fip1, WDR33
- Function: AAUAAA recognition and cleavage
- Activity: Endonuclease (CPSF3/CFI-73)

CstF (Cleavage stimulation Factor):
- Subunits: CstF1, CstF2, CstF3
- Function: GU/U-rich element binding
- RNA binding: CstF2 (CstF-64) subunit

CFI and CFII (Cleavage Factors I and II):
- CFI: CFI-25, CFI-68 subunits
- CFII: PCF11, CLP1 subunits  
- Function: Enhance cleavage efficiency

PAP (Poly(A) Polymerase):
- Function: Adds 200-250 adenine residues
- Processivity: Distributive (requires PABP)
- Regulation: CPSF and CstF stimulate activity
- Speed: 20-30 nucleotides/second
```

### **Poly(A) Tail Functions**
```
Translation enhancement:
- PABP binding: Poly(A)-binding protein recognition
- Circularization: PABP-eIF4G interaction
- Synergy: Cap and poly(A) cooperative effect
- Enhancement: 10-100× translation increase

mRNA stability:
- 3' protection: Blocks 3' exonuclease access
- Deadenylation: First step in mRNA decay
- Length correlation: Longer tail = more stable
- Half-life: Hours to days depending on sequence

Quality control:
- Nuclear polyadenylation: Required for export
- Cytoplasmic regulation: Tail length modulation
- Stress response: Global polyadenylation changes
```

---

## **MICRORNA REGULATION** (Post-Transcriptional Silencing)

### **MicroRNA Biogenesis**
```
Transcription:
- RNA pol II: Primary transcript (pri-miRNA)
- Length: 200-2,000 nucleotides
- Structure: Hairpin-containing precursor
- Regulation: Tissue-specific promoters

Nuclear processing:
- Drosha/DGCR8: Microprocessor complex
- Product: ~70 nt precursor (pre-miRNA)
- Recognition: Double-strand RNA structure
- Cleavage: ~22 bp from hairpin loop

Cytoplasmic processing:
- Dicer: RNase III endonuclease
- Product: ~22 nt miRNA duplex
- Guide strand: Incorporated into RISC
- Passenger strand: Degraded or sometimes functional

RISC loading:
- Argonaute proteins: Central RISC component (AGO1-4)
- Guide selection: Thermodynamic asymmetry
- Target recognition: Seed sequence (nt 2-8)
- Silencing: Translation repression or mRNA decay
```

### **Target Recognition and Silencing**
```
Seed sequence pairing:
- Region: Nucleotides 2-8 of miRNA
- Requirement: Perfect or near-perfect complementarity
- Location: Usually in 3' UTR of target mRNA
- Conservation: Evolutionary constraint on seed regions

Binding modes:
- Canonical sites: Perfect seed match + 3' compensation
- Marginal sites: Single mismatch in seed region
- Non-canonical: Compensatory binding outside seed
- Efficiency: Canonical > marginal > non-canonical

Silencing mechanisms:
- Translation repression: Initiation and elongation blocks
- mRNA decay: Deadenylation and degradation
- P-body sequestration: Stress granule localization
- Context dependence: 3' UTR length and structure effects
```

### **Quantitative miRNA Effects**
```
Target prediction:
- Human miRNAs: ~2,500 mature sequences
- Predicted targets: 10-1,000 per miRNA
- Validated targets: 1-100 per miRNA (functional)
- Network coverage: ~60% of protein-coding genes

Silencing magnitude:
- Protein reduction: 20-80% (typical range)
- mRNA reduction: 10-50% (when mRNA decay occurs)
- Fold-change: 1.2-5× (modest but significant)
- Tissue specificity: miRNA and target expression overlap

Evolutionary conservation:
- Seed sequences: Highly conserved across vertebrates
- Target sites: Conserved in orthologous 3' UTRs
- miRNA families: Ancient origin, slow turnover
- Regulatory networks: Conserved modules
```

---

## **RNA MODIFICATIONS** (Epitranscriptomics)

### **N6-Methyladenosine (m6A)**
```
Frequency: Most abundant mRNA modification
- Prevalence: ~0.1-0.4% of adenines in mRNA
- Distribution: ~3-5 sites per mRNA on average
- Location: Preferentially in 3' UTRs and near stop codons
- Motif: DRACH consensus (D=A/G/U, R=A/G, H=A/C/U)

Writers (methyltransferases):
- METTL3/METTL14: Primary methyltransferase complex
- WTAP: Regulatory subunit
- KIAA1429, RBM15: Additional complex members
- Activity: S-adenosylmethionine-dependent

Readers (binding proteins):
- YTHDF1: Translation enhancement
- YTHDF2: mRNA decay promotion
- YTHDF3: Translation and decay regulation
- YTHDC1: Nuclear splicing regulation

Erasers (demethylases):
- FTO: Fat mass and obesity-associated protein
- ALKBH5: AlkB homolog 5
- Activity: α-ketoglutarate-dependent demethylation
- Regulation: Metabolic and stress-responsive
```

### **Functional Consequences**
```
Translation regulation:
- YTHDF1: Ribosome recruitment enhancement
- eIF3 interaction: Direct translation stimulation
- Stress response: m6A promotes cap-independent translation
- Magnitude: 1.5-3× translation increase

mRNA stability:
- YTHDF2: Deadenylation and decay acceleration
- P-body recruitment: mRNA storage and degradation
- Half-life: 20-50% reduction in stability
- Selectivity: Tissue and condition-specific effects

Splicing regulation:
- YTHDC1: Nuclear m6A reader
- SR protein recruitment: Splicing enhancer activity
- Exon inclusion: 10-30% changes in alternative splicing
- Co-transcriptional: Links transcription and processing
```

### **Other RNA Modifications**
```
Pseudouridine (Ψ):
- Frequency: Second most abundant modification
- Function: RNA structure stabilization
- Enzymes: PUS proteins (pseudouridine synthases)
- Location: rRNA, tRNA, and some mRNAs

5-Methylcytosine (m5C):
- Enzymes: DNMT2, NSUN family
- Function: mRNA stability and translation
- Detection: Bisulfite sequencing adaptation
- Distribution: Selective mRNA targeting

Inosine (I) editing:
- Enzymes: ADAR1, ADAR2 (adenosine deaminases)
- Function: A-to-I conversion (read as G)
- Consequences: Amino acid changes, splicing effects
- Regulation: Tissue-specific and stress-responsive
```

---

## **NONSENSE-MEDIATED DECAY** (Quality Control)

### **NMD Mechanism**
```
Recognition signals:
- Premature termination codon (PTC): Stop codon upstream of exon junction
- Exon junction complexes (EJCs): Mark spliced exon boundaries
- Normal translation: EJCs displaced by ribosome
- NMD trigger: EJCs remain downstream of PTC

Core factors:
- UPF1: Central helicase (ATP-dependent)
- UPF2: Bridging factor (EJC to UPF1)
- UPF3: Cofactor (enhances UPF2 function)
- SMG factors: Kinases and phosphatases (SMG1, SMG5-7)

Mechanism steps:
1. PTC recognition during translation
2. UPF1 recruitment and phosphorylation
3. mRNA deadenylation and decay initiation
4. UPF1 dephosphorylation and recycling

Efficiency: 80-95% of PTC-containing transcripts degraded
Timeline: 2-6 hours for complete mRNA elimination
```

### **Physiological Functions**
```
Quality control:
- Nonsense mutations: 30% of genetic diseases
- Splicing errors: Aberrant transcript elimination
- Frameshift protection: Out-of-frame translation
- Evolutionary buffer: Permits neutral mutations

Gene regulation:
- Alternative splicing: Regulated inclusion of NMD exons
- Unproductive splicing: 10-30% of transcripts targeted
- Homeostasis: Autoregulation of splicing factors
- Stress response: Selective NMD inhibition

Therapeutic targeting:
- Nonsense suppression: PTC readthrough drugs
- NMD inhibition: Restore protein expression
- Cancer therapy: Exploit NMD dependence
- Examples: Ataluren, PTCX compounds
```

---

## **RNA-BINDING PROTEINS** (Global Regulators)

### **Major RBP Families**
```
SR proteins (Serine/Arginine-rich):
- Members: SRSF1-12 (formerly ASF/SF2, SC35, etc.)
- Function: Splicing enhancement, nuclear export
- Domains: RNA recognition motif + RS domain
- Regulation: Phosphorylation-dependent activity

hnRNPs (heterogeneous nuclear RNPs):
- Members: hnRNPA1, A2/B1, C, D, F, H, I, K, etc.
- Function: RNA packaging, splicing silencing
- Domains: RRM, RGG, KH domains
- Localization: Nuclear and cytoplasmic

ELAV/Hu proteins:
- Members: HuR, HuB, HuC, HuD
- Function: mRNA stabilization, translation
- Targets: AU-rich elements (AREs) in 3' UTRs
- Disease: HuR overexpression in cancer

CELF proteins:
- Members: CELF1-6 (CUG-BP1, ETR-3, etc.)
- Function: Alternative splicing, translation
- Targets: CUG and UGU repeats
- Disease: Myotonic dystrophy involvement
```

### **Quantitative RBP Effects**
```
Target breadth:
- Major RBPs: 1,000-10,000 mRNA targets each
- Specificity: Sequence and structure preferences
- Occupancy: 10-90% of binding sites occupied
- Competition: Multiple RBPs per mRNA

Regulatory magnitude:
- Splicing: 10-80% exon inclusion changes
- Stability: 2-10× mRNA half-life changes
- Translation: 2-20× protein output changes
- Localization: Nuclear vs. cytoplasmic partitioning

Tissue distribution:
- Ubiquitous: hnRNPs, SR proteins
- Tissue-restricted: Neuronal (Nova, RBFOX), muscle (MBNL)
- Developmental: Temporal expression patterns
- Disease: Aberrant RBP expression in pathology
```

---

## **CLINICAL SIGNIFICANCE**

### **Splicing Diseases**
```
Spinal muscular atrophy (SMA):
- Gene: SMN1 deletions/mutations
- Mechanism: SMN2 exon 7 skipping (weak splice site)
- Therapy: Spinraza (antisense oligonucleotide)
- Outcome: Exon inclusion restoration

β-Thalassemia:
- Cause: >200 different splicing mutations
- Mechanism: Cryptic splice site activation
- Severity: Reduced β-globin protein levels
- Therapy: Gene therapy, antisense approaches

Myotonic dystrophy:
- Cause: CUG repeat expansion (DM1) or CCUG (DM2)
- Mechanism: MBNL protein sequestration
- Effects: Aberrant splicing in muscle and brain
- Targets: Insulin receptor, cardiac troponin T

Cancers:
- SF3B1 mutations: 15% of myelodysplastic syndromes
- SRSF2 mutations: 10% of acute myeloid leukemia
- U2AF1 mutations: 5% of lung adenocarcinomas
- Mechanism: Altered splice site recognition
```

### **Therapeutic Approaches**
```
Antisense oligonucleotides (ASOs):
- Mechanism: Complementary sequence targeting
- Chemistry: 2'-O-methyl, morpholino modifications
- Examples: Eteplirsen (DMD), nusinersen (SMA)
- Delivery: Intrathecal, systemic administration

Small molecule modulators:
- Targets: Splicing factors, kinases
- Examples: Risdiplam (SMN2 splicing), TG003 (CLK inhibitor)
- Advantages: Oral bioavailability
- Challenges: Specificity, off-target effects

Gene therapy:
- Vectors: Adeno-associated virus (AAV)
- Approach: Normal gene complementation
- Examples: Zolgensma (SMA), Luxturna (LCA)
- Limitations: Delivery, immunogenicity

CRISPR/Cas approaches:
- Prime editing: Precise sequence correction
- Base editing: C-to-T, A-to-G conversions
- Advantages: Permanent correction
- Challenges: Delivery to tissues
```

---

## **EXPERIMENTAL TECHNIQUES**

### **RNA-seq Variants**
```
Standard RNA-seq:
- Information: Gene expression, novel transcripts
- Resolution: Exon-level quantification
- Depth: 20-100 million reads typical
- Applications: Differential expression analysis

Long-read sequencing:
- Platforms: PacBio, Oxford Nanopore
- Advantages: Full-length transcript isoforms
- Resolution: Individual splice variant detection
- Applications: Alternative splicing analysis

Single-cell RNA-seq:
- Sensitivity: 1,000-10,000 genes per cell
- Applications: Cell type identification, trajectories
- Splicing: Droplet-based methods limited
- Full-length: Plate-based methods better

Ribosome profiling:
- Principle: Ribosome-protected fragments
- Information: Translational efficiency
- Resolution: Codon-level precision
- Applications: Translation regulation studies
```

### **Splicing-Specific Methods**
```
Exon arrays:
- Design: Probes for individual exons
- Information: Exon inclusion levels
- Limitations: Known splice sites only
- Applications: Clinical diagnostics

CLIP-seq (Cross-linking immunoprecipitation):
- Principle: UV cross-linking + immunoprecipitation
- Information: Protein-RNA interaction sites
- Resolution: Nucleotide-level binding
- Variants: iCLIP, eCLIP, PAR-CLIP

SHAPE-seq (Selective 2'-hydroxyl acylation):
- Principle: Chemical probing of RNA structure
- Information: In vivo RNA secondary structure
- Applications: Splicing regulatory elements
- Resolution: Single nucleotide

Minigene assays:
- Design: Artificial genes with test exons
- Information: Splicing regulatory activity
- Applications: Mutation functional testing
- Advantages: Controlled experimental system
```

---

## **EVOLUTIONARY PERSPECTIVES**

### **Splicing Evolution**
```
Intron origin:
- Early hypothesis: Introns-early vs. introns-late
- Evidence: Group II self-splicing introns (prokaryotes)
- Spliceosome: Evolved from group II ribozymes
- Complexity: Increased in eukaryotic evolution

Alternative splicing expansion:
- Invertebrates: ~25% of genes alternatively spliced
- Vertebrates: >90% of genes alternatively spliced
- Complexity: Correlated with organism complexity
- Brain: Highest alternative splicing levels

Regulatory element turnover:
- ESE/ESS motifs: Rapid evolutionary turnover
- Constraint: Functional elements more conserved
- Innovation: New splice sites create novel functions
- Disease: Evolutionary recent elements more variable
```

### **Functional Innovation**
```
Proteome diversification:
- Single gene: Multiple protein isoforms
- Domain shuffling: Exon duplication and insertion
- Functional specialization: Tissue-specific isoforms
- Evolution: 100,000+ human protein isoforms from 20,000 genes

Regulatory complexity:
- Splicing networks: Coordinate cell type programs
- Feedback loops: Autoregulation of splicing factors
- Cross-regulation: miRNA and RBP interactions
- Robustness: Buffering against mutations
```

---

## **VERIFICATION STATUS**: ✅ **ESTABLISHED FACT**

**Evidence Level**: Level 1 (Mechanistic understanding, atomic structures)
**Confidence**: 100% - Comprehensive experimental validation
**Applications**: Therapeutic development, diagnostic tools, biotechnology
**Precision**: Single-nucleotide resolution, quantitative kinetics

---

## **SELF-TEST CHECKLIST**
- [ ] Understand 5' capping, splicing, and 3' processing mechanisms
- [ ] Know alternative splicing patterns and regulation
- [ ] Can explain miRNA biogenesis and function
- [ ] Understand RNA modifications and their effects
- [ ] Know quality control mechanisms (NMD)
- [ ] Understand clinical applications and therapeutic approaches

---

*Sources: Sharp & Roberts splicing discovery, Steitz laboratory spliceosome research, Bartel laboratory miRNA studies, He laboratory m6A modifications, ENCODE project RNA processing data* 