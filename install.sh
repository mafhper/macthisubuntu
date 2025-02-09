#!/usr/bin/env bash

# Script para instalar o tema WhiteSur e ícones (com opções avançadas)

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configurações
THEME_VARIANTS=("dark" "light")
ICON_VARIANTS=("dark" "light")
WALLPAPER_URL="https://raw.githubusercontent.com/vinceliuice/WhiteSur-wallpapers/main/macOS-Big-Sur.jpg"

# Variáveis globais
THEME_VARIANT="dark"
ICON_VARIANT="dark"
INSTALL_EXTENSIONS=false
UNINSTALL_MODE=false

# Configurações de segurança
set -eo pipefail

# --- Funções Auxiliares ---

show_help() {
  echo -e "${BLUE}Uso: $0 [OPÇÕES]${NC}"
  echo "Opções:"
  echo "  -v [dark|light]  Escolher variante do tema (padrão: dark)"
  echo "  -i [dark|light]  Escolher variante dos ícones (padrão: dark)"
  echo "  -e               Instalar extensões GNOME recomendadas"
  echo "  -u               Modo de desinstalação"
  echo "  -h               Mostrar esta ajuda"
  exit 0
}

log() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$HOME/whitesur_install.log"
}

check_dependencies() {
  local dependencies=("git" "gnome-shell" "curl")
  local missing=()
  
  for dep in "${dependencies[@]}"; do
    if ! command -v "$dep" &> /dev/null; then
      missing+=("$dep")
    fi
  done

  if [ ${#missing[@]} -gt 0 ]; then
    echo -e "${RED}Dependências faltando:${NC} ${missing[*]}"
    echo -e "Instale com: sudo apt install ${missing[*]}"
    exit 1
  fi
}

check_gnome() {
  if [[ "$XDG_CURRENT_DESKTOP" =~ GNOME|ubuntu:GNOME ]]; then
    return 0
  else
    echo -e "${RED}Este script requer o ambiente GNOME. Abortando.${NC}"
    exit 1
  fi
}

confirm_action() {
  local message="$1"
  read -r -p "$message (s/N): " choice
  [[ "$choice" =~ ^[sSyY] ]]
}

handle_existing_dir() {
  local dir="$1"
  local dir_type="$2"
  
  if [ -d "$dir" ]; then
    echo -e "${YELLOW}Diretório $dir_type já existe:${NC} $dir"
    if confirm_action "Deseja atualizar o repositório?"; then
      log "Atualizando repositório em $dir"
      git -C "$dir" pull --rebase
      return 0
    elif confirm_action "Deseja remover e reinstalar?"; then
      rm -rf "$dir"
      return 0
    else
      return 1
    fi
  fi
  return 0
}

clone_repo() {
  local repo_url="$1"
  local dest_dir="$2"
  local dir_type="$3"

  echo -e "${BLUE}Clonando $dir_type...${NC}"
  if git clone --depth 1 "$repo_url" "$dest_dir"; then
    log "$dir_type clonado com sucesso"
    return 0
  else
    log "Erro ao clonar $dir_type"
    return 1
  fi
}

install_components() {
  local component="$1"
  local variant="$2"
  local install_script
  
  case $component in
    "theme")
      install_script="$HOME/.themes/WhiteSur-gtk-theme/install.sh"
      ;;
    "icons")
      install_script="$HOME/.icons/WhiteSur-icon-theme/install.sh"
      ;;
    *)
      return 1
  esac

  if [ ! -f "$install_script" ]; then
    log "Script de instalação não encontrado: $install_script"
    return 1
  fi

  chmod +x "$install_script"
  log "Instalando $component ($variant)"
  
  local options=()
  [[ "$component" == "theme" ]] && options+=("--color" "$variant")
  [[ "$component" == "icons" ]] && options+=("--color" "$variant" "--theme" "default")
  
  if "$install_script" "${options[@]}"; then
    log "$component instalado com sucesso"
    return 0
  else
    log "Erro na instalação do $component"
    return 1
  fi
}

apply_settings() {
  echo -e "${BLUE}Aplicando configurações...${NC}"
  gsettings set org.gnome.desktop.interface gtk-theme "WhiteSur-${THEME_VARIANT}"
  gsettings set org.gnome.desktop.interface icon-theme "WhiteSur-${ICON_VARIANT}"
  gsettings set org.gnome.desktop.wm.preferences theme "WhiteSur-${THEME_VARIANT}"
}

install_extensions() {
  local extensions=(
    "dash-to-dock@micxgx.gmail.com"
    "user-theme@gnome-shell-extensions.gcampax.github.com"
  )

  echo -e "${BLUE}Instalando extensões GNOME...${NC}"
  for ext in "${extensions[@]}"; do
    gnome-extensions install "$ext" || true
  done
  gnome-shell-extension-tool -e "user-theme"
  gnome-shell-extension-tool -e "dash-to-dock"
}

download_wallpaper() {
  local wallpaper_dir="$HOME/Imagens/Wallpapers"
  mkdir -p "$wallpaper_dir"
  
  echo -e "${BLUE}Baixando wallpaper do macOS...${NC}"
  if curl -sLo "$wallpaper_dir/macOS-WhiteSur.jpg" "$WALLPAPER_URL"; then
    gsettings set org.gnome.desktop.background picture-uri "file://$wallpaper_dir/macOS-WhiteSur.jpg"
    log "Wallpaper configurado com sucesso"
  else
    log "Erro ao baixar wallpaper"
  fi
}

uninstall() {
  echo -e "${RED}Iniciando desinstalação...${NC}"
  rm -rfv "$HOME/.themes/WhiteSur"* "$HOME/.icons/WhiteSur"*
  gsettings reset org.gnome.desktop.interface gtk-theme
  gsettings reset org.gnome.desktop.interface icon-theme
  gsettings reset org.gnome.desktop.wm.preferences theme
  echo -e "${GREEN}Tema removido com sucesso!${NC}"
  exit 0
}

# --- Processamento de Argumentos ---
while getopts ":v:i:euh" opt; do
  case $opt in
    v) [[ " ${THEME_VARIANTS[*]} " =~ " ${OPTARG} " ]] && THEME_VARIANT="$OPTARG" || {
         echo -e "${RED}Variante de tema inválida: ${OPTARG}${NC}"; exit 1
       } ;;
    i) [[ " ${ICON_VARIANTS[*]} " =~ " ${OPTARG} " ]] && ICON_VARIANT="$OPTARG" || {
         echo -e "${RED}Variante de ícone inválida: ${OPTARG}${NC}"; exit 1
       } ;;
    e) INSTALL_EXTENSIONS=true ;;
    u) UNINSTALL_MODE=true ;;
    h) show_help ;;
    \?) echo -e "${RED}Opção inválida: -$OPTARG${NC}"; exit 1 ;;
  esac
done

# --- Execução Principal ---

# Modo desinstalação
$UNINSTALL_MODE && uninstall

# Verificações iniciais
check_gnome
check_dependencies

# Diretórios necessários
mkdir -p "$HOME/.themes" "$HOME/.icons"

# Instalação do Tema GTK
if handle_existing_dir "$HOME/.themes/WhiteSur-gtk-theme" "tema"; then
  clone_repo "https://github.com/vinceliuice/WhiteSur-gtk-theme.git" \
    "$HOME/.themes/WhiteSur-gtk-theme" "tema" && \
  install_components "theme" "$THEME_VARIANT"
fi

# Instalação dos Ícones
if handle_existing_dir "$HOME/.icons/WhiteSur-icon-theme" "ícones"; then
  clone_repo "https://github.com/vinceliuice/WhiteSur-icon-theme.git" \
    "$HOME/.icons/WhiteSur-icon-theme" "ícones" && \
  install_components "icons" "$ICON_VARIANT"
fi

# Aplicar configurações
apply_settings

# Extensões opcionais
$INSTALL_EXTENSIONS && install_extensions

# Wallpaper
download_wallpaper

# Resumo final
echo -e "${GREEN}\nInstalação concluída com sucesso!${NC}"
echo -e "Variantes aplicadas:"
echo -e "  Tema: ${THEME_VARIANT}"
echo -e "  Ícones: ${ICON_VARIANT}"
echo -e "\nReinicie sua sessão para aplicar completamente as mudanças."
