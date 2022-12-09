# Page Ratings app

This app, designed to be deployed as a Functions app on DigitalOcean, collects page ratings, given the following environment variables:

- `DB_HOST`
- `DB_USER`
- `DB_DATABASE`
- `DB_PASSWORD`
- `DB_PORT`

## Prerequisites

1. [Optional] This is a Python 3.x app; to run locally, you'll want to install the Python runtime and run `pip install mysql-connector-python`
2. Provision a MySQL server; we recommend the DigitalOcean Managed MySQL database product. Then, create the required schema by executing the SQL contained in the `.sql` file
