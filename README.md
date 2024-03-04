# Micros
An experimental 'Service Order' (Ordem de Serviço) API made with Flask.

**Features**
- Clients, Equipments, Orders, ...

## How to
### Nix Flake (nix develop)
- Clone the repo.
- `cd` to the repo directory.
- `nix develop .`

### No nix
- Clone the repo.
- `cd` to the repo directory.
- Create a new python venv
```console
python -m venv venv
```
- Activate the python environment.
```console
./venv/bin/activate # Linux
./venv/Scripts/activate.ps1 # Windows
```

- Install the dependencies
```
pip install -r requirements.txt
```

## Todo
- [ ] Auth
    - [x] Basic User Model
    - [x] API Auth System
- [ ] Client
    - [x] Basic Client Model
    - [x] Basic CRUD System
- [ ] Equipments
    - [ ] ...

