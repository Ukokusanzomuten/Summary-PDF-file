import summary
import read_paper
import taigendome
import tk_pdf
import os

pdf_path = tk_pdf.select_pdf_file()
input_text = read_paper.read_pdf(pdf_path)
out_list = []

# input_textが長すぎるとOpenAIのトークンの上限に到達してしまうので区切る
max_token = 10000 #トークンの最大 今回は10000に設定
#リストを分割して格納 (max_token)の数値を文字数の単位として区切る
input_list = [input_text[i:i + max_token] for i in range(0, len(input_text), max_token)]

# 各リストを要約し体言止めで出力
for sammary_input in input_list:
    summary_text = summary.summarize_text(sammary_input)
    # print(summary_text)
    txt_list = taigendome.divide_sentences(summary_text)
    output_text = taigendome.taigendome(txt_list)
    out_list.append(output_text)

# リストごとの要約文リストを繋げる
txt_all = "\n".join(out_list)

# ファイルに書き込む
with open(f"summary\\{os.path.basename(pdf_path)[:-4]}_summary.txt", "w", encoding="utf-8") as file:
    file.write(txt_all)

print("改行付きでファイルが保存されました。")
