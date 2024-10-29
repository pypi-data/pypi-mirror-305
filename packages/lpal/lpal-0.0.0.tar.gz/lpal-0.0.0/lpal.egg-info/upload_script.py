import os
import subprocess

os.environ['TWINE_PASSWORD'] = "pypi-AgEIcHlwaS5vcmcCJGQ1ZDA5NWMzLWU5NGYtNDNhOS1iMDcyLTZiM2E4YzlkM2Q3YwACKlszLCIwMjQ0YWMwNS04ODAzLTQ1YmEtYjBiNS01YmU1NWY0Zjg0ZWUiXQAABiBB9D9QmJzGeHZczjpoTNFjZqW5KfJb5_ICQMlsZ6JJvg"
subprocess.run(["twine", "upload", "-u", "__token__", "dist/*"])
