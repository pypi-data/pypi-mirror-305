# Uvicorn SSL Restarter

This service is intended to be used with any uvicorn application to automatically restart it when new SSL-Certificates are available.

## Usage

```sh
pip install uvicorn-ssl-restarter
```

Import the `UvicornSSLRestarter` class into your `entrypoint.py` file. (Or wherever you start your Uvicorn server).

```
from app.uvicorn_ssl_restarter import UvicornSSLRestarter
```

Start the server using:

```python
uvicorn_ssl_restarter = UvicornSSLRestarter(
    virtual_host="example.com",
    app_path="app.main:app",
    fallback_certs_dir="/app/fallback-certs",
    real_certs_dir="/app/certs",
    renew_check_interval=60*60*2, # Seconds between checks for new certificates
    server_port=443,
)
await uvicorn_ssl_restarter.run()
```

Change variables as needed.

## Publish package

Update the version in the `pyproject.toml` and then run:

```sh
uv sync
uv build
# make sure that UV_PUBLISH_TOKEN is populated with your pypi token
uv publish
```
(Make sure to first enable a virtual environment with the required dependencies)
