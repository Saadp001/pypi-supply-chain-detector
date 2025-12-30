## Detecting Typosquatting Attacks in PyPI

This project prototypes an applied security research system for detecting
potentially malicious Python packages in the PyPI ecosystem.

### Approach
- Collected package metadata using PyPI public APIs
- Applied string similarity techniques to detect typosquatting
- Modeled suspicious publishing behavior using heuristic risk scoring

### Motivation
Typosquatting is a common software supply chain attack where adversaries
publish packages with names similar to popular libraries to trick developers.

### Outcome
The system flags packages exhibiting high name similarity and anomalous
publishing behavior for further investigation.
