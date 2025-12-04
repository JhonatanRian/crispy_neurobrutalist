# 📚 Documentação - Crispy Neurobrutalist

Bem-vindo à documentação completa do Crispy Neurobrutalist!

## 📖 Guias Principais

### Começando

- **[README.md](README.md)** - Visão geral do projeto, recursos e exemplos básicos
- **[INSTALLATION.md](INSTALLATION.md)** - Guia completo de instalação e configuração
- **[CHANGELOG.md](CHANGELOG.md)** - Histórico de versões e mudanças

### Desenvolvimento

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guia para contribuir com o projeto
- **[pyproject.toml](pyproject.toml)** - Configuração do projeto e dependências

## 🎯 Links Rápidos

### Para Usuários

| O que você quer fazer? | Onde encontrar |
|------------------------|----------------|
| Instalar o pacote | [INSTALLATION.md](INSTALLATION.md#installation-methods) |
| Configurar no Django | [INSTALLATION.md](INSTALLATION.md#django-configuration) |
| Ver exemplos de uso | [README.md](README.md#usage) |
| Personalizar estilos | [README.md](README.md#customization) |
| Resolver problemas | [INSTALLATION.md](INSTALLATION.md#troubleshooting) |
| Ver CSS necessário | [neurobrutalist.css](neurobrutalist.css) |

### Para Desenvolvedores

| O que você quer fazer? | Onde encontrar |
|------------------------|----------------|
| Configurar ambiente de dev | [CONTRIBUTING.md](CONTRIBUTING.md#development-setup) |
| Executar testes | [CONTRIBUTING.md](CONTRIBUTING.md#running-tests) |
| Entender a estrutura | [.github/copilot-instructions.md](.github/copilot-instructions.md) |
| Fazer um PR | [CONTRIBUTING.md](CONTRIBUTING.md#pull-request-process) |
| Ver roadmap | Issues no GitHub |

## 📂 Estrutura da Documentação

```
crispy_neurobrutalist/
├── README.md                          # Visão geral e guia rápido
├── INSTALLATION.md                    # Instalação e configuração detalhada
├── CONTRIBUTING.md                    # Guia para contribuidores
├── CHANGELOG.md                       # Histórico de versões
├── neurobrutalist.css                 # Arquivo CSS de exemplo
├── pyproject.toml                     # Configuração do projeto
├── MANIFEST.in                        # Arquivos incluídos no pacote
│
├── .github/
│   └── copilot-instructions.md        # Documentação técnica interna
│
└── src/crispy_neurobrutalist/
    ├── __init__.py                    # Exports principais
    ├── apps.py                        # Configuração Django App
    ├── layout.py                      # Componentes de layout
    ├── neurobrutalist.py              # CSSContainer
    ├── py.typed                       # Marker para type checking
    │
    ├── templates/neobrutalist/        # Templates Django
    │   ├── field.html
    │   ├── uni_form.html
    │   ├── errors.html
    │   └── layout/                    # Templates de widgets
    │       ├── checkbox.html
    │       ├── select.html
    │       ├── radioselect.html
    │       └── ...
    │
    └── templatetags/                  # Template tags customizadas
        ├── neo_field.py
        └── neuro_filters.py
```

## 🚀 Início Rápido

### 1. Instalação

```bash
pip install crispy-neurobrutalist
```

### 2. Configuração

```python
# settings.py
INSTALLED_APPS = [
    'crispy_forms',
    'crispy_neurobrutalist',
]

CRISPY_TEMPLATE_PACK = "neobrutalist"
```

### 3. Uso no Template

```django
{% load crispy_forms_tags %}

<form method="post">
    {% csrf_token %}
    {{ form|crispy }}
</form>
```

### 4. Incluir CSS

```html
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="{% static 'css/neurobrutalist.css' %}">
```

Para instruções completas, veja [INSTALLATION.md](INSTALLATION.md).

## 🎨 Recursos

- ✅ **Template Pack Completo** - Todos os widgets Django estilizados
- ✅ **Componentes Customizados** - Botões com variantes de cores
- ✅ **CSS Customizável** - Estende facilmente com suas próprias classes
- ✅ **Type Hints** - Suporte completo para type checking
- ✅ **Bem Documentado** - Guias detalhados e exemplos

## 📝 Convenções de Documentação

### Formato dos Guias

Todos os guias seguem estas convenções:

- **Títulos claros e descritivos**
- **Exemplos de código** com syntax highlighting
- **Notas e avisos** claramente marcados
- **Links cruzados** para documentação relacionada
- **Seções de troubleshooting** quando relevante

### Exemplos de Código

Os exemplos sempre incluem:
- Contexto de onde o código deve ser colocado
- Comentários explicativos quando necessário
- Outputs esperados quando relevante

### Versionamento

- Seguimos [Semantic Versioning](https://semver.org/)
- Todas as mudanças documentadas no [CHANGELOG.md](CHANGELOG.md)
- Breaking changes claramente indicadas

## 🤝 Contribuindo

Encontrou um erro na documentação? Quer melhorar algo?

1. Abra uma [issue](https://github.com/JhonatanRian/crispy_neurobrutalist/issues)
2. Faça um fork e crie um PR
3. Veja o [guia de contribuição](CONTRIBUTING.md)

## 📧 Suporte

- **Issues**: [GitHub Issues](https://github.com/JhonatanRian/crispy_neurobrutalist/issues)
- **Discussões**: [GitHub Discussions](https://github.com/JhonatanRian/crispy_neurobrutalist/discussions)
- **Email**: jhonatanrian@zohomail.com

## 📜 Licença

Este projeto é licenciado sob CC BY-NC 4.0. Veja [LICENSE](LICENSE) para detalhes.

---

**Última atualização**: 3 de dezembro de 2025
