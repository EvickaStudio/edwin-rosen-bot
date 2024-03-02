# Edwin Rosen Bot

Falls du keine weiteren Konzerte verpassen willst, ist dieser einfache Bot die perfekte Lösung für dich.

Dieser Bot überprüft die REST API von https://edwinrosen.de/faceless/pwa/1/catalog/products?type=Ticket und sendet eine Nachricht an den Discord-Webhook, falls sich der Inhalt der Antwort dieser Anfrage verändert hat (hoffentlich neue Tickets).

> [!NOTE]
> Ich konnte den Bot bisher noch nicht richtig testen, weshalb er evtl. nicht richtig erkannt wird, wenn es neue Tickets gibt.

## Voraussetzungen

- Python 3
- pip

## Installation

1. Klone die Repository:

```sh
git clone https://github.com/evickastudio/edwin-rosen-bot.git
cd edwin-rosen-bot
```

2. Erstelle eine virtuelle Umgebung und aktiviere sie (optional):

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Installiere benötigte Bibliotheken:

```sh
pip install -r requirements.txt
```

4. Kopiere die `.env_example` Datei und benenne sie in `.env` um. Aktualisiere die Url.

## Nutzung

Starte den Bot mit dem folgenden Befehl:

```sh
python main.py
```

Der Bot läuft nun im Hintergrund und überwacht die Website. Bei Änderungen sendet er eine Benachrichtigung an den in der `.env` Datei angegebenen Discord-Webhook.

## Lizenz

Dieses Projekt steht unter der Apache 2.0 Lizenz. Weitere Informationen finden Sie in der [LICENSE](LICENSE) Datei.
