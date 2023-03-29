# コンテナに入り、シェルを起動する
docker exec -it whisper-gpu bash -c "

    # コマンドを実行する
    # pip freeze > requirements_conda.txt
    conda init
    echo 'conda activate py39_env' >> ~/.bashrc
    conda config --set env_prompt '({name})'
    conda config --set default_env py39_env
    conda init
    pip install --upgrade pip
    pip install -r requirements_conda.txt
    pip install -r requirements.txt
    pip install ctranslate2 OpenNMT-py sentencepiece
    pip install transformers
    python src/WhisperGradioApp_CPU.py
"