# elasticsearch_wiki_test

## 以下準備

`jawiki-latest-pages-articles.xml.bz2`を用意

```
git clone https://github.com/attardi/wikiextractor
 wikiextractor/WikiExtractor.py -b 80M -o extracted jawiki-latest-pages-articles.xml.bz2 --json
```