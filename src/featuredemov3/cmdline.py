import uvicorn
from featuredemov3 import main


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("featuredemov3.main:app",
                host="0.0.0.0", port=10118, reload=False)


def test123():
    print(main.app)


if __name__ == '__main__':
    start()
