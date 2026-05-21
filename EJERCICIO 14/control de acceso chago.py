from tkinter import *
from tkinter import messagebox
from datetime import datetime


registros=[]


def guardar(reg):

    with open(
        "historial_chagoaccess.txt",
        "a",
        encoding="utf8"
    ) as f:

        f.write(
f"""
Nombre: {reg["nombre"]}
Matricula: {reg["matricula"]}
Carrera: {reg["carrera"]}
Hora: {reg["hora"]}
Estado: {reg["estado"]}

"""
)


def registrar():

    nombre=e_nombre.get().strip()

    matricula=e_matricula.get().strip()

    carrera=e_carrera.get().strip()

    if not nombre or not matricula or not carrera:

        messagebox.showwarning(
            "Error",
            "Completa todos los campos"
        )

        return


    hora=datetime.now().strftime("%H:%M")


    estado="AUTORIZADO"


    if (
        not credencial_var.get()
        or not bata_var.get()
    ):

        estado="DENEGADO"


    dato={

        "nombre":nombre,
        "matricula":matricula,
        "carrera":carrera,
        "hora":hora,
        "estado":estado

    }

    registros.append(dato)

    guardar(dato)


    lista.insert(
        END,
        f"{nombre}  →  {estado}"
    )

    actualizar()

    limpiar()

    messagebox.showinfo(
        "CHAGOACCESS",
        f"Acceso {estado}"
    )



def actualizar():

    total=len(registros)

    buenos=0

    for r in registros:

        if r["estado"]=="AUTORIZADO":
            buenos+=1


    stats.config(

text=f"""
Total: {total}

Autorizados: {buenos}

Denegados: {total-buenos}
"""

)



def limpiar():

    e_nombre.delete(0,END)

    e_matricula.delete(0,END)

    e_carrera.delete(0,END)

    credencial_var.set(True)

    bata_var.set(True)




root=Tk()

root.title(
"🕷 CHAGOACCESS — SPIDER EDITION"
)

root.geometry(
"1000x650"
)

root.config(
bg="#0b132b"
)



titulo=Label(

root,

text="🕷 CHAGOACCESS",

font=(
"Impact",
32
),

bg="#0b132b",

fg="#ff3333"

)

titulo.pack(
pady=15
)



panel=Frame(

root,

bg="#16324f",

padx=20,

pady=20

)

panel.pack()



Label(

panel,

text="Nombre",

bg="#16324f",

fg="white"

).grid(
row=0,
column=0
)

e_nombre=Entry(
panel,
width=30
)

e_nombre.grid(
row=0,
column=1
)



Label(

panel,

text="Matricula",

bg="#16324f",

fg="white"

).grid(
row=1,
column=0
)

e_matricula=Entry(
panel,
width=30
)

e_matricula.grid(
row=1,
column=1
)



Label(

panel,

text="Carrera",

bg="#16324f",

fg="white"

).grid(
row=2,
column=0
)

e_carrera=Entry(
panel,
width=30
)

e_carrera.grid(
row=2,
column=1
)



credencial_var=BooleanVar()

credencial_var.set(True)

bata_var=BooleanVar()

bata_var.set(True)



Checkbutton(

panel,

text="Trae Credencial",

variable=credencial_var,

bg="#16324f",

fg="white",

selectcolor="#16324f"

).grid(
row=3,
column=1,
sticky="w"
)



Checkbutton(

panel,

text="Trae Bata",

variable=bata_var,

bg="#16324f",

fg="white",

selectcolor="#16324f"

).grid(
row=4,
column=1,
sticky="w"
)



def ver_historial():

    try:

        with open(
            "historial_chagoaccess.txt",
            "r",
            encoding="utf8"
        ) as f:

            contenido=f.read()

        ventana=Toplevel()

        ventana.title(
            "Historial"
        )

        ventana.geometry(
            "700x500"
        )

        texto=Text(
            ventana
        )

        texto.pack(
            fill="both",
            expand=True
        )

        texto.insert(
            END,
            contenido
        )

    except:

        messagebox.showinfo(
            "Historial",
            "No hay registros"
        )

def reiniciar_historial():

    confirmar=messagebox.askyesno(

        "Reiniciar",

        "¿Seguro que quieres borrar TODO el historial?"

    )

    if confirmar:

        global registros

        registros=[]

        lista.delete(
            0,
            END
        )

        stats.config(
            text="Total: 0"
        )

        with open(
            "historial_chagoaccess.txt",
            "w",
            encoding="utf8"
        ) as f:

            f.write("")

        messagebox.showinfo(

            "Listo",

            "Historial reiniciado"

        )
Button(

root,

text="🕸 REGISTRAR",

font=(
"Arial",
14
),

width=22,

bg="#d62828",

fg="white",

command=registrar

).pack(
    pady=15
)


Button(

root,

text="📋 VER HISTORIAL",

font=(
"Arial",
12
),

bg="#00509d",

fg="white",

width=22,

command=ver_historial

).pack(
    pady=5
)

Button(

root,

text="🗑 REINICIAR HISTORIAL",

font=("Arial",12),

bg="#8b0000",

fg="white",

width=22,

command=reiniciar_historial

).pack(
pady=5
)

lista=Listbox(

root,

width=80,

height=12,

bg="#1b263b",

fg="white"

)

lista.pack()



stats=Label(

root,

text="Total: 0",

bg="#0b132b",

fg="#58a6ff",

font=(
"Arial",
14
)

)

stats.pack(
pady=20
)



Label(

root,

text="Friendly Neighborhood Access System",

bg="#0b132b",

fg="gray"

).pack()



root.mainloop()