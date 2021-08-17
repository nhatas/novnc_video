
FROM debian:testing

RUN sed -i -e 's/ main/ main contrib non-free/g' /etc/apt/sources.list && \
    set -ex; \
    apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      bash \
      bzip2 \
      curl \
      ffmpeg \
      flatpak \
      fluxbox \
      git \
      make \
      mpv \
      nano \
      novnc \
      pulseaudio \
      screen \
      supervisor \
      streamlink \
      unzip \
      wget \
      x11vnc \
      xterm \
      xvfb \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists

# Setup demo environment variables
ENV HOME=/root \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1920 \
    DISPLAY_HEIGHT=1080 \
    RUN_XTERM=yes \
    RUN_FLUXBOX=yes

RUN sed -i -e 's/encs.push(encodings.pseudoEncodingQualityLevel0 + 6);/encs.push(encodings.pseudoEncodingQualityLevel0 + 9);/g' /usr/share/novnc/core/rfb.js
RUN sed -i -e 's/encs.push(encodings.pseudoEncodingCompressLevel0 + 2);/encs.push(encodings.pseudoEncodingCompressLevel0 + 0);/g' /usr/share/novnc/core/rfb.js

WORKDIR /app
COPY . /app

CMD ["/bin/bash"]