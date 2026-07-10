# Forest-Explorer-Kenya
An interactive data-driven platform for exploring Kenya's forests, wildlife, biodiversity, and conservation insights.

# Introduction

Forest Explorer Kenya is an end-to-end cloud-based data engineering project that centralizes environmental data about Kenya's forests and wildlife into a single platform.

The project automatically extracts data from multiple public APIs and datasets, processes it through an ETL pipeline, stores it in Google Cloud, and presents the information through a responsive web application.

Instead of manually collecting information from different conservation websites, users can explore forests, wildlife species, biodiversity statistics, weather conditions, and conservation status from one centralized platform.

The project demonstrates modern Data Engineering concepts including ETL pipelines, cloud storage, data warehousing, workflow orchestration, REST APIs, and full-stack web development.

# Problem Statement

Kenya has over 300 forests and thousands of wildlife species spread across multiple ecosystems. However, environmental information is fragmented across government agencies, conservation organizations, research databases, and public APIs.

Students, researchers, tourists, and conservationists often spend significant time searching different platforms for reliable information.

Forest Explorer Kenya solves this challenge by building a centralized cloud platform that automatically collects, processes, stores, and visualizes environmental data.

# Objectives

- Build an automated ETL pipeline for environmental data.

- Integrate multiple APIs into one platform.

- Store raw and processed data in Google Cloud.

- Build a cloud data warehouse using BigQuery.

- Develop REST APIs using FastAPI.

- Create a responsive React web application.

- Provide interactive dashboards and maps.

- Demonstrate an end-to-end Data Engineering workflow.

# Architecture

             External Data Sources

      GBIF API
      IUCN Red List API
      Kenya Forest Service
      OpenWeather API

               │
               ▼

        Python ETL Pipeline

               │
               ▼

         Apache Airflow

               │
               ▼

     Google Cloud Storage

               │
               ▼

      Google BigQuery

               │
      ┌────────┴────────┐
      ▼                 ▼

 PostgreSQL         FastAPI

      │                 │
      └────────┬────────┘
               ▼

        React Web App

               ▼

             Users

# Components

**GBIF API** - Provides biodiversity and wildlife occurrence records.

**IUCN Red List API** - Provides conservation status for species.

**Kenya Forest Service Dataset** - Contains information about Kenya's forests including location, size, and descriptions.

**OpenWeather API** - Provides real-time weather conditions for each forest.

**Python** - Responsible for extracting, cleaning, validating, and transforming environmental data.Libraries used: Requests, Pandas and NumPy.

**Apache Airflow** - Automates and orchestrates the ETL workflow.Responsibilities: Schedule data extraction ,Execute ETL jobs ,Monitor workflows and Load processed data.

**Google Cloud Storage** - Acts as the project's Data Lake. Stores: Raw JSON, Raw CSV, Images and Logos.

**Google BigQuery** - Cloud Data Warehouse used for analytical queries and reporting.

**PostgreSQL** - Stores application-specific data such as users, favourites, and saved searches.

**FastAPI** - Provides REST APIs that connect the frontend with the database.

**React** - Responsive frontend used to display:

- Dashboard
- Forest Explorer
- Wildlife Explorer
- Interactive Map
- Weather
- Conservation Dashboard

# ETL Workflow

Extract

↓

GBIF API
KFS Dataset
Weather API

↓

Transform

Remove duplicates

Standardize names

Clean coordinates

Handle missing values

↓

Load

Google Cloud Storage

↓

BigQuery

↓

FastAPI

↓

React Website

# Features

**Forest Explorer**

Search and browse Kenya's forests.

**Wildlife Explorer**

Explore wildlife species with conservation information.

**Interactive Map**

Locate forests and protected areas.

**Weather Dashboard**

Current weather conditions for selected forests.

**Statistics Dashboard**

Visualize biodiversity and conservation data.

**Search Engine**

Search forests, wildlife, and species.

# Tech Stack

| *Category*      | *Technology*          |
| --------------- | --------------------- |
| Programming     | Python                |
| Backend         | FastAPI               |
| Frontend        | React                 |
| Database        | PostgreSQL            |
| ETL             | Apache Airflow        |
| Data Processing | Pandas                |
| Cloud Storage   | Google Cloud Storage  |
| Data Warehouse  | BigQuery              |
| Maps            | Leaflet / Google Maps |
| Version Control | GitHub                |
| Deployment      | Google Cloud Run      |

# Author

Janelle Akinyi

Capstone Project – End-to-End Cloud Data Engineering
