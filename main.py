#!/usr/bin/env python

import uvicorn

from api.api import create_app


def main():
    app = create_app()
    print("Goto http://localhost:8080/ or http://localhost:8080/redoc")
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
