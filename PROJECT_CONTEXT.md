# PROJECT_CONTEXT.md

# Nahongu Project Context

## Overview

Nahongu is a Python-based desktop application focused on data analysis and AI-assisted insights generation.

The project was developed as a competition submission and combines traditional data analysis methods with AI-generated interpretations and reporting capabilities.

The application is designed to be user-friendly, Persian-language compatible, and capable of processing user-provided datasets to generate meaningful reports.

---

# Current Status

Project Status: Submitted

Competition Status: Waiting for judging results

The competition version has already been packaged, documented, recorded, and submitted.

Future development may continue independently of the competition version.

---

# Main Technologies

Language:

* Python

GUI:

* PyQt6

Data Processing:

* Pandas
* NumPy
* CSV
* JSON

AI Layer:

* AIClient
* AI Analysis Module

Networking:

* Requests
* python-dotenv

Reporting:

* ReportLab
* PDF Export

Persian Support:

* arabic_reshaper
* python-bidi

---

# High Level Architecture

Application Layers:

1. GUI Layer
2. Data Processing Layer
3. Numerical Analysis Layer
4. AI Analysis Layer
5. Reporting Layer

The GUI is responsible for user interaction.

The Data Processing Layer loads and prepares datasets.

The Numerical Analysis Layer performs statistical and mathematical operations.

The AI Layer generates explanations, interpretations, and insights.

The Reporting Layer creates PDF outputs and formatted reports.

---

# Design Goals

Primary Goals:

* Easy dataset loading
* Automated analysis
* AI-assisted interpretation
* Persian language support
* Professional report generation
* Competition-ready presentation

Secondary Goals:

* Clean architecture
* Maintainability
* Future scalability
* Modular design

---

# Known Components

Observed modules include:

* ai_layer.ai_client
* run_numpy_analysis()
* run_ai_analysis()

Additional modules may exist and should be documented later.

---

# Dependencies

Current known dependencies:

PyQt6
pandas
numpy
reportlab
requests
python-dotenv
chardet
arabic-reshaper
python-bidi

---

# Development Notes

The project should continue moving toward:

* Better modularity
* Cleaner architecture
* Better separation of concerns
* Easier maintenance
* Improved AI capabilities
* Better reporting features

---

# AI Context Instructions

When analyzing this repository:

1. Read README.md first.
2. Read PROJECT_CONTEXT.md second.
3. Identify architecture from actual source code.
4. Compare source code against documented architecture.
5. Document missing components.
6. Suggest improvements without breaking existing functionality.

---

# Important Reminder

This document is a context summary.

Source code is always the primary source of truth.

If source code and this document conflict:

Trust the source code.
