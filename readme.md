# Auto HackRF GPS spoofing

Simple application which fetches latest BRDC file form Nasa archive, generates binary file for gps spoofing and makes HackRF One execute this file

## [CDDIS Nasa](https://cddis.nasa.gov)

You will need an account which can reach protected BRDC files in archive. After registration and signing in into your account you have to save your auth token to auth.json.

To achieve that you need to

1. Open developer tools on the website
2. Go to storage tab
3. Go to cookies section
4. Find ProxyAuth and urs_guid_ops cookies
5. Copy values to auth.json file

I'm not sure if urs_guid_ops cookie is required for authentication, so in some cases you can leave it blank in auth.json file

Example:

```
{
  "proxyAuthToken": "your_auth_token",
  "ursGuidOps": ""
}

```

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
