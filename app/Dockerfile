# syntax = docker/dockerfile:1.0-experimental
################################################################################
# DCS_IMAGE_REF is set dynamically by the bootstrap script.
################################################################################

ARG DCS_IMAGE_REF
FROM $DCS_IMAGE_REF

# Setup Python project.

ARG SBT_ENVIRONMENT_NAME
ARG prefix=/opt/symbio/${SBT_ENVIRONMENT_NAME}

# Install apt dependencies.
# Add packages to the apt-get install call as necessary.

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install python dependencies.

COPY ./app/requirements.txt ${prefix}/app/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r ${prefix}/app/requirements.txt

# Copy the project content into the image. Uses the repo root as the
# build context in order to include the "infrastructure" directory.

COPY --chown=symbio:symbio ./ ${prefix}/
WORKDIR ${prefix}/app

# Install the project in editable mode.

RUN python3 setup.py develop

# Configuration persists across container runs and is therefore mounted
# from the host filesystem.

VOLUME ${prefix}/configuration

# Add metadata.

ARG SBT_CHECKOUT_ID
LABEL symbio.checkout_id=${SBT_CHECKOUT_ID}
