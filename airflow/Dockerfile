FROM debian:stretch

ENV BUILDDIR="/usr/src/build/" \
    WORKDIR="/usr/src/app/"
WORKDIR "${BUILDDIR}"

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

# APT Requirements
COPY apt-requirements.txt "${BUILDDIR}"
RUN apt-get update \
  && xargs apt-get install -y < apt-requirements.txt \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get clean
# Python Requirements
COPY requirements.txt "${BUILDDIR}"
RUN apt-get update && \
    apt-get install -y g++ python3-dev && \
    pip3 install -r requirements.txt --no-deps --no-cache-dir && \
    apt-get autoremove -y g++ python3-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get clean

WORKDIR "${WORKDIR}"
COPY entrypoint.sh /
COPY helpers/* /usr/local/bin/
ENTRYPOINT ["/entrypoint.sh"]
