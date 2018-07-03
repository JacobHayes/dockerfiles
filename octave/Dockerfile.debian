# TAG jacobhayes/octave:debian
#
#  docker run \
#    --rm \
#    -it \
#    -v="$PWD:/host" \
#    --workdir=/host \
#    jacobhayes/octave:debian
FROM debian:stretch-backports
ENV VERSION 4.4.0-3~bpo9+1
LABEL maintainer "Jacob Hayes <jacob.r.hayes@gmail.com>"
LABEL version $VERSION

RUN apt-get update && apt-get install -t stretch-backports --no-install-recommends -y \
        ghostscript \
        gnuplot \
        less \
        libopenblas-base \
        octave=$VERSION \
        pstoedit \
    && rm -rf /var/lib/apt/lists/*
ENTRYPOINT ["octave-cli"]
