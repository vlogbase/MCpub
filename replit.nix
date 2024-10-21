{ pkgs }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.poetry
  ];
}
