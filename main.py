# http://nekoyukimmm.hatenablog.com/entry/2016/05/27/162736
# https://qiita.com/Gen6/items/f1636be0fe479f42b3ee
# https://qiita.com/miyahan/items/7d629d00429c9f032a27


import os
import io
import re
from flask import Flask, jsonify, request, redirect, url_for, send_from_directory, render_template, make_response
from werkzeug import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# limit upload file size : 1MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


UPLOAD_FOLDER = './masks'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        # 拡張子の評価はしてない
        if file:
            filename = secure_filename(file.filename)
            # 保存する処理
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            # 保存しないで処理する
            with file.stream as f:
                new_file, new_filename = convert(f.read().decode('utf-8'), filename)
                if new_file is None:
                    '''<p>エラーが発生しました</p>'''
                else:
                    # レスポンスオブジェクトを作成
                    response = make_response()
                    # レスポンスオブジェクトのdataのセット
                    response.data = new_file
                    # ダウンロード時のファイル名を定義
                    response.headers['Content-Disposition'] = 'attachment; filename=' + new_filename
                    # ダウンロードファイルのmimetypeを設定
                    response.mimetype = "application/octet-stream"
                    return response

            # return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')


@app.route('/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)



# ファイルストリームとファイル名を引数にとる。
# mask データを マスクとカッパーデータにする
def convert(data, filename):

    # (fp_poly 任意の文字列 (layer F.Mask) 任意の文字列)改行があるかも)の繰り返し 改行)EOFとなっているので、
    # このパターンを取得する
    # re.DOTALLで複数行に対応させる .は改行にも使える
    matchObj = re.search("(\(fp_poly.+\(layer F.Mask\).+\).*\))+.{0,1}\)$", data, flags=re.DOTALL)

    # マッチしたとき
    if matchObj:
        # print(matchObj.group()) # マッチした文字列： abc
        # print(matchObj.start()) # マッチした文字列の開始位置： 3
        # print(matchObj.end())   # マッチした文字列の終了位置： 6
        # print(matchObj.span())  # マッチした文字列の開始位置と終了位置： (3, 6)
        # print()
        # 置換
        result = data.replace("F.Mask", "F.Cu")

        # maskを後ろに追記(最後の)と改行はいらないので-2している)
        data = "{}{}".format(result[:-2], matchObj.group())
        # print(data)
    else:
        return None,None

    # pathと拡張子の取得
    root, ext = os.path.splitext(filename)
    # 返す
    new_filename = "{}_and_cu{}".format(root,ext)
    return data, new_filename


if __name__ == '__main__':
    app.run(debug=True, port=8000)
