# HappyTech Link Shortener

Encurtador de URLs baseado em regras do Apache, para campanhas e produtos HappyHouse. Não utiliza PHP, banco de dados ou serviços externos.

## Link disponível

| URL curta (após instalação) | Destino | Código |
| --- | --- | --- |
| `https://happytech.com.br/go/mappy` | `https://happytech.com.br/apps/happyhouse/external/products/mappy/` | `302` |

> O link curto somente funcionará depois que o arquivo for publicado e o Apache estiver configurado. Este repositório não publica automaticamente no servidor.

## Estrutura

```text
.
├── .github/workflows/validate.yml
├── docs/INSTALL.md
├── go/.htaccess
├── tests/test_redirects.py
├── .gitignore
├── CHANGELOG.md
├── README.md
└── VERSION
```

## Instalação

Consulte [docs/INSTALL.md](docs/INSTALL.md). Instale **apenas** `go/.htaccess` no diretório `/go` da raiz pública do domínio. Não substitua o `.htaccess` da raiz.

## Novo atalho

Adicione uma regra em `go/.htaccess`, antes de `Options -Indexes`:

```apache
RewriteRule ^nova-campanha/?$ https://happytech.com.br/destino/ [R=302,L,NE,NC]
```

Evite usar parâmetros de destino não confiáveis. Mantenha os destinos definidos explicitamente para não criar um redirecionador aberto.

## Testes

Execute `python3 -m unittest discover -s tests -v`. O workflow GitHub Actions valida a configuração de forma estática; não substitui o teste de integração no Apache de produção.

## Autoria

Fabio Castilhos <fabcastilhos@gmail.com> | HappyHouse.

## Licenciamento

Nenhuma licença de redistribuição foi definida neste pacote. Defina a política de licenciamento da organização antes de tornar o repositório público ou aceitar contribuições externas.
