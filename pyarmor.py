import os

module_list = ['features']

for module in module_list:
    os.system(
        f"pyarmor gen -O encoded_project -r -i src/featuredemov3/{module}")
os.system("pyarmor gen -O encoded_project -i src/featuredemov3/main.py")
os.system("pyarmor gen -O encoded_project -i src/featuredemov3/cmdline.py")
