COMMANDE :

INSTALL PIP
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
py get-pip.py
py -m pip install --upgrade pip

VENV
py -3 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.venv\Scripts\activate
pip install flask

SERVER
python app.py

ANNEXE
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt


ATTENTION
Avant utilisation changer : FICHIER_HASHES dans /trp-nsi/crawler.py
                            image_test dans /trp-nsi/test.py
                            FICHIER_JSON dans /trp-nsi/test.py