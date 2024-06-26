# Summary PDF File
PDFファイルで作成された論文を読み込み,その概要を体言止めにして出力するプログラムです。<br>
このプログラムを動かしたい場合は"main.py"を実行してください。<br>
また、このプログラムはOpenAIを利用し、APIキーの取得が必須です。<br>
<br>
大まかに以下のような動作でプログラムが実行されます。
1. TKinterで読み込みたいPDFファイルのパスを読み込み
2. PDFファイルからテキストデータを抽出
3. OpenAIのgpt-3.5-turboを利用し文書の要約を指示
4. 要約された文章を句読点で区切って分割
5. 分割されたデータの文章に形態素解析を行い品詞分解
6. 最後に名詞が出るまで各文章の末尾を消し、文章データを統合して出力

# English Description
This program reads a thesis created in a PDF file and outputs a summary of the thesis in a noun-terminated format.

To run this program, run "main.py".

This program also uses OpenAI, so you must obtain an API key.

The program runs roughly as follows:

1. Read the path of the PDF file you want to read with TKinter

2. Extract text data from the PDF file

3. Use OpenAI's gpt-3.5-turbo to instruct the program to summarize the document

4. Split the summarized sentences by separating them with punctuation marks

5. Perform morphological analysis on the split data sentences and break them down into parts of speech

6. Delete the end of each sentence until a noun is found, then integrate and output the sentence data
