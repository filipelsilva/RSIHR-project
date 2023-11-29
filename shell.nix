{ pkgs ? import <nixpkgs> {} }:
let
	packages = ps: with ps; [
		pyqt5
		netifaces
		requests
	];
	my-python = pkgs.python39.withPackages packages;
in
pkgs.mkShell {
	buildInputs = with pkgs; [
		# qt5
		my-python
		xorg.libXinerama
	];
}
