# WhisperTranscription_Docker

## 説明

---

OpenAI が開発した文字起こし翻訳モデル Whisper と Dokcer と Gradio を使用した文字起こしアプリを作ります。

# CPU を使用する場合

```
docker-compose up -d
```

# GPU を使用する場合

## NVIDIA CUDA Toolkit のインストール

```
https://developer.nvidia.com/cuda-toolkit-archive
```

## イメージ選択

マシンの GPU に合わせた Image を選択し、Dockerfile を更新する。

Image は以下

```
https://hub.docker.com/r/pytorch/pytorch/tags?page=1
```

Driver については以下やググった結果を参考にする

```
https://pystyle.info/pytorch-relationship-between-gpu-and-driver-cuda-and-cudnn-versions/
```

## docker-compose.yml 書き換え

GPU 側のコメントアウトを解除

CPU 側をコメントアウト

## 実行

```
docker-compose up -d
```
