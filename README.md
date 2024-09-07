# Readmeファイルの作成


開発環境では以下のdockerコードを使用してローカルで実行できます。

```bash
docker-compose -f docker-compose.yml build
```


本番環境では以下のdockerコードを使用してローカルで実行できます。

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
```
