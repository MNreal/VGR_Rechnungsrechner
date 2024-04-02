import tkinter as tk

def calculate():
    choice = var.get()
    
    if choice == 1:
        vgr = float(ent_vgr.get())
        s = float(ent_s.get())
        t = float(ent_t.get())
        m = float(ent_m.get())
        result = vgr + s + t + m
        lbl_result.config(text=f"BIP laut Entstehungsrechnung = {result} MRD.")
    elif choice == 2:
        l = float(ent_l.get())
        g = float(ent_g.get())
        v = float(ent_v.get())
        m = float(ent_m2.get())
        result = l + g + v + m
        lbl_result.config(text=f"BIP der Verteilung des Einkommens = {result} MRD.")
    elif choice == 3:
        c = float(ent_c.get())
        i = float(ent_i.get())
        g = float(ent_g2.get())
        x = float(ent_x.get())
        m = float(ent_m3.get())
        result = c + i + g + (x - m)
        lbl_result.config(text=f"BIP Verteilt auf verschiedene Verwendungsbereiche = {result} MRD.")
    else:
        lbl_result.config(text="Vorgang abgebrochen!")

def show_fields():
    choice = var.get()
    if choice == 1:
        ent_vgr.grid(row=0, column=1)
        lbl_vgr.grid(row=0, column=0)
        ent_s.grid(row=1, column=1)
        lbl_s.grid(row=1, column=0)
        ent_t.grid(row=2, column=1)
        lbl_t.grid(row=2, column=0)
        ent_m.grid(row=3, column=1)
        lbl_m.grid(row=3, column=0)
        ent_l.grid_forget()
        lbl_l.grid_forget()
        ent_g.grid_forget()
        lbl_g.grid_forget()
        ent_v.grid_forget()
        lbl_v.grid_forget()
        ent_m2.grid_forget()
        lbl_m2.grid_forget()
        ent_c.grid_forget()
        lbl_c.grid_forget()
        ent_i.grid_forget()
        lbl_i.grid_forget()
        ent_g2.grid_forget()
        lbl_g2.grid_forget()
        ent_x.grid_forget()
        lbl_x.grid_forget()
        ent_m3.grid_forget()
        lbl_m3.grid_forget()
    elif choice == 2:
        ent_l.grid(row=0, column=3)
        lbl_l.grid(row=0, column=2)
        ent_g.grid(row=1, column=3)
        lbl_g.grid(row=1, column=2)
        ent_v.grid(row=2, column=3)
        lbl_v.grid(row=2, column=2)
        ent_m2.grid(row=3, column=3)
        lbl_m2.grid(row=3, column=2)
        ent_vgr.grid_forget()
        lbl_vgr.grid_forget()
        ent_s.grid_forget()
        lbl_s.grid_forget()
        ent_t.grid_forget()
        lbl_t.grid_forget()
        ent_m.grid_forget()
        lbl_m.grid_forget()
        ent_c.grid_forget()
        lbl_c.grid_forget()
        ent_i.grid_forget()
        lbl_i.grid_forget()
        ent_g2.grid_forget()
        lbl_g2.grid_forget()
        ent_x.grid_forget()
        lbl_x.grid_forget()
        ent_m3.grid_forget()
        lbl_m3.grid_forget()
    elif choice == 3:
        ent_c.grid(row=0, column=5)
        lbl_c.grid(row=0, column=4)
        ent_i.grid(row=1, column=5)
        lbl_i.grid(row=1, column=4)
        ent_g2.grid(row=2, column=5)
        lbl_g2.grid(row=2, column=4)
        ent_x.grid(row=3, column=5)
        lbl_x.grid(row=3, column=4)
        ent_m3.grid(row=4, column=5)
        lbl_m3.grid(row=4, column=4)
        ent_vgr.grid_forget()
        lbl_vgr.grid_forget()
        ent_s.grid_forget()
        lbl_s.grid_forget()
        ent_t.grid_forget()
        lbl_t.grid_forget()
        ent_m.grid_forget()
        lbl_m.grid_forget()
        ent_l.grid_forget()
        lbl_l.grid_forget()
        ent_g.grid_forget()
        lbl_g.grid_forget()
        ent_v.grid_forget()
        lbl_v.grid_forget()
        ent_m2.grid_forget()
        lbl_m2.grid_forget()

root = tk.Tk()
root.title("VGR-Rechner")

# Label für die Auswahl
lbl_choice = tk.Label(root, text="Welchen Rechnung möchten Sie benutzen?")
lbl_choice.pack()

# Radiobuttons für die Auswahl
var = tk.IntVar()
var.set(1)
radio_entstehungsrechnung = tk.Radiobutton(root, text="Entstehungsrechnung", variable=var, value=1, command=show_fields)
radio_entstehungsrechnung.pack(anchor=tk.W)
radio_verteilungsrechnung = tk.Radiobutton(root, text="Verteilungsrechnung", variable=var, value=2, command=show_fields)
radio_verteilungsrechnung.pack(anchor=tk.W)
radio_verwendungsrechnung = tk.Radiobutton(root, text="Verwendungsrechnung", variable=var, value=3, command=show_fields)
radio_verwendungsrechnung.pack(anchor=tk.W)

# Eingabefelder und Labels für die verschiedenen Rechnungen
frame = tk.Frame(root)
frame.pack()

ent_vgr = tk.Entry(frame)
lbl_vgr = tk.Label(frame, text="Bruttowertschöpfung zu Faktorenkosten (in MRD.):")

ent_s = tk.Entry(frame)
lbl_s = tk.Label(frame, text="Subventionen abzüglich der Produktionsabgaben (in MRD.):")

ent_t = tk.Entry(frame)
lbl_t = tk.Label(frame, text="Produktions- und Importsteuern abzüglich der Subventionen (in MRD.):")

ent_m = tk.Entry(frame)
lbl_m = tk.Label(frame, text="Wert der Vorleistungen (in MRD.):")

ent_l = tk.Entry(frame)
lbl_l = tk.Label(frame, text="Entgelte der Arbeitnehmer (in MRD.):")

ent_g = tk.Entry(frame)
lbl_g = tk.Label(frame, text="Gewinne der Unternehmen (in MRD.):")

ent_v = tk.Entry(frame)
lbl_v = tk.Label(frame, text="Vermögenseinkommen (in MRD.):")

ent_m2 = tk.Entry(frame)
lbl_m2 = tk.Label(frame, text="Subventionen abzüglich der Produktionsabgaben (in MRD.):")

ent_c = tk.Entry(frame)
lbl_c = tk.Label(frame, text="Konsumausgaben der Haushalte (in MRD.):")

ent_i = tk.Entry(frame)
lbl_i = tk.Label(frame, text="Investitionen der Unternehmen (in MRD.):")

ent_g2 = tk.Entry(frame)
lbl_g2 = tk.Label(frame, text="Staatliche Ausgaben für den Konsum und Investitionen (in MRD.):")

ent_x = tk.Entry(frame)
lbl_x = tk.Label(frame, text="Exporte von Gütern und Dienstleistungen (in MRD.):")

ent_m3 = tk.Entry(frame)
lbl_m3 = tk.Label(frame, text="Importe von Gütern und Dienstleistungen (in MRD.):")

# Button zur Berechnung
btn_calc = tk.Button(root, text="Berechnen", command=calculate)
btn_calc.pack()

# Label für das Ergebnis
lbl_result = tk.Label(root, text="")
lbl_result.pack()

root.mainloop()
