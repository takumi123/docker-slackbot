import html
from flask import Flask, jsonify, make_response, render_template_string
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

llm = OpenAI(temperature=0.7)

prompt = PromptTemplate(
    input_variables=["product"],
    template="{product}を作る会社の社名として、何かいいものはないですか？日本語の社名でお願いします。",
)

chain = LLMChain(llm=llm, prompt=prompt)

# HTMLテンプレートを文字列として定義
html_template = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Response Test</title>
</head>
<body>
    <h1>API Test Page</h1>
    <div id="response"></div>

    <script>
    fetch('/api/hello')
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = data.message;
        })
        .catch(error => console.error('Error:', error));
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/api/hello')
def hello():
    prediction = chain.run("カラフルな靴下")
    decoded_data = html.unescape(prediction.strip())
    response = {
        "message": decoded_data
    }
    resp = make_response(jsonify(response))
    print(resp)
    resp.headers['Content-Type'] = 'application/json; charset=utf-8'
    return resp

def lambda_handler(event, context):
    with app.app_context():
        return hello().get_data(as_text=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)