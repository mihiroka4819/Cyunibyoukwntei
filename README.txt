# 厨二語録現代語訳検定

55問（5〜1級 各10問＋特級5問）のローカルWebアプリです。

## PCでの一番簡単な使い方（Flaskなし）
1. ZIPを展開する。
2. 中の `index.html` をダブルクリックする。
3. Chrome / Edge / Safariなどでサイトが開く。
4. 階級を選んで開始。

この方法ならPythonのインストールすら不要です。

## Python + Flaskで起動する方法
### 1. Pythonを確認
WindowsならPowerShell、Macならターミナルを開いて：

    python --version

Macで `python` が無い場合は：

    python3 --version

### 2. Flaskをインストール
Windows:

    py -m pip install flask

Mac:

    python3 -m pip install flask

### 3. フォルダへ移動
`app.py` があるフォルダをターミナルで開く。

### 4. 起動
Windows:

    py app.py

Mac:

    python3 app.py

### 5. ブラウザで開く
    http://127.0.0.1:5000/

## 自動解読判定について
入力した回答と模範解答の主要語を比較する簡易ローカル判定です。
本格的なAI採点ではないため、特に特級では「自動判定」より自分の解釈を優先してください。

## 収録
5級 10問
4級 10問
3級 10問
2級 10問
1級 10問
特級 5問

合計55問。
