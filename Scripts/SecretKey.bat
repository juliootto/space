REM Este script gera uma chave secreta segura usando o módulo 'secrets' do Python.
REM A chave gerada é adequada para uso em aplicações web, como chaves de sessão ou tokens CSRF.
python3 -c "import secrets; print(secrets.token_urlsafe(50))"