# Chinese Admin Text Classifier

## Overview

This project implements a rule-based Chinese administrative text consistency classifier. It checks whether a website column name is consistent with its corresponding government site name by using administrative hierarchy detection, institution keyword extraction, alias normalization, and explainable rule-based classification.

## Background

This project is an anonymized and simplified reconstruction of a real-world internship task involving government website crawler output validation. The original workflow involved checking whether crawled pages and column names were consistent with their source websites, reviewing machine-generated labels, and formatting crawled article metadata into standardized HTML structures.

To protect data privacy and confidentiality, this repository uses only synthetic examples and does not include any original internship data or code.

## Data Note

The original problem was inspired by real-world data processing experience during an internship. To protect data privacy and confidentiality, all examples in this repository are synthetic or anonymized.

## Current Features

- Chinese administrative level detection
- Rule-based consistency classification
- Explainable prediction output
- Synthetic sample dataset
- Basic pro4ject structure for future Streamlit dashboard and evaluation

## Project Structure

```text
chinese-admin-text-classifier/
├── data/
│   └── synthetic_sample.csv
├── src/
│   ├── alias_normalizer.py
│   ├── evaluator.py
│   ├── hierarchy.py
│   ├── preprocess.py
│   └── rule_engine.py
├── notebooks/
├── screenshots/
├── app.py
├── README.md
└── requirements.txt