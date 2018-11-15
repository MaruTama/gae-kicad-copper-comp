# これは何？
kicad の銅箔むき出しコンポーネントの作成するアプリ  

# どの様に使う？
maskのkicad_modをアップロードすると、maskとcuのコンポーネントに成って落ちてくる  

# ref
- [Quickstart for Python 3 in the App Engine Standard Environment](https://cloud.google.com/appengine/docs/standard/python3/quickstart)  
- [app.yaml Reference](https://cloud.google.com/appengine/docs/standard/python3/config/appref)  
公式

- [PythonのFlaskアプリをGoogle App Engineにデプロイしてみた](https://qiita.com/kai_kou/items/775bcc058aaabbdff4e7)  
python3での貴重な資料

- [Google App Engine (GAE)でDjangoアプリケーションをデプロイする](https://loft.tokyo/post/gae/)  
GAEの全体の流れが分かりやすい


## ファイルのアップロードのために
- [<Flask> Uploading](http://nekoyukimmm.hatenablog.com/entry/2016/05/27/162736)
- [Flaskで画像アップローダー](https://qiita.com/Gen6/items/f1636be0fe479f42b3ee)
- [Flask にアップロードされたCSVファイルを保存せずに読み込む](https://qiita.com/miyahan/items/7d629d00429c9f032a27)

## ファイルのダウンロードのために
- [Flaskでファイルダウンロードを実現する３つの方法](https://qiita.com/5zm/items/760000cf63b176be544c)

# 環境
```
# すべてのバージョンを表示する
$ pyenv versions

# コマンド python3 python2 のverを設定する.  python は3.6.4
$ pyenv shell 3.5.0 2.7.14
# pipの設定変更するため
$ pyenv global 3.5.0
$ pyenv rehash
$ pip install --upgrade distribute
$ pip install  -r requirements.txt

# update
$ gcloud components update
$ gcloud projects list
# デフォルトのプロジェクトIDをセット
$ gcloud config set project silicon-axle-159205

# デプロイ
# 支払い情報が登録されていなくてエラーでて躓いた
$ gcloud auth login
$ gcloud app deploy app.yaml
$ gcloud app browse
```
