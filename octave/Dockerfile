# TAG jacobhayes:octave
#
#  docker run \
#    --rm \
#    -it \
#    -v="$PWD:/host" \
#    --workdir=/host \
#    jacobhayes/octave
FROM alpine:latest
ENV VERSION 4.2.0-r1
LABEL maintainer "Jacob Hayes <jacob.r.hayes@gmail.com>"
LABEL version $VERSION

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add --no-cache "octave==$VERSION"
ENTRYPOINT ["octave-cli"]
