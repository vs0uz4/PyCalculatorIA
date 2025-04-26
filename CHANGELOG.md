# Changelog

Todas as alterações notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.1] - 2024-04-26

### 📚 Documentação

- Adicionado CHANGELOG.md seguindo o formato Keep a Changelog
- Documentação detalhada de todas as alterações desde o início do projeto
- Organização clara com seções e emojis para melhor legibilidade
- Links para releases no GitHub

## [1.0.0] - 2024-04-26

### ✨ Adicionado

- Interface gráfica moderna usando Streamlit
- Tema claro/escuro automático baseado nas preferências do sistema
- Display com fonte monoespaçada para melhor legibilidade
- Suporte completo a teclado com atalhos
- Operações matemáticas básicas (adição, subtração, multiplicação, divisão)
- Funcionalidades especiais:
  - Inversão de sinal (±)
  - Cálculo de porcentagem (%)
  - Ponto decimal
  - Botão de limpar (AC)
  - Botão de apagar (⌫)

### 🎨 Visual & UI

- Implementação de ícones Unicode modernos para operadores
- Esquema de cores diferenciado para botões:
  - Azul (#2196F3) para botões de operação
  - Laranja (#FF9800) para botões de controle
  - Verde (#4CAF50) para efeito hover
- Animações suaves nos botões
- Sombras e efeitos visuais modernos
- Interface totalmente responsiva

### 🔧 Melhorias Técnicas

- Tratamento robusto de erros:
  - Prevenção de divisão por zero
  - Validação de entrada de números
  - Mensagens de erro claras
- Formatação consistente de números:
  - Mantém inteiros sem casas decimais
  - Preserva casas decimais quando necessário
- Implementação de estado da calculadora usando Streamlit session_state
- Suporte a teclado via JavaScript
- CSS personalizado para melhor experiência do usuário

### 📚 Documentação

- README completo com:
  - Badges informativos
  - Instruções de instalação
  - Guia de uso
  - Lista de características
  - Seção de contribuição
- Link para demonstração online
- Documentação de atalhos de teclado
- Informações sobre licença e contribuições

### 🌐 Deployment

- Aplicação deployada no Streamlit Cloud
- Disponível publicamente em: https://pycalculator.streamlit.app/

[1.0.0]: https://github.com/vs0uz4/PyCalculatorIA/releases/tag/v1.0.0 