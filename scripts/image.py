import dotenv
from python_on_whales import docker
from poetry.core.pyproject.toml import PyProjectTOML
from poetry.core.semver import parse_constraint

PYPROJECT = PyProjectTOML("pyproject.toml")
SOURCE = PYPROJECT.poetry_config["repository"]
IMG_NAME = PYPROJECT.poetry_config["name"]
IMG_VERS = PYPROJECT.poetry_config["version"]
IMG_REPO = f"ghcr.io/tjpalanca/{IMG_NAME}:{IMG_VERS}"
IMG_LTST = f"ghcr.io/tjpalanca/{IMG_NAME}:latest"
IMAGES = [IMG_REPO, IMG_LTST]
TEST_PORT = 3838
ENVIRONMENT = dict(dotenv.dotenv_values())


def build():
    py_constraint = parse_constraint(PYPROJECT.poetry_config["dependencies"]["python"])
    docker_version = str(py_constraint.min)
    docker.build(
        context_path=".",
        build_args={
            "BASE_IMAGE": f"python:{docker_version}",
            "SOURCE": SOURCE,
            "POETRY_VERSION": "1.1.13",
        },
        tags=IMAGES,
    )


def push():
    docker.push(IMAGES)


def run(command=[]):
    docker.run(
        image=IMG_REPO,
        command=command,
        envs=ENVIRONMENT,
        tty=True,
        interactive=True,
    )


def shell():
    docker.run(command=["bash"])
