# TAG jacobhayes/airflow
FROM python:3.7-slim

ENV BUILDDIR="/usr/src/build/" \
    WORKDIR="/usr/src/app/"

ENV LANG="C.UTF-8" \
    LANGUAGE="C.UTF-8" \
    LC_ALL="C.UTF-8" \
    SLUGIFY_USES_TEXT_UNIDECODE=yes

WORKDIR "${BUILDDIR}"
# APT Requirements - Airflow deps require compiled packages
COPY apt-requirements.txt .
RUN apt-get update && \
    xargs apt-get install -y < apt-requirements.txt && \
    rm -rf /var/lib/apt/lists/* && apt-get clean
# Python Requirements
RUN pip3 install --no-cache-dir pipenv==v2018.10.13
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system
# Compile the static assets - these are only generated/bundled with releases.
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -sL https://deb.nodesource.com/setup_10.x | \
        bash - && \
    apt-get install -y nodejs && \
    cd src/apache-airflow && \
    python setup.py compile_assets && \
    apt-get autoremove -y curl gnupg nodejs && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

WORKDIR "${WORKDIR}"
ENV AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__LOAD_EXAMPLES="False"
ENTRYPOINT ["airflow"]
