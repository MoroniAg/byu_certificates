"""
Program to compute the molar mass of a chemical compound from its chemical formula and the number of moles in a given mass of the compound.

Author: Moroni Aguilera
Changes:
- 2026-03-26: add function make_periodic_table() to create a dictionary of chemical symbols, names, and atomic masses.
- 2026-03-27: add function compute_molar_mass() to compute the molar mass of a compound from a list of chemical symbols and quantities and a periodic table dictionary.
- 2026-03-27: add main program logic to prompt user for input, compute molar mass, and display results.
- 2026-03-28: add additional functionality to print in a file the molar mass and number of moles for a given compound and mass, and allow the user to calculate multiple compounds in a single session.

"""

from formula import parse_formula 

def make_periodic_table():
    periodic_table_dict = {
  "Ac": ["Actinium", 227],
  "Ag": ["Silver", 107.8682],
  "Al": ["Aluminum", 26.9815386],
  "Ar": ["Argon", 39.948],
  "As": ["Arsenic", 74.9216],
  "At": ["Astatine", 210],
  "Au": ["Gold", 196.966569],
  "B": ["Boron", 10.811],
  "Ba": ["Barium", 137.327],
  "Be": ["Beryllium", 9.012182],
  "Bi": ["Bismuth", 208.9804],
  "Br": ["Bromine", 79.904],
  "C": ["Carbon", 12.0107],
  "Ca": ["Calcium", 40.078],
  "Cd": ["Cadmium", 112.411],
  "Ce": ["Cerium", 140.116],
  "Cl": ["Chlorine", 35.453],
  "Co": ["Cobalt", 58.933195],
  "Cr": ["Chromium", 51.9961],
  "Cs": ["Cesium", 132.9054519],
  "Cu": ["Copper", 63.546],
  "Dy": ["Dysprosium", 162.5],
  "Er": ["Erbium", 167.259],
  "Eu": ["Europium", 151.964],
  "F": ["Fluorine", 18.9984032],
  "Fe": ["Iron", 55.845],
  "Fr": ["Francium", 223],
  "Ga": ["Gallium", 69.723],
  "Gd": ["Gadolinium", 157.25],
  "Ge": ["Germanium", 72.64],
  "H": ["Hydrogen", 1.00794],
  "He": ["Helium", 4.002602],
  "Hf": ["Hafnium", 178.49],
  "Hg": ["Mercury", 200.59],
  "Ho": ["Holmium", 164.93032],
  "I": ["Iodine", 126.90447],
  "In": ["Indium", 114.818],
  "Ir": ["Iridium", 192.217],
  "K": ["Potassium", 39.0983],
  "Kr": ["Krypton", 83.798],
  "La": ["Lanthanum", 138.90547],
  "Li": ["Lithium", 6.941],
  "Lu": ["Lutetium", 174.9668],
  "Mg": ["Magnesium", 24.305],
  "Mn": ["Manganese", 54.938045],
  "Mo": ["Molybdenum", 95.96],
  "N": ["Nitrogen", 14.0067],
  "Na": ["Sodium", 22.98976928],
  "Nb": ["Niobium", 92.90638],
  "Nd": ["Neodymium", 144.242],
  "Ne": ["Neon", 20.1797],
  "Ni": ["Nickel", 58.6934],
  "Np": ["Neptunium", 237],
  "O": ["Oxygen", 15.9994],
  "Os": ["Osmium", 190.23],
  "P": ["Phosphorus", 30.973762],
  "Pa": ["Protactinium", 231.03588],
  "Pb": ["Lead", 207.2],
  "Pd": ["Palladium", 106.42],
  "Pm": ["Promethium", 145],
  "Po": ["Polonium", 209],
  "Pr": ["Praseodymium", 140.90765],
  "Pt": ["Platinum", 195.084],
  "Pu": ["Plutonium", 244],
  "Ra": ["Radium", 226],
  "Rb": ["Rubidium", 85.4678],
  "Re": ["Rhenium", 186.207],
  "Rh": ["Rhodium", 102.9055],
  "Rn": ["Radon", 222],
  "Ru": ["Ruthenium", 101.07],
  "S": ["Sulfur", 32.065],
  "Sb": ["Antimony", 121.76],
  "Sc": ["Scandium", 44.955912],
  "Se": ["Selenium", 78.96],
  "Si": ["Silicon", 28.0855],
  "Sm": ["Samarium", 150.36],
  "Sn": ["Tin", 118.71],
  "Sr": ["Strontium", 87.62],
  "Ta": ["Tantalum", 180.94788],
  "Tb": ["Terbium", 158.92535],
  "Tc": ["Technetium", 98],
  "Te": ["Tellurium", 127.6],
  "Th": ["Thorium", 232.03806],
  "Ti": ["Titanium", 47.867],
  "Tl": ["Thallium", 204.3833],
  "Tm": ["Thulium", 168.93421],
  "U": ["Uranium", 238.02891],
  "V": ["Vanadium", 50.9415],
  "W": ["Tungsten", 183.84],
  "Xe": ["Xenon", 131.293],
  "Y": ["Yttrium", 88.90585],
  "Yb": ["Ytterbium", 173.054],
  "Zn": ["Zinc", 65.38],
  "Zr": ["Zirconium", 91.224],
  }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0
    for symbol, quantity in symbol_quantity_list:
        if symbol in periodic_table_dict:
            element_mass = periodic_table_dict[symbol][1]
            total_mass += element_mass * quantity
    return total_mass


def save_historical_data(formula, molar_mass, number_moles):
    with open("historical_data.txt", "a") as file:
        file.write(f"{formula}: Molar Mass = {molar_mass:.5f} g/mol, Number of Moles = {number_moles:.5f} moles\n")

def main():
  print("|-------------------------------------------------------------------------|\n| This program calculates the molar mass of a chemical compound.          | \n| It also calculates the number of moles in a given mass of the compound. | \n| You can enter any chemical formula,                                     | \n| and the program will compute the results for you.                       | \n|\tLet's get started!                                                | \n|-------------------------------------------------------------------------|")
  while True:
    formula = input("Enter the chemical formula of the compound: ")
    size_grams = float(input("Enter the size of the sample in grams: "))
    periodic_table = make_periodic_table()
    parse_form = parse_formula(formula, periodic_table)
    molar_mass = compute_molar_mass(parse_form, periodic_table)
    print(f"The molar mass of {formula} is {molar_mass:.5f} grams/mole.")
    number_moles = size_grams / molar_mass
    print(f"The number of moles in {size_grams:.5f} grams of {formula} is {number_moles:.5f} moles.")
    save_historical_data(formula, molar_mass, number_moles)
    cont = input("\nDo you want to calculate another compound? (yes/no): ")
    if cont.lower() != "yes":
        break


if __name__ == "__main__":
  main()    