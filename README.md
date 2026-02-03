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

 ## 📊 Task 3: Event Impact Modeling

### Objective
Assess how major policy, market, and infrastructure events relate
to changes in financial inclusion indicators in Ethiopia.

### Methodology
- Defined ±12 month pre/post event windows
- Computed mean indicator changes following events
- Constructed an event–indicator association matrix
- Visualized impacts using heatmaps and bar charts

### Validation
Directional consistency between post-event changes and known
historical trends was assessed, supporting plausibility of associations.

### Key Assumptions
- Event impacts are linear and short- to medium-term
- Effects are associative, not causal
- External confounders are not fully controlled

### Outputs
- `data/outputs/event_indicator_matrix.csv`
- Event–indicator heatmap
- Pre/post impact visualizations

### Next Step
Results inform event-weighted, scenario-based forecasting in Task 4.


## 📊 Task 4: Forecasting Financial Inclusion Indicators (2025–2027)

### Objective

The objective of Task 4 is to forecast Ethiopia’s financial inclusion trajectory for 2025–2027, focusing on the two core Global Findex dimensions:

- Access: Account Ownership Rate

- Usage: Active Mobile Money / Digital Payment Adoption

These forecasts support forward-looking policy planning and investment decisions for stakeholders including development finance institutions, mobile money operators, and the National Bank of Ethiopia.

### Data Inputs

- Enriched unified dataset:
data/processed/ethiopia_fi_unified_enriched.csv

- Indicators selected based on availability, relevance, and alignment with Global Findex standards.

### Methodology

#### Time Series Preparation

- Annual aggregation of indicator values.

- Validation to ensure sufficient historical coverage.

#### Baseline Forecasting

- Linear trend extrapolation using historical data.

- Chosen due to limited sample size and need for interpretability.

#### Uncertainty Quantification

- Confidence intervals constructed using residual standard error.

- Reflects uncertainty from data sparsity and structural changes.

#### Scenario Analysis

- Baseline: continuation of observed trends.

- Optimistic: accelerated reform and infrastructure expansion.

- Pessimistic: policy delays or slower ecosystem growth.

### Outputs

#### Forecasting notebook:
notebooks/task_4_forecasting.ipynb

#### Forecast table with confidence intervals:
data/forecasts/access_usage_forecasts.csv

#### Visualizations:

Indicator forecasts with confidence bands

Scenario comparison plots

### Key Findings

- Both Access and Usage indicators show continued growth through 2027.

- Usage growth is more sensitive to ecosystem and policy changes than Access.

- Scenario analysis highlights the importance of regulatory timing and infrastructure investments.

### Limitations

- Short historical time series limits model complexity.

- Linear trends may not fully capture nonlinear adoption dynamics.

- Event impacts are incorporated qualitatively rather than through causal estimation.

### Next Steps

- Integrate event-impact coefficients into forecasts (Task 3 → Task 4 refinement).

- Extend uncertainty modeling using probabilistic or Bayesian methods.

- Develop an interactive dashboard to communicate results to stakeholders (Task 5).

## 📊 Task 5: Interactive Dashboard for Financial Inclusion Forecasting

### Overview

Task 5 focuses on developing an interactive dashboard to communicate historical trends, key events, and forecasted trajectories of financial inclusion indicators in Ethiopia. The dashboard serves as the final decision-support layer of the project, translating analytical outputs into an accessible interface for policymakers, regulators, mobile money operators, and development partners.

The dashboard integrates historical data, enriched event information, and model-based forecasts developed in earlier tasks.

### Objectives

The dashboard is designed to:

Visualize historical Access and Usage indicators

Overlay key ecosystem events (e.g., Telebirr launch, M-Pesa entry)

Present forecasts for 2025–2027 with uncertainty intervals

Allow users to explore alternative growth scenarios

Communicate key insights and limitations clearly

### Folder Structure
dashboard/
├── app.py          # Streamlit application (UI + visualizations)
├── utils.py        # Reusable data loading and validation functions

### Data Sources

The dashboard uses:

data/processed/ethiopia_fi_unified_enriched.csv

data/forecasts/access_usage_forecasts.csv

These datasets are outputs from Tasks 1–4 and follow the unified schema defined earlier in the project.

### Key Dashboard Components
1. Historical Trends

Interactive time-series visualizations of financial inclusion indicators

Enables inspection of long-term trajectories and short-term changes

2. Event Timeline

Timeline visualization of major digital finance events

Supports contextual interpretation of structural shifts in indicators

3. Forecasts with Uncertainty

Forecasts for 2025–2027

Confidence intervals displayed to reflect model uncertainty

4. Scenario Analysis

User-controlled growth adjustment slider

Allows exploration of optimistic and pessimistic scenarios

5. Insights & Limitations

Summary of key takeaways

Explicit documentation of assumptions and data limitations

### How to Run the Dashboard

#### Install dependencies:

pip install -r requirements.txt


#### Launch the dashboard:

streamlit run dashboard/app.py


Open the provided local URL in your browser.

### Key Assumptions & Limitations

Forecasts assume structural continuity of recent trends

Event impacts are associative, not causal

Short time series limits complex model selection

Scenario analysis is illustrative, not predictive

### Outcome

The dashboard provides a clear, interactive interface for exploring Ethiopia’s financial inclusion trajectory, supporting evidence-based policy discussion and strategic planning.