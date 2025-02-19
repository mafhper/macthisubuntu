# Instalador Interativo para o WhiteSur GTK Theme

Este repositório contém um script interativo em shell que facilita a configuração e instalação do tema [WhiteSur GTK Theme](https://github.com/vinceliuice/WhiteSur-gtk-theme) utilizando os scripts originais `install.sh` e `tweaks.sh`.

## Descrição

O script guia o usuário através de uma interface interativa baseada no utilitário **dialog**, permitindo selecionar diversas opções de customização, como:
- Diretório de instalação e nome do tema;
- Opacidade e variantes de cor;
- Configurações específicas para controle de janelas e acentuação do tema;
- Ajustes adicionais para o tema via `tweaks.sh`, incluindo configurações para GDM e Firefox.

Após a configuração inicial e execução do `install.sh`, o script continua com a configuração e execução do `tweaks.sh`, proporcionando uma experiência completa de instalação e personalização do tema.

## Requisitos

- **Bash**: Shell compatível com Bash.
- **Dialog**: Ferramenta para exibição de interfaces interativas em modo texto.  
  Em distribuições baseadas no Debian, instale com:
  ```bash
  sudo apt-get install dialog
