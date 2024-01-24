# %% [markdown]
# 
# # Zadání znovupoužitelnost Reusability
#
# Pro to, abychom dnes spočítali sinus nějakého úhlu nemusíme příliš přemýšlet jak je zařízeno, 
# že nám kalkulačka vrací správný výsledek. V programátorské terminologii prostě zavoláme sin(x)

# načítání dat už znovu programovat nemusíme, máme připravenou funkci v minulém cvičení
# v pythonu můžeme importovat jiné soubory s pythone zdrojovým kódem pomocí klíčového slova import
# %%
from typing import Callable, Tuple
from a02_load_filter_in_memory import load_data

people = load_data("osoby.csv")
print(people[:4])


# lidi co jsou těžší než bmi = k


def filter(people : tuple, filter_function:Callable[[Tuple[str]],bool]) -> list:
    filtered_people  = list()
    for person in people:
        if filter_function(person):
            filtered_people.append(person)
    return filtered_people

# %% [markdown]
# Soubor se nám opravdu načte za použití funkce, kterou jsme implementovali v minulém cvičení.
# Také ale věnujme pozornost tomu, že obdržíme výpis o počtu osob s podprůměrnou vahou a nášeho známého Hubeného Staříka.
# Stane se tak proto, že python, při zavádění nového 'modulu' musí vykonat všechny příkazy, které jsou v něm obsaženy.
# Pokud tedy kromě definice nových funkcí obsahuje i jejich volání nebo jiný funkční kód, prostě je zavolá. 
# S tímto problémem se umíme vypořádat, prozatím budeme však tento fakt mít na mysli, avšak nebudeme se jím zabývat.

# ## Zadání 
# Z načteného seznamu osob vyfiltrujte pouze ty, které mají obezitu jakéhokoli stupně.

# podváha < 18,5        	
# normální váha	18,5–24,9	
# nadváha	25–29,9	mírně   
# obezita 1. stupně	30–34,9	
# obezita 2. stupně	35–39,9	
# obezita 3. stupně	≥ 40

# %%
def is_obese(person: tuple) -> bool:
    firstname,lastname,weight,height,age = person
    bmi = float(weight) / ((float(height)/100)**2) ##MASK_RM##
    #print(f"bmi: {bmi}")
    #bmi = weight / height**2 #<--- tato řádka nám způsobí problémy
    return bmi > 30 ##MASK_RM##

#print(f"je 1. obezni? {is_obese(people[1])}")
#print(f"je 2. obezni? {is_obese(people[2])}")

def has_bmi_higher_than_k(person: tuple, k: int = 30) -> bool:
    firstname,lastname,weight,height,age = person
    bmi = float(weight) / ((float(height)/100)**2) ##MASK_RM##
    print(f"bmi: {bmi}")
    #bmi = weight / height**2 #<--- tato řádka nám způsobí problémy
    return bmi > k ##MASK_RM##    

def has_bmi_higher_than_k_factory(k: int = 30) -> Callable[[Tuple[str]],bool]:
    def has_bmi_higher_than_k(person: tuple) -> bool:
        firstname,lastname,weight,height,age = person
        bmi = float(weight) / ((float(height)/100)**2) ##MASK_RM##
        print(f"bmi: {bmi}")
        #bmi = weight / height**2 #<--- tato řádka nám způsobí problémy
        return bmi > k ##MASK_RM##    
    return has_bmi_higher_than_k 

print(f"je 1. obezni? {has_bmi_higher_than_k(people[1],25)}")


# %%

# f -> f(k:3)
h2 = has_bmi_higher_than_k_factory(30)
fp = filter(people,lambda p: has_bmi_higher_than_k(p,56))

fp2 = [x for x in people if has_bmi_higher_than_k(x,56)]
people==3

print(fp[:4])

#print(filtered_people[:4])
# %%


