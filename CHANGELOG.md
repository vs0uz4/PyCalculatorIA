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

## [1.1.0] - 2024-06-07

### ✨ Adicionado

- Exibição da expressão completa (ex: 1+5) no display enquanto o usuário digita, mostrando apenas o resultado após pressionar '='.
- Uso de símbolos matemáticos tradicionais (× para multiplicação e ÷ para divisão) no display, mantendo os operadores originais para o cálculo.

### 🎨 Visual & UX

- Melhoria na experiência visual do display, tornando a visualização da operação mais intuitiva e próxima das calculadoras físicas.

### 🐞 Correções

- Ajuste para limpar corretamente a expressão e o resultado ao pressionar 'AC'.

## [1.2.0] - 2024-06-07

### ✨ Melhorias e Novidades
- Refatoração completa do layout dos botões para uso exclusivo de `st.button` e `st.columns`, eliminando grids HTML customizados.
- Responsividade aprimorada e alinhamento perfeito dos botões em todos os tamanhos de tela.
- Display da calculadora com gradiente suave, sombra, borda e texto em negrito para maior destaque e legibilidade.
- Botões AC e = destacados em laranja intermediário (`#FFA726`), com hover mais claro, usando `type="primary"` do Streamlit.
- Botões de operação (+, −, ×, ÷) em azul claro (`#64B5F6`), com hover azul mais intenso, usando `type="secondary"`.
- Remoção de todos os tooltips e resíduos de experimentos antigos (HTML customizado, scripts JS, query params, etc).
- CSS customizado limpo, robusto e fácil de manter, aproveitando os tipos nativos de botão do Streamlit.
- Código organizado: funções utilitárias no topo, layout do display e botões em sequência lógica.

### 🐞 Correções
- Corrigido erro de função indefinida (`update_display`) ao clicar nos botões.
- Corrigido problema de hover verde sobrescrevendo as cores personalizadas dos botões.
- Corrigido desalinhamento e diferenças visuais entre botões causados por tooltips e HTML customizado.

### 🧹 Limpeza e Refatoração
- Remoção de todo o código legado de grid HTML, scripts JS, tooltips e experimentos antigos.
- Garantia de que apenas o layout nativo do Streamlit é utilizado para máxima compatibilidade e manutenção.

[1.0.0]: https://github.com/vs0uz4/PyCalculatorIA/releases/tag/v1.0.0 