--SQL query 


with main as 

(
SELECT 
    CAST(raw.covid_test.date AS DATE) AS IncidentDate,
    CAST(raw.covid_test.cases AS INT) AS TotalNumCases,
    CAST(raw.covid_test.deaths AS INT) AS TotalNumDeaths,
    CAST(raw.covid_test.recovered AS INT) AS TotalNumRecovered
FROM 
    raw.covid_test
)

SELECT * FROM main