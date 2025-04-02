from pathlib import Path

import aind_behavior_experiment_launcher.launcher.behavior_launcher as behavior_launcher
from aind_behavior_experiment_launcher.apps import AindBehaviorServicesBonsaiApp
from aind_behavior_services.session import AindBehaviorSessionModel
from pydantic_settings import CliApp

from {{ cookiecutter.package_name }}.rig import {{ cookiecutter.class_suffix }}Rig
from {{ cookiecutter.package_name }}.task_logic import {{ cookiecutter.class_suffix }}TaskLogic


def make_launcher(settings: behavior_launcher.BehaviorCliArgs) -> behavior_launcher.BehaviorLauncher:
    data_dir = r"C:/Data"
    srv = behavior_launcher.BehaviorServicesFactoryManager()
    srv.attach_bonsai_app(AindBehaviorServicesBonsaiApp(Path(r"./src/main.bonsai")))

    return behavior_launcher.BehaviorLauncher(
        rig_schema_model={{ cookiecutter.class_suffix }}Rig,
        session_schema_model=AindBehaviorSessionModel,
        task_logic_schema_model={{ cookiecutter.class_suffix }}TaskLogic,
        services=srv,
        settings=settings,
        picker=behavior_launcher.DefaultBehaviorPicker(
            config_library_dir=Path(r"\\allen\aind\scratch\AindBehavior.db\{{ cookiecutter.class_suffix }}")
        ),
    )


def main():
    args = CliApp().run(behavior_launcher.BehaviorCliArgs)
    launcher = make_launcher(args)
    launcher.main()
    return None


if __name__ == "__main__":
    main()