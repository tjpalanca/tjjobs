import requests
from . import image
from os import getenv


def deploy():
    resp = requests.post(
        url=getenv("CLOUD66_DEPLOY_URL"), params={"services": "tjjobs,tjjobs-gateway"}
    )
    print(resp.text)
    return


def build_and_deploy():
    image.build()
    image.push()
    deploy()
