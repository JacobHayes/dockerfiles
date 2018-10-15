# TAG jacobhayes/swagger-cli
#
# To run, use the following:
#     docker run \
#         --rm \
#         --workdir="$PWD" \
#         -v "$PWD:$PWD" \
#         jacobhayes/swagger-cli
#
FROM node:10-alpine
RUN npm install -g swagger-cli@2.1.3
ENTRYPOINT ["swagger-cli"]
