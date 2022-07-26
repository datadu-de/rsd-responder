# RSD responder

## installation

```
mkdir rsd-responder
cd rsd-responder
python -m venv .venv
.venv\scripts\activate
pip install -r .\requirements.txt
uvicorn main:app --reload
```

## usage

After setup you have a local server running, that you c

```
Generate Schema Files=OnUse;Location=C:\TX_Sources\RestTest;Logfile=C:\TX_Sources\RestTest;Max Log File Count=2;Max Log File Size=10MB;URI=http://127.0.0.1:8000/;Verbosity=5
```` 
