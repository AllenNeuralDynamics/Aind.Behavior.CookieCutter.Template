from cookiecutter.main import cookiecutter
from datetime import datetime

repository_name = "{{ cookiecutter.repository_name }}"
package_name = repository_name.replace(".", "_").lower()
project_name = package_name.replace("_", "-")

cookiecutter(
    "cookiecutter-django",
    extra_context={
        "year": datetime.now().year,
        "package_name": package_name,
        "project_name": project_name,}
)
