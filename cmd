# 1. AWS CLIの認証情報を設定（まだ設定していない場合）
aws configure

# 2. ECRリポジトリの作成（まだ存在しない場合）
aws ecr create-repository --repository-name docker-test --region ap-northeast-1

# 3. ECRへのログイン
aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin $(aws sts get-caller-identity --query Account --output text).dkr.ecr.ap-northeast-1.amazonaws.com

# 4. Dockerイメージのビルド（本番用設定を使用）
DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

# 5. イメージにECRリポジトリのタグを付ける
docker tag docker-test:latest $(aws sts get-caller-identity --query Account --output text).dkr.ecr.ap-northeast-1.amazonaws.com/docker-test:latest

# 6. ECRにイメージをプッシュ
docker push $(aws sts get-caller-identity --query Account --output text).dkr.ecr.ap-northeast-1.amazonaws.com/docker-test:latest
