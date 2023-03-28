from multiprocessing.sharedctypes import Value
import whisper
import gradio as gr 
from datetime import timedelta
from srt import Subtitle
import srt
# モデル選択、下に行くほどデカくて遅いが高精度
# model = whisper.load_model("tiny")
# model = whisper.load_model("base")
# model = whisper.load_model("small")
# model = whisper.load_model("medium")
# model = whisper.load_model("large")
model = whisper.load_model("large-v2")

def speechRecognitionModel(input): 
    result = model.transcribe(input, verbose=True, language="ja")    
    seginfo = result["segments"]
    out_text = []
    # segment情報から発言の開始/終了時間とテキストを抜き出し、srt形式で編集する
    for data in seginfo:
        start = data["start"]
        end = data["end"]
        text = data["text"]
        out_line = Subtitle(index=1,\
                            start=timedelta(seconds=timedelta(seconds=start).seconds,\
                            microseconds=timedelta(seconds=start).microseconds),\
                            end=timedelta(seconds=timedelta(seconds=end).seconds,\
                            microseconds=timedelta(seconds=end).microseconds),\
                            content=text,\
                            proprietary='')
        out_text.append(out_line)
    with open("sample" + ".csv", mode="w", encoding="utf-8") as f:
        origin = srt.compose(out_text)
        origin = origin.replace(",",".")
        origin = origin.replace("\n",",")
        origin = origin.replace(",,","\n")
        f.write(origin)
    
    return result

def changeInputTypeVideo():
    gr.Interface(    
        title = 'Whisper Sample App', 
        fn=speechRecognitionModel, 
        inputs=[
            # 動画ファイル
            gr.Video(type="filepath")
        ],
        outputs=[
            "textbox"
        ],
        live=True).launch()

def changeInputTypeAudio():
    gr.Interface(    
        title = 'Whisper Sample App', 
        fn=speechRecognitionModel, 
        inputs=[
            # 音声ファイル
            gr.Audio(type="filepath")
        ],
        outputs=[
            "textbox"
        ],
        live=True).launch()

def changeInputTypeMic():
    gr.Interface(    
        title = 'Whisper Sample App', 
        fn=speechRecognitionModel, 
        inputs=[
            # マイク入力
            gr.inputs.Audio(source="microphone", type="filepath")        
        ],
        outputs=[
            "textbox"
        ],
        live=True).launch()


gr.Interface(
    title = 'Whisper Sample App', 
    fn=speechRecognitionModel, 
    inputs=[
        # 動画ファイル
        gr.Video(type="filepath")
    ],
    outputs=[
        "textbox"
    ],
    live=True).launch()