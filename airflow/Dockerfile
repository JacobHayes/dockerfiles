# TAG jacobhayes/airflow
FROM python:3.7-slim

ENV BUILDDIR="/usr/src/build/" \
    WORKDIR="/usr/src/app/"

ENV LANG="C.UTF-8" \
    LANGUAGE="C.UTF-8" \
    LC_ALL="C.UTF-8"

WORKDIR "${BUILDDIR}"
# APT Requirements - Airflow deps require compiled packages
COPY apt-requirements.txt .
RUN apt-get update && \
    xargs apt-get install -y < apt-requirements.txt && \
    rm -rf /var/lib/apt/lists/* && apt-get clean
# Python Requirements
RUN pip3 install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock ./
RUN SLUGIFY_USES_TEXT_UNIDECODE=yes pipenv install --deploy --system

WORKDIR "${WORKDIR}"
ENV AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__LOAD_EXAMPLES="False"
COPY helpers/* /usr/local/bin/
ENTRYPOINT ["airflow"]
