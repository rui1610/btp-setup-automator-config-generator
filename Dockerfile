##################################################################################################################################################
# LICENSE
# This Dockerfile is provided under the LICENSE defined in the Github repository
# at https://github.com/SAP-samples/btp-setup-automator
##################################################################################################################################################
# Now putting all pieces together 
##################################################################################################################################################
FROM python:3.9.9-alpine3.15
ENV USERNAME=user
ENV HOME_FOLDER /home/$USERNAME
ENV LIBS_FOLDER $HOME_FOLDER/libs
ENV CONTAINER_NAME=btp-setup-automator-config-generator
COPY requirements.txt /tmp/pip-tmp/requirements.txt

# Add config folders according to https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html
ENV XDG_CONFIG_HOME=$HOME_FOLDER/.config
ENV XDG_DATA_HOME=$HOME_FOLDER/.local/share
ENV XDG_STATE_HOME=$HOME_FOLDER/.local/state

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$HOME_FOLDER" \
    --no-create-home \
    "$USERNAME" \
    && apk update \
    && apk upgrade \
    && apk add --no-cache \
               bash \
               coreutils \
               git \
               jq \
               sudo \
    && pip install --no-cache-dir -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp \
    ## Set the right timezone in the container image
    && cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime \
##########################################################################################
# Add user to sudo user
##########################################################################################
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

##########################################################################################
# Fill the image with the necessary resources
##########################################################################################
USER $USERNAME
WORKDIR $HOME_FOLDER

## Copy over the all necessary resources
COPY --chown=$USERNAME:$USERNAME libs/python/generator  $HOME_FOLDER/
COPY --chown=$USERNAME:$USERNAME templates              $HOME_FOLDER/templates/
COPY --chown=$USERNAME:$USERNAME libs/python/helper*.py $LIBS_FOLDER/python/
COPY --chown=$USERNAME:$USERNAME .vscode                $HOME_FOLDER/.vscode/

# For using outside of VS Code context:
CMD ["bash"]
