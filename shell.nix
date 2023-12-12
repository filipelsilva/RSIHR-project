{ pkgs ? import <nixpkgs> {} }:
let
	packages = ps: with ps; [
		gtts
		pyqt5
		netifaces
		requests
	];
	my-python = pkgs.python39.withPackages packages;
in
pkgs.mkShell {
	buildInputs = [
		my-python
	];

	QT_QPA_PLATFORM_PLUGIN_PATH="${pkgs.qt5.qtbase.bin}/lib/qt-${pkgs.qt5.qtbase.version}/plugins";
}
