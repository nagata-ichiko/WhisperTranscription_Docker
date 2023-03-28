FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-runtime

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    git \
    python3-tk \
    portaudio19-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*  

RUN pip install --upgrade pip
COPY requirements.txt /root/
WORKDIR /root/
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/WhisperGradioApp.py"]