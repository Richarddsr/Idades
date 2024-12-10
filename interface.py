import tkinter as tk

def exibir_texto():
    texto = entrada.get()  # Obtendo o texto inserido pelo usuário
    label_resultado.config(text=f"Você tem : {texto} anos")  # Atualizando o texto do Label

def limpar_texto():
    entrada.delete(0, tk.END)  # Apaga o conteúdo do Entry
    label_resultado.config(text="")  # Limpa o texto do Label

root = tk.Tk()
root.title("Revelador de idades 🖥️")
root.geometry("600x400")
root.configure(bg="lightyellow")

label = tk.Label(root, text="Digite sua idade: ", font=("Cardinal", 14), bg="lightyellow", fg="orange")
label.pack(pady=20)  # Exibindo o rótulo com espaçamento vertical

entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)  # Exibindo a entrada com espaçamento vertical

botao_exibir = tk.Button(root, text="Exibir Idade", font=("Cardinal", 12), bg="lightgreen", fg="white", command=exibir_texto)
botao_exibir.pack(pady=10)

frame_botoes = tk.Frame(root, bg="lightyellow")
frame_botoes.pack(pady=10)

botao_enviar = tk.Button(frame_botoes, text="Enviar", font=("Cardinal", 12), bg="white", fg="blue", command=exibir_texto)
botao_enviar.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar", font=("Cardinal", 12), bg="white", fg="red", command=limpar_texto)
botao_limpar.pack(side=tk.LEFT, padx=5)

# Label para exibir o texto inserido
label_resultado = tk.Label(root, text="", font=("Cardinal", 10), bg="lightyellow", fg="orange")
label_resultado.pack(pady=20)

root.mainloop()