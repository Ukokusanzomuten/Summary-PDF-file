import openai
import os

# OpenAIのAPIキーを設定します
openai.api_key = os.environ['OPENAI_API_KEY']

def summarize_text(text):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"以下の文章の概要を作成してください:\n\n{text}\n\n概要:"}
    ],
    # この変数は欲しい文章に合わせて調整してください
    max_tokens=300,
    n=1,
    stop=None,
    temperature=0.1
    )
    
    summary = response.choices[0].message['content'].strip()
    return summary
