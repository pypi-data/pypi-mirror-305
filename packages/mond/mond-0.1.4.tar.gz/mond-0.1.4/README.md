# monte-solver


[![Downloads](https://static.pepy.tech/personalized-badge/mond?period=total&units=international_system&left_color=orange&right_color=blue&left_text=Downloads)](https://pepy.tech/project/mond)
[![License: GPL v3](https://img.shields.io/badge/License-GPL_v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C-blue)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![PyPI - Version](https://img.shields.io/pypi/v/mond.svg)](https://pypi.org/project/mond)

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