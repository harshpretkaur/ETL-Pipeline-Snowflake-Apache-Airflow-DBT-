# Use Astronomer's Astro Runtime as the base image
FROM quay.io/astronomer/astro-runtime:10.3.0

# Create a Python virtual environment, activate it, install dbt-snowflake, then deactivate
RUN python -m venv dbt_venv && \
    source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && \
    deactivate
