# %% [markdown]
# 
# # Zadání 
# Napište funkci, která načte data ze souboru a odpoví nám na otázku: "Kolik osob má podprůměrnou váhu" 
# průměrnou váhu osob, které jsou 
#
# Když se zamyslíme nad kroky, které vedou k řešení, zjistíme, že potřebujeme:
# - Získat průměrnou váhu osob 
# - Spočítat osoby, které mají váhu menší než je ta průměrná.
#
# Pokud bychom chtěli implementovat novou funkci, která by měla na vstupu jméno souboru a nějaký limit (číslo -- maximální váhu)
# Brzy zjistíme, že náš program není ideálně dekomponovaný. Soubor otevíráme dvakrát (pro vypočítání průměru a pro filtrování osob)
# Tuto skutečnost bychom měli ihned jak ji odhalíme napravit a příště ji pokud možno identifikovat dříve. 
# Například příliš dlouhý a složitý název funkce: load_data_and_count_mean, nám může napovědět, že funkce dělá více věcí, než by měla.
# Konkrétně 2 věci: 
# - načítá data 
# - počítá průměr.
#
# Společnou část obou funkcí(načtení dat) tedy můžeme extrahovat do samostatné funkce. Výsledkem bude:
# - kratší zdrojový kód -> přehlednější
# - přehlednější -> snadnější identifikace chyb
# - případnou chybu opravíme pouze na jednom místě. 
# - kód se nám bude tedy lépe udržovat a rozšiřovat
# - příště, až budeme opět potřebocat načítat osoby ze souboru, můžeme opět použít již existující funkci a ušetřit čas a práci
# 
# # Připravte tedy funkci load_data(filename), která načte data ze souboru a vrátí seznam osob.
# Vstup: jméno souboru
# Výstup: seznam osob

# %%
def load_data(filename: str) -> list:
    people = list()
    with open(filename, encoding="utf8") as f:
        for line_number,line in enumerate(f):
            
            # TODO pridejme podmínku, která přeskočí první řádek v souboru
            ## ########### ## ##  
                ########          
            
            line = line.strip() 
            data = line.split(",")
            
            # v předchozím cvičení jsme si všechny hodnoty uložili do proměnných,
            # nyní uložíme celý rozdělený do seznamu lidí
            # jmeno, prijmenni, vek, vaha = data
            people.append(data)
    return people    

# %% [markdown]
# Také upravíme funkci z minulého cvičení tak, aby využívala nově vytvořenou funkci pro načítání dat.
# Upravujeme tedy definici vstupu. Funkce nyní nepřijímá jméno souboru ale seznam osob.
# Vstup seznam osob
# Výstup: průměrná váha osob

# %%
def count_avg_weight(people : list) -> float:
    weight_sum = 0
    weight_count = 0
    for person in people:
        firstname,lastname,weight,height,age = person
        # TODO na dvou následujících řádcích přičtěme váhu a zvýšeme počet osob
        ########## ## #############  
        ############ ## #           
    return weight_sum/weight_count


# %% [markdown]
# Nyní zavoláme funkci pro načtení dat a uložíme výsledek do proměnné people.
# V zápětí spočítáme průměrnou váhu osob a uložíme ji do proměnné avg_weight.

# %%
people = load_data("osoby.csv")
avg_weight = count_avg_weight(people)

# %%
# Nejlepší na tom je to, že pro spočtení osob, které mají podprůměrnou váhu, už máme polovinu práce hotovou (načtení dat).
# Vhodnou dekompozicí si tedy můžeme velice usnadnit práci. 
# Nyní stačí jenom projít všechny osoby a spočítat ty, které mají váhu menší než je průměrná.
# Vytvoříme tedy novou funkci filter_people_by_weight
# Vstup seznam osob, limitní váha
# Výstup: seznam osob, které mají váhu menší než je limitní váha

def filter_people_by_weight(people : list, limit : float) -> list:
    filtered_people = list()
    for person in people:
        
        # všimněme si, že funkce počítá, že data přichází v konkrétním pořadí. 
        # pokud bychom dostali soubor v jiném formátu, mohli bychom narazit na problém.
        firstname,lastname,weight,height,age = person
        weight = float(weight)
        if float(weight) < limit: # váha je 
            # TODO přidejme osobu do seznamu osob pomocí funkce append
            ############################## 
    return filtered_people


# %% [markdown]
# Všimněme si, že funkce, kterou jsme napsali, neodpovídá přímo na otázku, kolik osob má podprůměrnou váhu.
# Ale vrací nám seznam osob, které mají váhu menší než je limitní váha.
# Pokud bychom napsali funkci, která vrátí pouze počet osob, odřízli bychom se od možnosti provádět další operace nad filtrovanými osobami.
# Například pokud bychom chtěli vyrobit histogram věku osob, které mají podprůměrnou váhu, museli bychom zasahovat do funkce, upravovat jeji
# funkcionalitu. Takto napsaná funkce je mnohem univerzálnější a můžeme ji použít v mnoha dalších situacích. Odpověď na původní otázku získáme
# jednoduchým zjištěním velikosti seznamu.
# Během svého života všichni narážíme na situace, kdy nám chybí nějaká znalost. Programátoři nejsou jiní a jejich denní rutinou
# je vyhledávání věcí, které ještě neví nebo už zapomněli.
# Pokud se taková situace stane, otevřeme oblíbený webový vyhledávač a zeptáme se. 
# Tedy například : 'How to count items in list python'
# Procvičme si tuto dovednost a doplňme samostatně chybějící řádek.

# %%
light_people = filter_people_by_weight(people,avg_weight)
# TODO na následujícím řádku vyplňme počet prvků v seznamu
n_of_light_people = 0
print(f"Počet osob s podprůměrnou váhou je: {n_of_light_people}")

# %% [markdown]
# Závěrem
# Připomeňme si, že jsme se v tomto cvičení naučili identifikovat znaky špatné dekompozice programu (dlouhá a komplexní pojmenování funkcí)
# a naučili jsme se, jak je možné takovou situaci řešit. Společné části jsme extrahovali do samostatné funkce (načtení dat)
# tato data poté slouží pro další zpracování (výpočet průměru, filtrování osob podle váhy)
# Při návrhu nové funkcionality pro spočtení osob s podprůměrnou váhou jsme využili již existující funkce pro načtení dat a navíc mysleli na to,
# abychom se nedopustili stejné chyby -- příliš konkrétní úzké funkcionality, která není znovu použitelná. 
# Schválně, zkuste doimplementovat funkci, která nám poví maximální věk osoby s podprůměrnou váhou.

# %%

def max_age_person(people : list) -> tuple:
    top_age = 0
    grandpa = None
    for person in people:
        firstname,lastname,weight,height,age = person
        age = int(age)
        weight = float(weight)
        if int(age) > top_age:
            top_age = age
            grandpa = person
    return grandpa

light_weighted_grandpa = max_age_person(light_people)
print(f"Nejstarší osoba s podprůměrnou váhou je: {light_weighted_grandpa}")
# 
# 
# # %% [markdown]
# Nyní můžeme funkci použít pro načtení dat ze souboru osoby.csv
# Vstupem naší funkce je název souboru, ze kterého chceme data načíst.
# Výstupem naší funkce je seznam načtených osob.
# Funkci zavoláme a podíváme se co nám vrátí.


# %% [markdown]
# Tento program není indeálně dekomponovaný. Soubor, bychom nemuseli načítat dvakrát.
# Děje se tak jednou v importované funkci, která ze souboru načítá data a podruhé v naší funkci, 
# když filtrujeme osoby podle váhy.
# Takovou situaci bychom příště měli identifikovat dříve. Například složitý názef funkce: 
# load_data_and_count_mean, nám může napovědět, že funkce dělá více věcí, než by měla.
# Konkrétně 2 věci: načítá data a počítá průměr.
# 

# %%

