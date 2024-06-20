import summary
import read_paper
import taigendome
import tk_pdf

pdf_path = tk_pdf.select_pdf_file()
input_text = read_paper.read_pdf(pdf_path)

# input_textが長すぎるとOpenAIのトークンの上限に到達してしまうので区切る
max_token = 10000 #トークンの最大 今回は10000に設定
#リストを分割して格納 (max_token)の数値を文字数の単位として区切る
input_list = [input_text[i:i + max_token] for i in range(0, len(input_text), max_token)]

# 各リストを要約し体言止めで出力
for sammary_input in input_list:
    summary_text = summary.summarize_text(sammary_input)
    # print(summary_text)
    txt_list = taigendome.divide_sentences(summary_text)
    taigendome.taigendome(txt_list)