# RSD responder

A companion tool for TimeXtender ODX to help you develop your RSD files to create the API requests you want.

## installation

```
mkdir rsd-responder
cd rsd-responder
python -m venv .venv
.venv\scripts\activate
pip install -r .\requirements.txt
```

## usage

After setup you can run a local API server by using the included `launch.json` in Visual Studio Code or with this command on the command line:
```
uvicorn main:app --reload
```

That server will print to the console *and* return all *headers*, *query parameters* and *body content* that was sent to it as a response - perfect to see, what calls to the API are made as a result of your RSD file!

Just head back to your ODX, configure a REST data source and use a connection string similar to this:
```
Generate Schema Files=OnUse;Location=C:\TX_Sources\RestTest;Logfile=C:\TX_Sources\RestTest;Max Log File Count=2;Max Log File Size=10MB;URI=http://127.0.0.1:8000/;Verbosity=5
```

Next, execute the Syncronization task to generate a RSD file.

You can now edit the file and test the request(s) that it produces by executing a transfer task on the data source.

## prerequisites

- a recent version of python3 (tested with 3.9 and 3.10)
