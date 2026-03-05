# AI FC Bus Safety System

An AI-assisted system for evaluating Fitness Certificates (FC) for public transport buses using inspection data.

## Problem
Manual FC inspections can be inconsistent and sometimes unsafe buses receive certification. This system introduces AI-based risk evaluation to support inspectors.

## Solution
Inspection data is analyzed using rule-based thresholds and a machine learning model to determine whether a bus should be:

- PASS
- CONDITIONAL (needs monitoring)
- REJECT

## Project Structure

ai-fc-bus-safety-system
│
├── README.md
├── docs
├── dataset
├── backend
├── frontend
└── api

## Tech Stack
- Python
- Flask API
- Scikit-learn
- HTML Dashboard

## Workflow
1. Input bus inspection data
2. AI predicts safety risk
3. System outputs certification decision
4. Dashboard displays result

## Future Scope
- IoT vehicle sensors
- Government transport API integration
- Predictive fleet maintenance
