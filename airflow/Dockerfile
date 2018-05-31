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
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir

WORKDIR "${WORKDIR}"
ENV AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__AIRFLOW_HOME="${WORKDIR}"
COPY entrypoint.sh /
COPY helpers/* /usr/local/bin/
ENTRYPOINT ["/entrypoint.sh"]
