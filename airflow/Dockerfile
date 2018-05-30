FROM debian:stretch

ENV BUILDDIR="/usr/src/build/" \
    WORKDIR="/usr/src/app/"

WORKDIR "${BUILDDIR}"
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && apt-get clean
# APT Requirements
COPY apt-requirements.txt .
RUN apt-get update \
  && xargs apt-get install -y < apt-requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
# Python Requirements
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y g++ python3-dev && \
    pip3 install -r requirements.txt --no-deps --no-cache-dir && \
    apt-get autoremove -y g++ python3-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

WORKDIR "${WORKDIR}"
ENV AIRFLOW_HOME="${WORKDIR}" \
    AIRFLOW__CORE__AIRFLOW_HOME="${WORKDIR}"

# Configure newer logging config for easier remote logging to gcs/s3.
COPY log_config.py config/
# Set the custom logging class and update the default task reader, which was renamed in future versions
ENV AIRFLOW__CORE__LOGGING_CONFIG_CLASS="log_config.DEFAULT_LOGGING_CONFIG" \
    AIRFLOW__CORE__REMOTE_BASE_LOG_FOLDER="" \
    AIRFLOW__CORE__REMOTE_LOGGING="False" \
    AIRFLOW__CORE__REMOTE_LOG_CONN_ID="google_cloud_default" \
    AIRFLOW__CORE__TASK_LOG_READER="task"

COPY entrypoint.sh /
COPY helpers/* /usr/local/bin/
ENTRYPOINT ["/entrypoint.sh"]
