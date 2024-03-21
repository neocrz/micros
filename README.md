# Micros
An experimental 'Service Order' (Ordem de Serviço) API made with Flask.

**Features**
- Clients, Equipments, Orders, ...

## Utilization
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

### Before running `run.py`
There is no routes for creating a Role and User. Remember to create via python before running `python run.py`.

## Todo
- [ ] Role
    - [x] Basic Role model
- [ ] User
    - [x] Basic User model
- [ ] Host
    - [ ] Host model
- [ ] Auth
    - [x] API Auth System (by User login)
- [ ] Client
    - [x] Basic Client Model
    - [x] Base CRUD
- [ ] Equipments
    - [x] Basic Equipment Model
    - [x] Base CRUD
- [ ] Orders
    - [x] Basic Order Model
    - [ ] Base CRUD
- [ ] Supplier
    - [ ] Basic Supplier Model
    - [ ] Base CRUD
- [ ] Make a unique db model for Client, Host, Supplier commons


