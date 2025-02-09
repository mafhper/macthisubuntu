#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def gerar_comando():
    comando = "./install.sh"

    # Opções básicas
    dest = dest_entry.get()
    if dest:
        comando += f" -d {dest}"
    nome = nome_entry.get()
    if nome:
        comando += f" -n {nome}"

    # Opções de Opacidade (repetível)
    opacidades = [opcao for opcao, var in opacidade_vars.items() if var.get()]
    if opacidades:
        for opacidade in opacidades:
            comando += f" -o {opacidade}"

    # Opções de Cor (repetível)
    cores = [cor for cor, var in cor_vars.items() if var.get()]
    if cores:
        for cor in cores:
            comando += f" -c {cor}"

    # Opções Alt (repetível)
    alts = [alt for alt, var in alt_vars.items() if var.get()]
    if alts:
        for alt in alts:
            comando += f" -a {alt}"

    # Opções de Tema (repetível)
    temas = [tema for tema, var in tema_vars.items() if var.get()]
    if temas:
        for tema in temas:
            comando += f" -t {tema}"

    # Opções de Scheme (repetível)
    schemes = [scheme for scheme, var in scheme_vars.items() if var.get()]
    if schemes:
        for scheme in schemes:
            comando += f" -s {scheme}"

    # Opções booleanas
    if monterey_var.get():
        comando += " -m"
    if libadwaita_var.get():
        comando += " -l"
    if fixed_var.get():
        comando += " -f"
    if highdefinition_var.get():
        comando += " -HD"
    if roundedmaxwindow_var.get():
        comando += " --round"
    if blackfont_var.get():
        comando += " --black"
    if darkercolor_var.get():
        comando += " --darker"
    if interactive_var.get():
        comando += " --dialog"
    if silent_var.get():
        comando += " --silent-mode"
    if remover_var.get():
        comando += " -r"

    # Opções Nautilus
    nautilus_opcao = nautilus_combobox.get()
    if nautilus_opcao and nautilus_opcao != "Padrão (BigSur-like)":
        comando += f" -N {nautilus_opcao.lower()}"

    # Opções Gnome Shell (sub-opções dentro de --shell)
    if gnomeshell_var.get():
        comando += " --shell"
        icon_opcao = icon_combobox.get()
        if icon_opcao and icon_opcao != "Padrão":
            comando += f" -i {icon_opcao.lower()}"
        background_opcao = background_entry.get()
        if background_opcao and background_opcao != "Padrão":
            if background_opcao == "blank":
                comando += " -b blank"
            else:
                comando += f" -b {background_opcao}"
        panelopacity_opcao = panelopacity_combobox.get()
        if panelopacity_opcao and panelopacity_opcao != "Padrão (15%)":
            comando += f" -p {panelopacity_opcao.lower()}"
        panelheight_opcao = panelheight_combobox.get()
        if panelheight_opcao and panelheight_opcao != "Padrão (32px)":
            comando += f" -h {panelheight_opcao.lower()}"
        if smallerfont_var.get():
            comando += " -sf"
        if normalappsbutton_var.get():
            comando += " normal"

    comando_output.config(state=tk.NORMAL) # Habilitar temporariamente para edição
    comando_output.delete(0, tk.END)
    comando_output.insert(0, comando)
    comando_output.config(state='readonly', fg='black') # Voltar para readonly e definir cor da fonte
    janela.update_idletasks() # Forçar atualização da interface


def mostrar_ajuda():
    ajuda_texto = """
Usage: ./install.sh [OPTIONS...]

OPTIONS:
  -d, --dest DIR
   Set destination directory. Default is '/home/[USER_NAME]/.themes'
  -n, --name NAME
   Set theme name. Default is 'WhiteSur'
  -o, --opacity [normal|solid]
   Set theme opacity variants. Repeatable. Default is all variants
  -c, --color [light|dark]
   Set theme color variants. Repeatable. Default is all variants
  -a, --alt [normal|alt|all]
   Set window control buttons variant. Repeatable. Default is 'normal'
  -t, --theme [default|blue|purple|pink|red|orange|yellow|green|grey|all]
   Set theme accent color. Repeatable. Default is BigSur-like theme
  -s, --scheme [standard|nord]
   Set theme colorscheme style. Repeatable. Default is 'standard'
  -m, --monterey
   Set to MacOS Monterey style.
  -N, --nautilus [stable|normal|mojave|glassy|right]
   Set Nautilus style. Default is BigSur-like style (stabled sidebar)
  -l, --libadwaita
   Install theme into gtk4.0 config for libadwaita. Default is dark version
  -f, --fixed
   Install fixed accent color version. Default is adaptive version
  -HD, --highdefinition
   Set to High Definition size. Default is laptop size
  --shell, --gnomeshell
   Tweaks for gnome-shell. Options:
     1. -i, -icon [apple|simple|gnome|ubuntu|tux|arch|manjaro|fedora|debian|void|opensuse|popos|mxlinux|zorin|budgie|gentoo]
     Set gnome-shell panel 'Activities' icon. Default is 'standard'
     2. -b, -background [default|blank|IMAGE_PATH]
     Set gnome-shell background image. Default is BigSur-like wallpaper
     3. -p, -panelopacity [default|30|45|60|75]
     Set gnome-shell panel transparency. Default is 15%
     4. -h, -panelheight [default|smaller|bigger]
     Set gnome-shell panel height size. Default is 32px
     5. -sf, -smallerfont
     Set gnome-shell font size to smaller (10pt). Default is 11pt
     6. normal, -normal
     Set gnome-shell show apps button style to normal. Default is BigSur
  --round, --roundedmaxwindow
   Set maximized window to rounded. Default is square
  --black, --blackfont
   Set panel font color to black. Default is white
  --darker, --darkercolor
   Install darker 'WhiteSur' dark themes.
  --dialog, --interactive
   Run this installer interactively, with dialogs.
  --silent-mode
   Meant for developers: ignore any confirm prompt and params become more strict.
  -r, --remove, -u, --uninstall
   Remove all installed WhiteSur themes.
  -h, --help
   Show this help.
    """
    messagebox.showinfo("Ajuda Install.sh", ajuda_texto)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Interface Install.sh WhiteSur")

# Frame para opções básicas
frame_basico = ttk.LabelFrame(janela, text="Opções Básicas")
frame_basico.pack(padx=10, pady=10, fill=tk.X)

tk.Label(frame_basico, text="Destino:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
dest_entry = tk.Entry(frame_basico)
dest_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

tk.Label(frame_basico, text="Nome do Tema:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
nome_entry = tk.Entry(frame_basico)
nome_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

# Frame para opções repetíveis
frame_repetiveis = ttk.LabelFrame(janela, text="Opções Repetíveis")
frame_repetiveis.pack(padx=10, pady=10, fill=tk.X)

# Opções de Opacidade
tk.Label(frame_repetiveis, text="Opacidade:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
opacidade_vars = {
    "normal": tk.BooleanVar(),
    "solid": tk.BooleanVar()
}
opacidade_frame = tk.Frame(frame_repetiveis)
opacidade_frame.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
for i, (opcao, var) in enumerate(opacidade_vars.items()):
    tk.Checkbutton(opacidade_frame, text=opcao, variable=var).pack(side=tk.LEFT)

# Opções de Cor
tk.Label(frame_repetiveis, text="Cor:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
cor_vars = {
    "light": tk.BooleanVar(),
    "dark": tk.BooleanVar()
}
cor_frame = tk.Frame(frame_repetiveis)
cor_frame.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
for i, (cor, var) in enumerate(cor_vars.items()):
    tk.Checkbutton(cor_frame, text=cor, variable=var).pack(side=tk.LEFT)

# Opções Alt
tk.Label(frame_repetiveis, text="Botões Alt:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
alt_vars = {
    "normal": tk.BooleanVar(),
    "alt": tk.BooleanVar(),
    "all": tk.BooleanVar()
}
alt_frame = tk.Frame(frame_repetiveis)
alt_frame.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
for i, (alt, var) in enumerate(alt_vars.items()):
    tk.Checkbutton(alt_frame, text=alt, variable=var).pack(side=tk.LEFT)

# Opções de Tema
tk.Label(frame_repetiveis, text="Tema Accent Color:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
tema_vars = {
    "default": tk.BooleanVar(), "blue": tk.BooleanVar(), "purple": tk.BooleanVar(),
    "pink": tk.BooleanVar(), "red": tk.BooleanVar(), "orange": tk.BooleanVar(),
    "yellow": tk.BooleanVar(), "green": tk.BooleanVar(), "grey": tk.BooleanVar(), "all": tk.BooleanVar()
}
tema_frame = tk.Frame(frame_repetiveis)
tema_frame.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
for i, (tema, var) in enumerate(tema_vars.items()):
    tk.Checkbutton(tema_frame, text=tema, variable=var).pack(side=tk.LEFT)

# Opções de Scheme
tk.Label(frame_repetiveis, text="Colorscheme Style:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
scheme_vars = {
    "standard": tk.BooleanVar(), "nord": tk.BooleanVar()
}
scheme_frame = tk.Frame(frame_repetiveis)
scheme_frame.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)
for i, (scheme, var) in enumerate(scheme_vars.items()):
    tk.Checkbutton(scheme_frame, text=scheme, variable=var).pack(side=tk.LEFT)


# Frame para opções booleanas
frame_booleanas = ttk.LabelFrame(janela, text="Opções Booleanas")
frame_booleanas.pack(padx=10, pady=10, fill=tk.X)

monterey_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Monterey Style", variable=monterey_var).pack(anchor=tk.W)
libadwaita_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Libadwaita", variable=libadwaita_var).pack(anchor=tk.W)
fixed_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Fixed Accent Color", variable=fixed_var).pack(anchor=tk.W)
highdefinition_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="High Definition", variable=highdefinition_var).pack(anchor=tk.W)
roundedmaxwindow_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Rounded Max Window", variable=roundedmaxwindow_var).pack(anchor=tk.W)
blackfont_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Black Font Panel", variable=blackfont_var).pack(anchor=tk.W)
darkercolor_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Darker Color Theme", variable=darkercolor_var).pack(anchor=tk.W)
interactive_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Interactive Mode", variable=interactive_var).pack(anchor=tk.W)
silent_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Silent Mode", variable=silent_var).pack(anchor=tk.W)
remover_var = tk.BooleanVar()
tk.Checkbutton(frame_booleanas, text="Remover/Uninstall", variable=remover_var).pack(anchor=tk.W)


# Frame para opções Nautilus
frame_nautilus = ttk.LabelFrame(janela, text="Opções Nautilus")
frame_nautilus.pack(padx=10, pady=10, fill=tk.X)

tk.Label(frame_nautilus, text="Estilo Nautilus:").pack(anchor=tk.W)
nautilus_opcoes = ["Padrão (BigSur-like)", "Stable", "Normal", "Mojave", "Glassy", "Right"]
nautilus_combobox = ttk.Combobox(frame_nautilus, values=nautilus_opcoes)
nautilus_combobox.set(nautilus_opcoes[0]) # Define o padrão
nautilus_combobox.pack(fill=tk.X, padx=5, pady=5)


# Frame para opções Gnome Shell
frame_gnomeshell = ttk.LabelFrame(janela, text="Opções Gnome Shell (--shell)")
frame_gnomeshell.pack(padx=10, pady=10, fill=tk.X)
gnomeshell_var = tk.BooleanVar()
tk.Checkbutton(frame_gnomeshell, text="Ativar Tweaks Gnome Shell", variable=gnomeshell_var, command=lambda: atualizar_gnomeshell_frame()).pack(anchor=tk.W)

gnomeshell_conteudo_frame = tk.Frame(frame_gnomeshell) # Frame interno para conteúdo do Gnome Shell
gnomeshell_conteudo_frame.pack(fill=tk.X, padx=10, pady=5)

def atualizar_gnomeshell_frame():
    if gnomeshell_var.get():
        gnomeshell_conteudo_frame.pack(fill=tk.X, padx=10, pady=5) # Mostra o frame de conteúdo
    else:
        gnomeshell_conteudo_frame.pack_forget() # Esconde o frame de conteúdo

# Opções Gnome Shell dentro do frame de conteúdo
tk.Label(gnomeshell_conteudo_frame, text="Ícone Activities:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
icon_opcoes = ["Padrão", "Apple", "Simple", "Gnome", "Ubuntu", "Tux", "Arch", "Manjaro", "Fedora", "Debian", "Void", "Opensuse", "Popos", "Mxlinux", "Zorin", "Budgie", "Gentoo"]
icon_combobox = ttk.Combobox(gnomeshell_conteudo_frame, values=icon_opcoes)
icon_combobox.set(icon_opcoes[0])
icon_combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

tk.Label(gnomeshell_conteudo_frame, text="Imagem de Fundo:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
background_entry = tk.Entry(gnomeshell_conteudo_frame)
background_entry.insert(0, "Padrão") # Valor padrão "Padrão"
background_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

tk.Label(gnomeshell_conteudo_frame, text="Opacidade do Painel:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
panelopacity_opcoes = ["Padrão (15%)", "30", "45", "60", "75"]
panelopacity_combobox = ttk.Combobox(gnomeshell_conteudo_frame, values=panelopacity_opcoes)
panelopacity_combobox.set(panelopacity_opcoes[0])
panelopacity_combobox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

tk.Label(gnomeshell_conteudo_frame, text="Altura do Painel:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
panelheight_opcoes = ["Padrão (32px)", "Smaller", "Bigger"]
panelheight_combobox = ttk.Combobox(gnomeshell_conteudo_frame, values=panelheight_opcoes)
panelheight_combobox.set(panelheight_opcoes[0])
panelheight_combobox.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W+tk.E)

smallerfont_var = tk.BooleanVar()
tk.Checkbutton(gnomeshell_conteudo_frame, text="Fonte Menor Gnome Shell", variable=smallerfont_var).grid(row=4, column=0, columnspan=2, sticky=tk.W)
normalappsbutton_var = tk.BooleanVar()
tk.Checkbutton(gnomeshell_conteudo_frame, text="Botão Apps Normal", variable=normalappsbutton_var).grid(row=5, column=0, columnspan=2, sticky=tk.W)

atualizar_gnomeshell_frame() # Inicialmente esconde o frame de conteúdo Gnome Shell


# Frame para comando gerado e botões
frame_comando = ttk.LabelFrame(janela, text="Comando Gerado")
frame_comando.pack(padx=10, pady=10, fill=tk.X)

comando_output = tk.Entry(frame_comando, state='readonly') # Campo de texto para saída do comando
comando_output.pack(fill=tk.X, padx=5, pady=5)

botao_gerar = tk.Button(janela, text="Gerar Comando", command=gerar_comando)
botao_gerar.pack(pady=5)

botao_ajuda = tk.Button(janela, text="Ajuda", command=mostrar_ajuda)
botao_ajuda.pack(pady=5)


janela.mainloop()
