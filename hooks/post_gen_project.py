
def pascal_to_snake_case(s: str) -> str:
    result = ""
    for i, char in enumerate(s):
        if char.isupper():
            if i != 0:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result


suffix = "{{ cookiecutter.class_suffix }}"
suffix = pascal_to_snake_case(suffix)

task_logic_template = f"""
json-schemas.task_logic
-------------------------

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/{{ cookiecutter.repository_name }}/main/src/DataSchemas/{suffix}_task_logic.json>`_

.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/{{ cookiecutter.repository_name }}/main/src/DataSchemas/{suffix}_task_logic.json
   :lift_definitions:
   :auto_reference:
"""

rig_template = f"""
json-schemas.rig
------------------

`Download Schema <https://raw.githubusercontent.com/AllenNeuralDynamics/{{ cookiecutter.repository_name }}/main/src/DataSchemas/{suffix}_rig.json>`_

.. jsonschema:: https://raw.githubusercontent.com/AllenNeuralDynamics/{{ cookiecutter.repository_name }}/main/src/DataSchemas/{suffix}_rig.json
   :lift_definitions:
   :auto_reference:

"""

def main():

    with open("docs/json-schemas.task_logic.rst", "a") as f:
        f.write(task_logic_template)

    with open("docs/json-schemas.rig.rst", "a") as f:
        f.write(rig_template)

    print("Project initialized!")



if __name__ == "__main__":
    main()