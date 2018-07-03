# TAG jacobhayes/airflow
FROM debian:stretch

ENV BUILDDIR="/usr/src/build/" \
    WORKDIR="/usr/src/app/"

ENV LANG="C.UTF-8" \
    LANGUAGE="C.UTF-8" \
    LC_ALL="C.UTF-8"

WORKDIR "${BUILDDIR}"
# APT Requirements
COPY apt-requirements.txt .
RUN apt-get update && \
  xargs apt-get install -y < apt-requirements.txt && \
  rm -rf /var/lib/apt/lists/* && apt-get clean
# Python Requirements
# Update cryptography to fix pyOpenssl issues
RUN pip3 install --no-cache-dir pipenv "cryptography>=2.2.1"
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --ignore-pipfile

WORKDIR "${WORKDIR}"
ENV AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__LOAD_EXAMPLES="False"
COPY helpers/* /usr/local/bin/
ENTRYPOINT ["airflow"]
