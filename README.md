# 🌳Forest-Explorer-Kenya
An interactive data-driven platform for exploring Kenya's forests, wildlife, biodiversity, and conservation insights.

# Introduction

Forest Explorer Kenya is an end-to-end cloud data engineering project that centralizes information about Kenya's forests and wildlife into a single platform. The project extracts data from public APIs and datasets, processes it through an automated ETL pipeline, stores it in Google Cloud, and delivers it through a responsive web application. It showcases key data engineering concepts, including ETL, cloud storage, data warehousing, workflow orchestration, and full-stack development.

# Problem Statement

Kenya has over 300 forests and thousands of wildlife species spread across multiple ecosystems. However, environmental information is fragmented across government agencies, conservation organizations, research databases, and public APIs.

Students, researchers, tourists, and conservationists often spend significant time searching different platforms for reliable information.

Forest Explorer Kenya solves this challenge by building a centralized cloud platform that automatically collects, processes, stores, and visualizes environmental data.


# Objectives

* Collect environmental data from multiple sources.
* Clean and transform the data using Python.
* Store the data in Google BigQuery.
* Analyze the data using SQL and Pandas.
* Create interactive dashboards and visualizations.
* Display forest and wildlife locations on maps.
* Make environmental information easier to explore.

---

# Architecture

```text
External Data Sources
        │
        ├── GBIF API
        ├── IUCN Red List
        ├── Kenya Forest Service
        └── OpenWeather API
        │
        ▼
Data Extraction
        │
        ▼
Data Cleaning & Transformation
        │
        ▼
Google BigQuery
        │
        ▼
SQL + Python + Pandas
        │
        ▼
Streamlit Application
        │
        ▼
Interactive Dashboards & Maps
        │
        ▼
Users
```

---

# Data Sources

### 🌍 GBIF API

Provides biodiversity and wildlife occurrence data, including species and geographic information.

### 🛡️ IUCN Red List

Provides information about species conservation status and categories.

### 🌲 Kenya Forest Service Dataset

Provides information about Kenya's forests, including forest types, locations, area, and geographic data.

### 🌦️ OpenWeather API

Provides weather information such as:

* Temperature
* Weather conditions
* Wind
* Precipitation

OpenWeather is used as an external environmental data source and will allow weather conditions to be connected to forest locations.

---

# ETL Workflow

### 1. Extract

Data is collected from:

* GBIF API
* IUCN Red List
* Kenya Forest Service
* OpenWeather API

### 2. Transform

The data is cleaned and prepared for analysis by:

* Removing duplicates
* Standardizing column names
* Handling missing values
* Cleaning coordinates
* Standardizing values
* Preparing datasets for BigQuery

### 3. Load

The processed data is stored in **Google BigQuery**.

### 4. Analyze

Data is queried using **SQL** and analyzed using **Python and Pandas**.

### 5. Visualize

The results are displayed through an interactive **Streamlit** application.

---

# Features

### 🏠 Dashboard

Provides an overview of the available forest data using:

* Key statistics
* Charts
* Maps

### 🌲 Forest Explorer

Allows users to:

* Explore forest locations
* Filter forests by type
* Filter by area
* View forest statistics
* View forest locations on a map

### 🦁 Wildlife Explorer

Allows users to explore:

* Wildlife species
* Species observations
* Counties
* Wildlife families
* Geographic distribution

### 🗺️ Interactive Map

Displays forest locations geographically and provides a visual way to explore environmental data.

### 🛡️ Conservation

Provides information about protected areas and IUCN conservation categories.

### 📊 Statistics

Provides charts and summaries comparing forest types, locations, and area.

### 🌦️ Weather

The weather section is being developed using the **OpenWeather API** to provide environmental conditions for selected locations.

---

# BigQuery

Google BigQuery is used as the project's cloud data warehouse.

The project currently contains datasets related to:

### Forests

* Forest locations
* Forest types
* Gazetted forests
* Protected forests

### Wildlife

* Species locations
* Species taxonomy
* Species observations
* Species conservation information

### Weather

* Weather data
* Current weather information

---

# Tech Stack

| Category        | Technology              |
| --------------- | ----------------------- |
| Programming     | Python                  |
| Data Processing | Pandas, NumPy           |
| Database        | Google BigQuery         |
| Querying        | SQL                     |
| Application     | Streamlit               |
| Visualization   | Plotly                  |
| Maps            | Streamlit Maps          |
| APIs            | GBIF, IUCN, OpenWeather |
| Data Source     | Kenya Forest Service    |
| Version Control | Git & GitHub            |
| Development     | VS Code                 |

---

# Project Structure

```text
Forest-Explorer-Kenya/
│
├── app/
│   ├── app.py
│   └── utils/
│       ├── __init__.py
│       └── bigquery.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── data_dictionary.md
│
├── notebooks/
│   ├── 01_gbif_eda.ipynb
│   ├── 02_tranform_gbif.ipynb
│   ├── 03_iucn_eda.ipynb
│   └── 04_inspect_kfs.ipynb
│
├── src/
│   ├── extract/
│   ├── load/
│   └── transform/
│
├── README.md
├── Research_Questions.md
├── requirements.txt
└── LICENSE
```

---

# Current Status

### ✅ Completed

* Data extraction and exploration
* Data cleaning and transformation
* GBIF data processing
* Kenya Forest Service data processing
* Google BigQuery integration
* Forest data loaded into BigQuery
* Wildlife data querying
* Protected-area data querying
* Streamlit application
* Forest dashboard
* Wildlife dashboard
* Conservation dashboard
* Statistics dashboard
* Interactive forest map
* Plotly visualizations

### 🔄 In Development

* OpenWeather API integration
* Weather dashboard
* Additional map layers
* Expanded wildlife analysis
* More advanced geospatial analysis

---

# Future Improvements

Future versions of Forest Explorer Kenya could include:

* Automated ETL workflows
* More environmental APIs
* Advanced interactive maps
* Forest boundary visualization
* Wildlife hotspot analysis
* Weather analysis
* REST APIs
* Cloud deployment

---

# Author

**Janelle Akinyi**

Data Analytics Student
Zindua Coding School

**Capstone Project — Forest Explorer Kenya**

---

## Project Goal

To bring environmental data together in one platform and make information about **Kenya's forests, wildlife, biodiversity, and conservation** easier to explore and understand.
