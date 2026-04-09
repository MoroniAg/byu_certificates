"""A small GUI that accepts an age and displays recommended heart rates.

This file builds a visual interface using `IntEntry` from
`number_entry.py`. It computes the slowest and fastest beneficial
heart rates and displays them in the window.
"""
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def calculate(event, ent_age, lbl_slow, lbl_fast):
	"""Compute and display the slowest and fastest beneficial heart rates.

	Parameters
		event: the tkinter event (unused except for the bind)
		ent_age: the IntEntry widget for age
		lbl_slow: label to display the slow rate
		lbl_fast: label to display the fast rate
	"""
	try:
		age = ent_age.get()
		max_rate = 220 - age
		slow = max_rate * 0.65
		fast = max_rate * 0.85
		lbl_slow.config(text=f"{slow:.0f}")
		lbl_fast.config(text=f"{fast:.0f}")
	except ValueError:
		lbl_slow.config(text="")
		lbl_fast.config(text="")


def clear(ent_age, lbl_slow, lbl_fast, btn_clear):
	"""Clear inputs/outputs and reset focus.

	Parameters
		ent_age: the IntEntry widget for age
		lbl_slow: label showing slow rate
		lbl_fast: label showing fast rate
		btn_clear: the Clear Button widget (so we can focus it)
	"""
	btn_clear.focus()
	ent_age.clear()
	lbl_slow.config(text="")
	lbl_fast.config(text="")
	ent_age.focus()


def main():
	root = tk.Tk()
	root.title("Heart Rate")

	frm = Frame(root)
	frm.pack(padx=6, pady=6)

	lbl_age = Label(frm, text="Age (12 - 90):")
	ent_age = IntEntry(frm, width=4, lower_bound=12, upper_bound=90)
	lbl_years = Label(frm, text="years")

	lbl_rates = Label(frm, text="Rates:")
	lbl_slow = Label(frm, width=6, anchor="e")
	lbl_fast = Label(frm, width=6, anchor="e")
	lbl_units = Label(frm, text="beats/minute")

	btn_clear = Button(frm, text="Clear")

	lbl_age.grid(row=0, column=0, padx=3, pady=3)
	ent_age.grid(row=0, column=1, padx=3, pady=3)
	lbl_years.grid(row=0, column=2, padx=0, pady=3)

	lbl_rates.grid(row=1, column=0, padx=(30,3), pady=3)
	lbl_slow.grid(row=1, column=1, padx=3, pady=3)
	lbl_fast.grid(row=1, column=2, padx=3, pady=3)
	lbl_units.grid(row=1, column=3, padx=0, pady=3)

	btn_clear.grid(row=2, column=0, padx=3, pady=6, columnspan=4, sticky="w")


	ent_age.bind("<KeyRelease>", lambda e: calculate(e, ent_age, lbl_slow, lbl_fast))
	btn_clear.config(command=lambda: clear(ent_age, lbl_slow, lbl_fast, btn_clear))
	ent_age.focus()

	root.mainloop()


if __name__ == "__main__":
	main()


