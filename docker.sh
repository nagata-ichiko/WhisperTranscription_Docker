# コンテナに入り、シェルを起動する
docker exec -it whisper-gpu bash -c "

    # コマンドを実行する
    # pip freeze > requirements_conda.txt
    conda update conda
    conda init
    conda config --set env_prompt '({name})'
    conda config --set default_env py39_env
    conda init
  "

docker exec -it whisper-gpu bash -c "
    # conda install --name py39_env --file requirements_conda.txt
    pip install --upgrade pip --user
    pip install -r requirements.txt  --user
    pip install ctranslate2 OpenNMT-py sentencepiece  --user
    pip install transformers --user
    python src/WhisperGradioApp_CPU.py
"