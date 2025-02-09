# Interface Gráfica para Install.sh WhiteSur

Este programa é uma interface gráfica simples criada em Python usando Tkinter para facilitar a geração de linhas de comando para o script `install.sh` do tema WhiteSur. Ele permite que você personalize a instalação do tema WhiteSur no seu sistema Linux de forma visual, sem precisar memorizar todas as opções da linha de comando.

## Funcionalidades

A interface gráfica oferece as seguintes opções, correspondendo às opções do script `install.sh`:

**Opções Básicas:**

*   **Destino (-d, --dest DIR):** Define o diretório de destino para a instalação do tema. O padrão é `/home/[USER_NAME]/.themes`.
*   **Nome do Tema (-n, --name NAME):** Define o nome do tema a ser instalado. O padrão é `WhiteSur`.

**Opções Repetíveis:**

*   **Opacidade (-o, --opacity [normal|solid]):** Define as variantes de opacidade do tema. Você pode selecionar múltiplas opções (normal, solid). O padrão é todas as variantes.
*   **Cor (-c, --color [light|dark]):** Define as variantes de cor do tema. Você pode selecionar múltiplas opções (light, dark). O padrão é todas as variantes.
*   **Botões Alt (-a, --alt [normal|alt|all]):** Define as variantes dos botões de controle da janela. Você pode selecionar múltiplas opções (normal, alt, all). O padrão é 'normal'.
*   **Tema Accent Color (-t, --theme [default|blue|purple|pink|red|orange|yellow|green|grey|all]):** Define a cor de destaque do tema. Você pode selecionar múltiplas opções (default, blue, purple, pink, red, orange, yellow, green, grey, all). O padrão é o tema similar ao BigSur.
*   **Colorscheme Style (-s, --scheme [standard|nord]):** Define o esquema de cores do tema. Você pode selecionar múltiplas opções (standard, nord). O padrão é 'standard'.

**Opções Booleanas:**

*   **Monterey Style (-m, --monterey):** Define o estilo para MacOS Monterey.
*   **Libadwaita (-l, --libadwaita):** Instala o tema na configuração gtk4.0 para libadwaita. O padrão é a versão dark.
*   **Fixed Accent Color (-f, --fixed):** Instala a versão com cor de destaque fixa. O padrão é a versão adaptativa.
*   **High Definition (-HD, --highdefinition):** Define o tamanho para High Definition. O padrão é tamanho para laptop.
*   **Rounded Max Window (--round, --roundedmaxwindow):** Define janelas maximizadas como arredondadas. O padrão é quadrado.
*   **Black Font Panel (--black, --blackfont):** Define a cor da fonte do painel para preto. O padrão é branco.
*   **Darker Color Theme (--darker, --darkercolor):** Instala temas dark 'WhiteSur' mais escuros.
*   **Interactive Mode (--dialog, --interactive):** Executa o instalador interativamente, com diálogos.
*   **Silent Mode (--silent-mode):** Destinado a desenvolvedores: ignora prompts de confirmação e parâmetros se tornam mais estritos.
*   **Remover/Uninstall (-r, --remove, -u, --uninstall):** Remove todos os temas WhiteSur instalados.

**Opções Nautilus:**

*   **Estilo Nautilus (-N, --nautilus [stable|normal|mojave|glassy|right]):** Define o estilo do Nautilus. O padrão é o estilo similar ao BigSur (sidebar estável).

**Opções Gnome Shell (--shell, --gnomeshell):**

*   **Ativar Tweaks Gnome Shell (--shell):** Habilita as opções de personalização do Gnome Shell.
    *   **Ícone Activities (-i, -icon [apple|simple|gnome|ubuntu|tux|arch|manjaro|fedora|debian|void|opensuse|popos|mxlinux|zorin|budgie|gentoo]):** Define o ícone do botão 'Activities' no painel do Gnome Shell. O padrão é 'standard'.
    *   **Imagem de Fundo (-b, -background [default|blank|IMAGE_PATH]):** Define a imagem de fundo do Gnome Shell. Você pode usar 'blank' para um fundo branco ou o caminho para um arquivo de imagem. O padrão é o wallpaper similar ao BigSur.
    *   **Opacidade do Painel (-p, -panelopacity [default|30|45|60|75]):** Define a transparência do painel do Gnome Shell. O padrão é 15%.
    *   **Altura do Painel (-h, -panelheight [default|smaller|bigger]):** Define a altura do painel do Gnome Shell. O padrão é 32px.
    *   **Fonte Menor Gnome Shell (-sf, -smallerfont):** Define o tamanho da fonte do Gnome Shell para menor (10pt). O padrão é 11pt.
    *   **Botão Apps Normal (normal, -normal):** Define o estilo do botão 'Mostrar Aplicativos' para normal. O padrão é o estilo BigSur.

## Como Usar

1.  **Pré-requisitos:**
    *   Tenha o Python 3 instalado no seu sistema.
    *   Certifique-se de ter o módulo `tkinter` instalado (geralmente incluído nas instalações padrão do Python, mas pode ser necessário instalar separadamente em algumas distribuições Linux com um comando como `sudo apt-get install python3-tk` ou similar).
    *   Certifique-se de ter o script `install.sh` do tema WhiteSur no mesmo diretório que o script Python.

2.  **Executando o Script:**
    *   Salve o código Python em um arquivo, por exemplo, `interface_install.py`.
    *   Abra um terminal e navegue até o diretório onde você salvou o arquivo.
    *   Torne o script Python executável (opcional, mas recomendado para executar diretamente): `chmod +x interface_install.py`
    *   Execute o script com Python 3: `./interface_install.py` ou `python3 interface_install.py`

3.  **Usando a Interface Gráfica:**
    *   A interface gráfica será aberta.
    *   Preencha as opções desejadas nos campos e caixas de seleção correspondentes.
    *   Clique no botão "Gerar Comando".
    *   O comando `install.sh` completo com as opções selecionadas será gerado e exibido na caixa de texto "Comando Gerado".
    *   Copie o comando gerado.
    *   Cole o comando no terminal e execute-o para instalar o tema WhiteSur com as configurações desejadas.
    *   Você pode clicar no botão "Ajuda" para ver a descrição completa de todas as opções do `install.sh`.

## Requisitos

*   Python 3
*   Tkinter (geralmente parte da instalação padrão do Python)

## Licença

[MIT License](LICENSE) (Você pode adicionar um arquivo `LICENSE` com a licença MIT se desejar)
