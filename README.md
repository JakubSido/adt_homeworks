
# Vypracování domácích úloh
Pro vypracování domácích úloh máte několik možností 


1) Lokální použití VSCode doplňku (DOPORUČENO)
2) Cloudové řešení (např. google colab)

## Prostředí Visual Studio Code - DOPORUČENÉ
1. Nainstalujte doplněk pro VSCode https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
2. Vytvořte lokální kopii repozitáře
3. VSCode doplněk pro JupyterNotebooky umožní přímou interakci s notebookem.


## Prostředí Google Colab
Vytvořte si kopii celého repozitáře na vlastní google drive do složky **adt_homeworks**

Poté je možné notebook otevřít přímo z prostředí google disku. 

## Připojení GoogleDrive do prostředí GoogleColab
Pro připojení google disku k virutálnímu stroji interpretujícímu kód v jupyter notebooku můžeme použít následájící snippet. Po připojení se k souborům můžeme chovat tak, jako by byly přímo na pevném disku, tedy jako cestu k datům můžeme používat konstantu DATA_FILE

```python
from google.colab import drive
drive.mount('/content/drive/', force_remount=True)
DATA_FILE  = "/content/drive/MyDrive/adt_homeworks/data/osoby.csv"
```