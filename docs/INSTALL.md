# Instalação e homologação

1. Confirme que o domínio `happytech.com.br` utiliza Apache com `mod_rewrite` ativo.
2. Confirme que a configuração do VirtualHost permite leitura de `.htaccess` e as diretivas usadas: `AllowOverride FileInfo Options` ou `AllowOverride All`. Em hospedagens restritas, solicite ajuste ao administrador.
3. Crie a pasta `go` dentro do DocumentRoot de `happytech.com.br`.
4. Envie o arquivo `go/.htaccess` para a pasta criada. Não envie o README ou os arquivos de desenvolvimento ao DocumentRoot.
5. Teste a resposta:

```bash
curl -sS -I https://happytech.com.br/go/mappy
```

A resposta esperada é `302` e o cabeçalho `Location: https://happytech.com.br/apps/happyhouse/external/products/mappy/`.

## Observações operacionais

- Se houver regras herdadas do `.htaccess` da raiz, valide possíveis conflitos.
- O uso de `Options -MultiViews` e `Options -Indexes` exige permissão `AllowOverride Options` (ou `All`).
- O código `302` evita indicar redirecionamento permanente durante campanhas.
- Para atualizar o destino, edite somente a regra correspondente, faça commit e publique o arquivo.
- O repositório não contém credenciais, pipeline de deploy nem painel de métricas.
