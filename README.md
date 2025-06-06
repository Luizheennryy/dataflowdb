Dataflow Mobres – Smart Data Automation Pipeline

Author: Luiz Henrique Vieira
Role: Data Engineer | Senior Data | Performance Analyst
Status: Production-ready MVP

🚀 Project Overview

dataflow_mobres is a professional-grade Data Engineering pipeline designed to automate the end-to-end ingestion, transformation, and refreshing of analytical data tables in a PostgreSQL environment. It efficiently handles deletion by date, file preparation, loading into staging or fact tables, and materialized view refresh — all from manually extracted .csv files.

🧰 Technologies & Tools Used

Category

Technologies / Tools

Language

Python 3.13

Database

PostgreSQL (local, port 5433)

ML/Forecasting (Future)

XGBoost, LightGBM, Prophet (planned)

Scheduling (Future)

GitHub Actions, Windows Task Scheduler

Version Control

Git + GitHub

Virtual Environment

venv

Encoding Handling

cp1252 > UTF-8

CSV Processing

Python csv, custom cleaner

Logging & Debugging

Python logging

CI/CD (Planned)

GitHub Actions

Environment Config

python-dotenv (.env management)

📂 Project Structure

├── .env                         # Environment variables (DB config)
├── notebooks/                  # Notebooks for EDA or experimentation
├── src/
│   ├── database/               # DB connection, delete, truncate, refresh
│   ├── pipelines/              # Data pipelines (CSV to Postgres)
│   ├── utils/                  # Helpers for file and data handling
│   ├── models/                 # Reserved for ML models (planned)
│   └── files/                  # Reserved for file categorization
├── tests/                      # Pytest test structure (coming soon)
├── main.py                     # Entry point: executes full pipeline
├── extrair_zipados.ipynb       # CSV extraction from VDI (manual step)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

✅ Features Implemented

🧪 Testing (Coming Soon)

Unit tests with pytest

Mocked PostgreSQL test environment

CI trigger for push and pull request on main branch

🧠 Planned Features

Feature

Description

🔁 Scheduling

Auto-run pipeline daily or hourly

🧪 Test coverage

Full test suite on ingestion & DB operations

📊 ML Forecasting

XGBoost / Prophet demand forecasting

📦 Dockerization

Containerize full app for portability

🧩 FastAPI microservice

Endpoint to trigger pipeline on demand

☁️ Cloud Support

Deploy on AWS EC2 or RDS (Phase 2)

🧭 How to Run

Clone this repository:

git clone https://github.com/Luizheennryy/dataflow_mobres.git
cd dataflow_mobres

Create and activate your virtual environment:

python -m venv .venv
source .venv/Scripts/activate  # Windows

Install dependencies:

pip install -r requirements.txt

Set your environment variables in .env:

HOST=localhost
PORT=5433
USER=postgres
PASSWD=22
DATABASE=Projetos

Place updated CSVs in C:/Users/<user>/Desktop/Bases/

Run the pipeline:

python main.py

🤝 Contributing

Contributions are welcome. Please fork the repository, open a branch, and submit a PR. Testing and documentation improvements are especially appreciated!

📩 Contact

Luiz Henrique Dos Santos Vieira – [LinkedIn](https://www.linkedin.com/in/luiz-henrique-santos-vieira/)

Feel free to reach out to discuss data projects, engineering roles, or collaborations.

📌 License

MIT – feel free to use, modify and share with credit. ✨
