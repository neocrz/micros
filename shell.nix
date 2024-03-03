{ pkgs ? import <nixpkgs> { }}:

with pkgs; let
  pythonpkgs = python3.withPackages (ps: with ps; [
    flask
    flask-bcrypt
    flask-jwt-extended
    flask-sqlalchemy
    gunicorn
  ]);
in mkShell {
  buildInputs = [
    pythonpkgs
    # metabase
  ];
}
