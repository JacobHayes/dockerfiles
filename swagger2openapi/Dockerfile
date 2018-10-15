# TAG jacobhayes/swagger2openapi
#
# To run, use the following:
#     docker run \
#         --rm \
#         --workdir="$PWD" \
#         -v "$PWD:$PWD" \
#         jacobhayes/swagger2openapi
#
FROM node:10-alpine
RUN npm install -g swagger2openapi@3.2.10
ENTRYPOINT ["swagger2openapi"]
