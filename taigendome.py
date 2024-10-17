import MeCab
import re

# 関数の定義
# 文章を句読点で区切ってリスト化する関数
def divide_sentences(text):
    # 正規表現を使用して句点または読点で分割
    sentences = re.split('[。、，．]', text)
    # 最後の要素が空文字列の場合、それを取り除く
    if sentences[-1] == '':
        sentences = sentences[:-1]
    return sentences

# 体言止めする関数
def taigendome(text_list):
    # 名詞以外の単語を入れるための空のリスト
    not_noun_list = []
    taigen_text = [] # 体言止めしたtextを格納する場所
    # リストごとに形態素解析
    for sentence in text_list:
        parse = MeCab.Tagger().parse(sentence)
        lines = parse.split("\n")
        items = list(re.split("[\t,]", line) for line in lines)
        #EOSと空のリストを削除
        while items != []:
            if len(items[-1]) >= 2:
                break
            del items[-1]

        # 名詞が出るまで後ろから単語を抽出
        while items != []:
            if items[-1][1] == "名詞":
                # senstenceの文の末尾が名詞なるように後ろから削除
                del_sentence = "".join(not_noun_list)
                end_noun_sentence = sentence.replace(f"{del_sentence}","")
                # not_noun_listの初期化(次の文の体言止め処理でも利用するため)
                not_noun_list = []
                taigen_text.append(end_noun_sentence)
                print(end_noun_sentence)
                break
            # 名詞以外の単語を抽出しリストに格納
            not_noun = items.pop(-1)
            not_noun_list.insert(0,not_noun[0])
    return "\n".join(taigen_text) #taigen_textはリストなのでここで合算して1つの文字列を出力してtxtファイルに保存する下準備

if __name__ == "__main__":
    test = "これはテストです。末尾の単語を消去して、体言止めの文章を生成できます。"
    test_sentence = divide_sentences(test)
    taigendome(test_sentence)