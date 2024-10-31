# monte-solver

Monte Carlo dissolver.

## Why

Studying molecules in solution is super interesting. 

## What

It is a module to automatically prepare sample mixtures for solutions in e.g. gas phase or liquid phase
from multiple molecules according to defined concentration

## OpenMM 

Installing OpenMM from PyPi is nice to avoid conda, but you need to have numpy<2 installed. In case
of errors, you may run: 

```bash
pip install "numpy<2"
```