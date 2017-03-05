import os

license_type = '{{ cookiecutter.project_license }}'

if license_type == "None":
    os.remove("LICENSE")
