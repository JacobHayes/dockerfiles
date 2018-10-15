# TAG jacobhayes/firebase-cli
#
# To run, use the following:
    # docker run \
    #     --rm \
    #     --workdir="$PWD" \
    #     -i \
    #     -p 9005:9005 \
    #     -v "$HOME/.config/configstore/:/root/.config/configstore/" \
    #     -v "$PWD:$PWD" \
    #     jacobhayes/firebase-cli
#
# The port forward is required for the `login` subcommand. If you have port conflicts, you can authenticate with the
# `login` url and then exec into the container and run `wget` on the redirected url.
FROM node:10-alpine
RUN npm install -g firebase-tools
ENTRYPOINT ["firebase"]
