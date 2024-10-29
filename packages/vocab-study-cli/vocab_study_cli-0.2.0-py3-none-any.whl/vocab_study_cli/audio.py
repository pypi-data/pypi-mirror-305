from pathlib import Path
import os
from dotenv import load_dotenv
from openai import OpenAI

# .envファイルから環境変数を読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
media_path = os.getenv("MEDIA_PATH")

# OpenAIクライアントの初期化
client = OpenAI(api_key=api_key)

# 読み上げるテキストとファイル名
text = "October is the tenth month of the year."
file_name = "october.mp3"
output_path = Path(media_path) / file_name

# TTSリクエストを送信して音声を生成
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",  # 他にも 'echo', 'fable', 'onyx', 'nova', 'shimmer' などが利用可能
    input=text
)

# 音声をMP3として保存
response.stream_to_file(output_path)

print(f"MP3ファイルが生成され、{output_path}に保存されました。Ankiのカードに[sound:{file_name}]と記述して音声を追加できます。")

