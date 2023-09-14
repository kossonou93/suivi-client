from google.cloud import bigquery

client = bigquery.Client()

query = """
SELECT * 
FROM 'client_client'
"""

query_job = client.query(query)

# Récupérez les résultats de la requête
results = query_job.result()

# Parcourez les résultats
for row in results:
    print(row)