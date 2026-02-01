# Forecasting-Financial-Inclusion
This repository contains an end-to-end data science project focused on forecasting Ethiopia’s financial inclusion trajectory using the World Bank Global Findex framework. The project was developed as part of the 10 Academy – KAIM Artificial Intelligence Mastery (Week 10 Challenge). 

## 📊 Task 1: Data Understanding and Enrichment

- Loaded and explored unified financial inclusion datasets
- Validated schema structure and record types
- Added enriched observations, events, and impact links
- Documented all enrichments in `docs/data_enrichment_log.md`


### Objective
The objective of Task 1 is to understand, validate, and enhance Ethiopia’s
financial inclusion dataset in preparation for analytical modeling.

### Key Activities
- Loaded and validated observations, events, and target indicators
- Reviewed schema consistency and data completeness
- Performed exploratory summaries by pillar, confidence, and time coverage
- Identified key data gaps limiting time-series analysis
- Added enriched proxy observations to improve modeling feasibility
- Documented all enrichment decisions for transparency and auditability

### Outputs
- Enriched dataset saved to `data/processed/ethiopia_fi_unified_data_enriched.csv`
- Data enrichment documentation in `data/enrichment/data_enrichment_log.md`
- Clean and reproducible Task 1 notebook

### Notes
Original raw data remains unchanged. All additions are conservative estimates
used solely to support downstream analysis and forecasting tasks.

## 📊 Task 2: Exploratory Data Analysis (EDA)

### Overview

This task performs an exploratory data analysis of Ethiopia’s financial inclusion dataset to assess data structure, coverage, quality, and analytical readiness. The analysis aims to uncover patterns, gaps, and limitations before advanced modeling or insight generation.

### Objectives

- Understand dataset composition and structure
- Assess pillar, source, and confidence distributions
- Evaluate temporal coverage and indicator sparsity
- Identify data quality issues and analytical constraints

### Key Analyses Performed

- Record type and pillar distribution
- Source and confidence assessment
- Temporal coverage analysis by year and indicator
- Indicator × year heatmap visualization
- Event timeline contextualization

### Key Insights

- Data is heavily concentrated in 2024–2025, limiting long-term trend analysis
- Access indicators dominate reporting; gender and affordability are underrepresented
- Most indicators lack sufficient longitudinal depth
- Events align with major financial and telecom sector reforms
- High confidence labels coexist with structural data gaps

### Data Quality Limitations

- Sparse temporal coverage for most indicators
- Significant missing values in several descriptive fields
- Limited geographic granularity
- Event records are non-numeric and contextual only

### Folder Structure

notebooks/
 └── task_2_eda.ipynb
data/
 ├── raw/
 ├── processed/
 └── enriched/
docs/
 └── task_2_readme.md
