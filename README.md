# OpenLedRace back end part
## Stack: Django + REST API
### Requirements
```
$ pip install django gunicorn 
```
### How to run the app, and test the REST API ?
In one terminal, start the **Django** server:
```
$ gunicorn -b 0.0.0.0 config_prj.wsgi
```
In a second terminal, use **curl** to test the **REST API**, the response must be:
```
$ curl http://127.0.0.1:8000/test/ | jq                    127 ↵
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    83  100    83    0     0  41500      0 --:--:-- --:--:-- --:--:-- 41500
{
  "status": false,
  "waitingRoom": [
    "Thierry",
    "Nekroface",
    "WOoOinux",
    "JC_onLine"
  ]
}
```
## Screen
![Example home page 2020-08-24_22-31-56](/doc/screens/home-page_2020-08-24_22-31-56.png "rudimentary home page")