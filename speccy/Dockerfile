# TAG jacobhayes/speccy
#
# To run, use the following:
#     docker run \
#         --rm \
#         --workdir="$PWD" \
#         -v "$PWD:$PWD" \
#         jacobhayes/speccy
#
FROM node:10-alpine
RUN npm install -g speccy@0.8.1
ENTRYPOINT ["speccy"]
