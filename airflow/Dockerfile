FROM debian:stretch

# TODO: Set this to a building workdir, then set this below for the actual airflow code
ENV WORKDIR="/usr/src/app/"
RUN mkdir -p "${WORKDIR}"
WORKDIR "${WORKDIR}"

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

# APT Requirements
COPY apt-requirements.txt "${WORKDIR}"
RUN apt-get -y update \
  && xargs apt-get install -y < apt-requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
# Python Requirements
COPY requirements.txt "${WORKDIR}"
RUN apt-get update && \
    apt-get install -y g++ python3-dev && \
    pip3 install -r requirements.txt --no-deps --no-cache-dir && \
    apt-get autoremove -y g++ python3-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
