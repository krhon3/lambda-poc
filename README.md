# Run the following commands
```bash
pip-compile --output-file=pip-files/requirements.txt pip-files/requirements.in 
```

```bash
pyenv local 3.9.6&python -m venv .venv&.venv\Scripts\activate&python -m pip install pip-tools&pip install --upgrade pip-tools&pip install --no-cache-dir -U pip setuptools wheel&pip install -r pip-files/requirements.txt
```

```bash
npm i -g serverless
```

```bash
serverless plugin install -n serverless-python-requirements --stage test&serverless plugin install -n serverless-s3-remover --stage test&sls deploy --stage test --verbose
```
