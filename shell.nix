{ pkgs ? import <nixpkgs> {} }:
let
	packages = ps: with ps; [
		pyqt5
		netifaces
	];
	my-python = pkgs.python39.withPackages packages;
in my-python.env

