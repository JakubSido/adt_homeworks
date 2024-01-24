# %% [markdown]
# 
# # Úloha 1 načtení a transformace dat

# Pro datovou analýzu je jedním z prvních kroků načtení datového vzorku. 
# Pro hlubší pochopení způsobu, jakým počítačové programy data zpracovávají nyní 
# naprogramujeme jednoduchou konzolovou aplikaci pro analýzu dat.

# %% [markdown]
# ## Funkce 
# Funkce v progrmaovacích jazycích má vstupy a výstupy.
# Princip je velice podobný jako u matematických funkcí (např. $f(x) = x^2$).
# tato funkce přijímá x(číslo) a vrací jeho druhou mocninu (číslo)
# $$ f(číslo) -> číslo$$

# ## Co je vstup a co výstup? 
# My máme podobné zadání, jen s tím rozdílem, že do naší funkce vstupuje cesta k soubor a vrací průměrnou váhu všech osob v souboru.
# Na první pohled je jasné, že jsou nutné předpoklady i pro naši funkci. 
# - Například musí vstupovat soubor, který existuje. 
# - Soubor musí obsahovat záznamy o osobách v konkrétním tvaru. 
# - Musí být přítomna informace o váze každé osoby.
# - atd. 

# Základní mechanismus je však stejný, funkce přijímá vstup a vrací výstup, jaký typ vstupu přijímá a jaký výstup vrací je již na nás.
# Většina programovacích jazyků umožňuje informaci o vstupu a výstupu přímo zapsat do zdrojového kódu.
# Tím sobě i ostatním programátorům usnadníme práci a zároveň zvýšíme přehlednost kódu.
# V pythonu se paramety a jejich typy zapisují do závorky za názvem funkce.
# To co funkce vrací popisujeme za šipku ->
# Tedy například:

# ```python
# # sčítáme dvě celá čísla a vracíme celé číslo
# def add_two_numbers(a : int, b:int) -> int
# # načítáme data ze souboru, jehož umístění je pžedáno jako řetězec a vracíme seznam
# # vhodným pojmenováním navíc pomáháme zlepšit čitelnost kódu
# def load_data(filepath : str) -> list
# ```

# Nejprve si tedy ujasníme tyto základní informace a můžeme začít programovat. 
# Samotný zdrojový kód funkce popisuje, jakým způsobem se vstupní data převedou na výstupní data.

# ## Jak uděláme to co máme? 
# Funkce otevře soubor uložený na disku a spočítá průměrnou váhu všech vzorků (osob). 
# Protože se jedná o jednoduchou informaci, můžeme chtěnou hodnotu spočítat průběžně. 

# Průměr můžeme spočítat pomocí vzorce:
# $$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$
# Nebo chcete-li:
# $$ \bar{x} = \frac{x_1+x_2+ x_3 + ... +x_n}{n}$$

# Postupně přečteme jednu osobu za druhou a povedeme si průběžný součet vah a počtu osob.
# Jedinné dvě proměnné, které budeme potřebovat tedy jsou:
# - proměnná, do které budeme ukládat součet vah (postupně nasčítávaný čitatel)
# - proměnná, do které budeme ukládat počet vzorků (postupně nasčítávaný jmenovatel)

# ### Poznámky:
# enumerate v cyklu nám umožní procházet řádky v souboru a zároveň nám vrátí číslo řádku


# %%
def load_data_and_count_mean(filename : str) -> float:
    
    # otevřeme soubor (mohli bychom ověřovat, že soubor existuje, ale pro jednoduchost to nebudeme dělat)
    with open(filename) as f:
        
        # inicializujeme proměnné, do kterých budeme ukládat mezivýsledek
        weight_sum = 0    # čitatel
        weight_count = 0  # jmenovatel
        
        # projdeme všechny řádky souboru, které představují jednotlivé osoby
        for line_number,line in enumerate(f):
            if line_number == 0:  # první řádek (počítáno od nuly) neobsahuje osobu, ale hlavičku, 
                continue        # proto ho přeskočíme
            
            # každý řádek má na konci speciální znak \n (konec řádku), toho se zbavíme pomocí funkce strip
            # funkce vrací nový řetězec, který je bez znaku \n
            line = line.strip() 
            
            # vyčištěný řádek rozdělíme pomocí čárky, funkce nám vrátí seznam hodnot (jméno, prijmenni, vek, vaha)
            data = line.split(",")
            
            # všechny hodnoty si uložíme do proměnných, všechno jsou to řetězce (string)
            firstname,lastname,weight,height,age = data
            
            # protože chceme spočítat průměr, musíme řetězec převést na desetinné číslo, to násleně můžeme nasačítat
            weight_sum += float(weight)
            weight_count += 1

    average = 0 # <-- TODO tuto řádku upravte tak, aby funkce vracela průměr
    return average

# %% [markdown]
# Funkci jsme definovali -- naprogramovali.
# 
# Nyní ji můžeme zavolat a výsledek vypsat.
#
# Jiným jazykem řečeno vstup (soubor osoby.csv) předáme funkci a 
# výstup (průměrná váha) uložíme do proměnné avg_weight.
# Ten následně vypíšeme pomocí funkce print.

# %%
avg_weight = load_data_and_count_mean("osoby.csv")
print(f"Průměrná váha osob v souboru je :{avg_weight}")

# %%

# %% [markdown]
# # Závěr
# Funkcionalita, kterou jsme naprogramovali je velice jednoduše replikovatelná
# v jakémkoli tabulkovém procesoru Excel, Google Tabulky.
# Rozdíl je v tom, že programovací jazyk nám dává mnohem větší volnost.
# Nemusíme se omezovat pouze na vstup ve formě taubulkových data (v našem případě csv soubor)
# můžeme zpracovávat data z databází, nebo například procházet celé adresářové 
# struktury složek a souborů uložené na disku a zpracovávat data uložená v nich. 
#
# Obecně vstupem programu může být cokoli, např. obrázek, zvuk, video, pdf nebo třeba i otázka.
# Stejnou svobodu máme ve výstupu programu. Obecněji se můžeme bavit o vnějším projevu programu, 
# který jsme napsali. Komplexní program může například obsluhovat internetové stránky.
# %%

