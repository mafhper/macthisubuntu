#!/bin/bash
# Script interativo para configurar e executar install.sh e, em seguida, tweaks.sh
# Certifique-se de ter o pacote 'dialog' instalado no sistema.

# --- Funções auxiliares ---
input_box() {
    dialog --title "$1" --inputbox "$2" 8 50 "$3" 3>&1 1>&2 2>&3
}

menu_box() {
    dialog --title "$1" --menu "$2" 15 50 "$3" "${@:4}" 3>&1 1>&2 2>&3
}

cleanup() {
    clear
}
trap cleanup EXIT

# =============================
# Configuração e execução do install.sh
# =============================

# Diretório de destino
dest_dir=$(input_box "Diretório de destino" "Informe o diretório onde o tema será instalado:" "/home/ubuntu/.themes")

# Nome do tema
theme_name=$(input_box "Nome do Tema" "Informe o nome do tema:" "WhiteSur")

# Opacidade do tema
opacity=$(menu_box "Opacidade" "Selecione a opacidade:" 2 \
  "normal" "Opacidade normal" \
  "solid" "Opacidade sólida")
  
# Variante de cor
color=$(menu_box "Cor" "Selecione a variante de cor:" 2 \
  "light" "Tema claro" \
  "dark" "Tema escuro")
  
# Variante dos botões de janela
alt=$(menu_box "Controle de Janela" "Selecione a variante de botões:" 3 \
  "normal" "Padrão" \
  "alt" "Alternativo" \
  "all" "Todos")

# Tema de acento
theme_accent=$(menu_box "Acento do Tema" "Selecione a cor de acento:" 10 \
  "default" "Padrão (BigSur-like)" \
  "blue" "Azul" \
  "purple" "Roxo" \
  "pink" "Rosa" \
  "red" "Vermelho" \
  "orange" "Laranja" \
  "yellow" "Amarelo" \
  "green" "Verde" \
  "grey" "Cinza" \
  "all" "Todos")

# Esquema de cores
scheme=$(menu_box "Esquema de Cores" "Selecione o esquema:" 2 \
  "standard" "Padrão" \
  "nord" "Nord")

# Ativar estilo MacOS Monterey?
dialog --title "MacOS Monterey" --yesno "Deseja ativar o estilo MacOS Monterey?" 7 50
if [ $? -eq 0 ]; then
    monterey_flag="-m"
else
    monterey_flag=""
fi

# Monta a linha de comando para o install.sh
cmd_install="./install.sh -d \"$dest_dir\" -n \"$theme_name\" -o $opacity -c $color -a $alt -t $theme_accent -s $scheme $monterey_flag"

# Mostra a linha de comando para confirmação
dialog --msgbox "Linha de comando gerada para install.sh:\n$cmd_install" 10 70

# Pergunta se deseja executar o install.sh
dialog --yesno "Deseja executar o comando install.sh?" 7 50
if [ $? -eq 0 ]; then
    eval $cmd_install
else
    dialog --msgbox "Instalação cancelada." 5 40
fi

# =============================
# Configuração e execução do tweaks.sh
# =============================

# Opacidade para tweaks
opacity_t=$(menu_box "Opacidade (tweaks)" "Selecione a opacidade:" 2 \
  "normal" "Normal" \
  "solid" "Sólida")

# Variante de cor para tweaks
color_t=$(menu_box "Cor (tweaks)" "Selecione a variante de cor:" 2 \
  "light" "Claro" \
  "dark" "Escuro")

# Tema de acento para tweaks
theme_accent_t=$(menu_box "Acento (tweaks)" "Selecione a cor de acento:" 9 \
  "default" "Padrão (BigSur-like)" \
  "blue" "Azul" \
  "purple" "Roxo" \
  "pink" "Rosa" \
  "red" "Vermelho" \
  "orange" "Laranja" \
  "yellow" "Amarelo" \
  "green" "Verde" \
  "grey" "Cinza")

# Esquema de cores para tweaks
scheme_t=$(menu_box "Esquema (tweaks)" "Selecione o esquema:" 2 \
  "standard" "Padrão" \
  "nord" "Nord")

# Configurações opcionais para GDM
dialog --title "GDM" --yesno "Deseja configurar opções do GDM?" 7 50
if [ $? -eq 0 ]; then
    gdm_icon=$(menu_box "Ícone GDM" "Selecione o ícone para o GDM:" 3 \
      "apple" "Apple" \
      "gnome" "Gnome" \
      "ubuntu" "Ubuntu")
    gdm_options="-g -i $gdm_icon"
else
    gdm_options=""
fi

# Monta a linha de comando para o tweaks.sh
cmd_tweaks="./tweaks.sh -o $opacity_t -c $color_t -t $theme_accent_t -s $scheme_t $gdm_options"

# Mostra a linha de comando para confirmação
dialog --msgbox "Linha de comando gerada para tweaks.sh:\n$cmd_tweaks" 10 70

# Pergunta se deseja executar o tweaks.sh
dialog --yesno "Deseja executar o comando tweaks.sh?" 7 50
if [ $? -eq 0 ]; then
    eval $cmd_tweaks
else
    dialog --msgbox "Tweaks cancelados." 5 40
fi

exit 0
