import datetime
import os

from aind_behavior_services.session import AindBehaviorSessionModel
from {{ cookiecutter.package_name}}.task_logic import {{ cookiecutter.class_suffix }}Parameters, {{ cookiecutter.class_suffix }}TaskLogic
from {{ cookiecutter.package_name}}.rig import {{ cookiecutter.class_suffix }}Rig



def mock_session() -> AindBehaviorSessionModel:
    """Generates a mock AindBehaviorSessionModel model"""
    return AindBehaviorSessionModel(
        date=datetime.datetime.now(tz=datetime.timezone.utc),
        experiment="{{ cookiecutter.class_suffix }}",
        root_path="c://",
        subject="test",
        notes="test session",
        experiment_version="0.0.0",
        allow_dirty_repo=True,
        skip_hardware_validation=False,
        experimenter=["Foo", "Bar"],
    )


def mock_rig() -> {{ cookiecutter.class_suffix }}Rig:

    return {{ cookiecutter.class_suffix }}Rig(
        rig_name="test_rig",
    )


def mock_task_logic() -> {{ cookiecutter.class_suffix }}TaskLogic:

    return {{ cookiecutter.class_suffix }}TaskLogic(
        task_parameters={{ cookiecutter.class_suffix }}Parameters()
    )


def main(path_seed: str = "./local/{schema}.json"):
    example_session = mock_session()
    example_rig = mock_rig()
    example_task_logic = mock_task_logic()

    os.makedirs(os.path.dirname(path_seed), exist_ok=True)

    for model in [example_task_logic, example_session, example_rig]:
        with open(path_seed.format(schema=model.__class__.__name__), "w", encoding="utf-8") as f:
            f.write(model.model_dump_json(indent=2))


if __name__ == "__main__":
    main()