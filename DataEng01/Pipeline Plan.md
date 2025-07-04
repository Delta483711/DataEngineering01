## COVID-19 Tracker Pipeline Plan

### Extract
- Use Python to pull data from GOV.UK COVID API or OWID.
- Fetch and store daily stats (cases, deaths, vaccinations, etc.).

### Load
- Insert data into `raw.uk_covid_daily`.

### Transform
- Clean and convert data types in `staging.uk_covid_summary`.
- Add rolling 7-day averages and regional comparisons.

### Tools
- Python (Requests, Pandas), Neon, dbt, Git, VS Code