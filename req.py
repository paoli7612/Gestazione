import requests
from bs4 import BeautifulSoup

def canzone(url, nomeCanzone, nomeArtista):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")

    div = soup.find('div', {'class': 'chiave'})
    try:
        with  open('canzoni/' + nomeArtista.strip() + "." + nomeCanzone.strip() + ".txt", 'w', encoding="utf-8") as f:
            print(nomeCanzone.strip())
            for r in div.text.split('\n'):
                r = r.strip()
                if not r:
                    continue
                # togli righe con almeno uno di questi accordi
                chords = False
                for c in ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']:
                    if c in r:
                        chords = True
                if (chords):
                    continue

                # scrivi riga sul file di testo
                f.write(r + '\n')
    except:
        pass
def artista(url, nomeArtista):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")
    for div in soup.find_all('div', {'class': 'archives'}):
        nomeCanzone = div.text
        canzone(div.find('a')['href'], nomeCanzone, nomeArtista)

response = requests.get('https://www.accordiespartiti.it/accordi-chitarra/')
soup = BeautifulSoup(response.text, 'html.parser', from_encoding="utf-8")

div = soup.find('ul', {'id': 'italiani'})
links = div.find_all('a')

for link in links:
    artista(link['href'], link.text)
