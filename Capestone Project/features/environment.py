import os
import platform
import sys
import allure


def before_all(context):
    """Runs once before all tests. Populates Allure Environment Metadata."""
    results_dir = "allure-results"

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    env_file_path = os.path.join(results_dir, "environment.properties")

    env_data = {
        "Python.Version": sys.version.split()[0],
        "Platform": platform.system(),
        "Platform.Release": platform.release(),
        "Base.Target": "AutomationExercise API Suite",
        "Framework": "Behave BDD + Requests",
    }

    with open(env_file_path, "w", encoding="utf-8") as env_file:
        for key, value in env_data.items():
            env_file.write(f"{key}={value}\n")


def before_scenario(context, scenario):
    """Runs before each scenario to attach scenario details to Allure."""
    allure.dynamic.feature(scenario.feature.name)
    allure.dynamic.story(scenario.name)


def after_scenario(context, scenario):
    """Runs after each scenario to attach failure status if applicable."""
    if scenario.status == "failed":
        allure.attach(
            f"Scenario '{scenario.name}' failed during execution.",
            name="Failure Log",
            attachment_type=allure.attachment_type.TEXT,
        )