# Replication Package for Bachelor’s Thesis in Computer Science

## Title: Exploring the impact of architectural smells refactoring in microservice projects

This replication package contains all the data and scripts used to extract and analyze architectural metrics from microservice-based projects.

---

### 📄 Script
- **[`Tesi-metrics-extractor.py`](./Tesi-metrics-extractor.py)**  
  Python script used to extract software metrics from the results of the Understand and Arcan analyses.
---

### Analyses   
The five remaining packages contain analyses conducted with the Arcan and Understand tools, in *toolName*-*projectName*-*iteration*.xlsx format. There are no Arcan reports for projects that have zero remaining smells in the final iteration. 
The folder structure is as follows:
```
├───MCA
│   ├───base
│   └───ref1 GC
├───RC
│   ├───base
│   ├───ref1 CD
│   ├───ref2 CD
│   ├───ref3 CD
│   └───ref4 CD
├───RP
│   ├───base
│   ├───ref1 CD
│   ├───ref10 HL
│   ├───ref2 CD
│   ├───ref3 CD
│   ├───ref4 CD
│   ├───ref5 HL
│   ├───ref6 HL
│   ├───ref7 HL
│   ├───ref8 HL
│   └───ref9 HL
├───RYC
│   ├───base
│   └───ref1 UD
└───SC
    ├───base
    ├───ref1 UD
    ├───ref2 UD
    ├───ref3 UD
    └───ref4 CD
```
