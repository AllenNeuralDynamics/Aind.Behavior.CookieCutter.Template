from typing import Literal

from aind_behavior_services.task_logic import AindBehaviorTaskLogicModel, TaskParameters
from pydantic import Field

__version__ = "0.1.0"


class {{ cookiecutter.class_suffix }}Parameters(TaskParameters):
    example_parameter: float = Field(default=0, title="Example parameter", description="This is an example parameter")


class {{ cookiecutter.class_suffix }}TaskLogic(AindBehaviorTaskLogicModel):
    """Olfactometer operation control model that is used to run a calibration data acquisition workflow"""

    name: Literal["{{ cookiecutter.repository_name.replace('.', '') }}"] = Field(default="{{ cookiecutter.repository_name.replace('.', '') }}", title="Name of the task logic", frozen=True)
    version: Literal[__version__] = __version__
    task_parameters: {{ cookiecutter.class_suffix }}Parameters = Field(..., title="Task parameters", validate_default=True)