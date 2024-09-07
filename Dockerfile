# ベースイメージとして AWS Lambda Python ランタイムを使用
FROM --platform=linux/amd64 public.ecr.aws/lambda/python:3.9

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY app.py ${LAMBDA_TASK_ROOT}

# Lambda 関数のハンドラを指定
CMD [ "app.lambda_handler" ]