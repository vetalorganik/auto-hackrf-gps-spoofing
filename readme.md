# Auto HackRF GPS spoofing

Simple application which fetches latest BRDC file form Nasa archive, generates binary file for gps spoofing and makes HackRF One execute this file

## Windows usage

1. Install Python
2. Install [Zadig](https://zadig.akeo.ie/) driver
3. Install PothosSDR
4. Connect HackRF One to your device
5. Double click on start_windows.bat

## Linux usage

1. Install hackrf package

   Ubuntu/Debian:

   ```
   sudo dnf apt-get install hackrf
   ```

   Fedora/Red Hat:

   ```
   sudo dnf install hackrf -y
   ```

   Gentoo Linux:

   ```
   emerge -a net-wireless/hackrf-tools
   ```

   Arch Linux:

   ```
   sudo pacman -S hackrf
   ```

2. Make start_linux.sh executable

   ```
   sudo chmod +x start_linux.sh
   ```

3. Run script:
   ```
   ./start_linux.sh
   ```
