HAGEDOWN
============

Shimehari example.
markdown で書けるメモ帳。
HTML タグは書いても削除されます。

ついでにタグ付けとかできるようにしてみたり。

動作サンプル : http://hagedown.appspot.com/

About
--------------------------------------------------

markdown を使った自分専用メモ帳環境が作れます。

このリポジトリをクローンした後、自分自身で GAE の app_key を取得していれてもらえれば
そのまま使えます。
ライセンスも BSD なんで商用だろうと適当に使ってもらって構いません。

とは言えあくまで Shimehari のサンプルなので
あんまり GAE のリソース対策とかはしてません。セキュリティ云々なんてやってません。
なんかあっても保証しません。
ベーシック認証なり OAuth なりで認証をかけて自分専用で使う分には特に問題ないと思います。

複数人数でとかある程度オープンで動かそうと思うなら適宜 memcache に突っ込んだり
適宜 Task Queues に投げるとかうまいことやったほうがいいと思います。

小粋に markdown 部分だけ css を分けてみたりしているので
カジュアルにそこだけ見た目整えるとかでもいいかもしれません。

依存しているモジュール
------------------------

* shimehari : [https://github.com/glassesfactory/Shimehari](https://github.com/glassesfactory/Shimehari)
* python-markdown : [https://github.com/waylan/Python-Markdown/](https://github.com/waylan/Python-Markdown/)
* jinja2 : [https://github.com/mitsuhiko/jinja2](https://github.com/mitsuhiko/jinja2)
* werkzeug : [https://github.com/mitsuhiko/werkzeug](https://github.com/mitsuhiko/werkzeug)
* formencode : [https://github.com/formencode/formencode](https://github.com/formencode/formencode)


Contact
-----------
* twitter @[__hage__](https://twitter.com/__hage__)