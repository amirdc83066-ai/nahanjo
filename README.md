# Nahanjo

## Overview

Nahanjo is an AI-assisted data anomaly detection and dataset investigation platform built with Python and PyQt6.

The project is designed to help users identify anomalies, evaluate dataset quality, and generate explainable AI-powered insights from structured data sources such as CSV and Excel files.

Nahanjo combines traditional anomaly detection algorithms with AI-generated explanations to make advanced data analysis more accessible for students, researchers, analysts, and developers.

---

## Key Features

### Dataset Import

* CSV file support
* Excel file support
* Dataset preview and validation

### Anomaly Detection

Currently implemented:

* Isolation Forest
* Z-Score Detection
* IQR (Interquartile Range)

Planned:

* Local Outlier Factor (LOF)
* One-Class SVM
* Ensemble Detection Engine
* Confidence Scoring System

### AI-Powered Analysis

* OpenAI-powered dataset analysis
* Natural language explanations
* Human-readable anomaly interpretation
* AI-generated investigation summaries

### Reporting

* PDF export for analysis results
* PDF export for AI-generated insights

---

## Current Workflow

1. Import a CSV or Excel dataset.
2. Run anomaly detection algorithms.
3. Review anomaly results in a structured table.
4. Generate AI-powered analysis and explanations.
5. Export findings and reports as PDF documents.

---

## Technology Stack

### Core

* Python

### Desktop Application

* PyQt6

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### AI Integration

* OpenAI API

### Reporting

* PDF Export System

---

## Current Development Status

Nahanjo is actively under development.

The current version provides:

* Dataset loading
* Multiple anomaly detection methods
* Result visualization through tables
* AI-assisted interpretation
* PDF report generation

The project is currently evolving toward a more advanced analytics and investigation platform.

---

## Planned Roadmap

### Data Workspace

* Dataset editing
* Column selection
* Data preparation tools

### Analysis Engine 2.0

* LOF
* One-Class SVM
* Ensemble anomaly detection
* Confidence scoring

### Dashboard System

* Histograms
* Box plots
* Risk indicators
* Anomaly distribution visualizations

### AI 2.0

* Dataset understanding
* Explainability engine
* Smart recommendations
* Executive summaries

### Investigation Workspace

* Critical anomaly review
* Search and filtering
* Interactive exploration

### Analysis History

* Recent analyses
* Pinned investigations
* Knowledge base

---

## Vision

The long-term goal of Nahanjo is to become an AI-assisted data investigation platform that helps users understand datasets, detect anomalies, explain findings, and support decision-making through intelligent analytics.

Rather than simply identifying outliers, the platform aims to help users understand why anomalies occur and what actions should be taken next.

---

## License

MIT License
