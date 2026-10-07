name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '4.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev libldns-dev zlib1g-dev
        python -m pip install --upgrade pip
        pip install --upgrade buildozer cython virtualenv

    - name: Build with Buildozer
      uses: ArtemSBulgakov/buildozer-action@v1
      id: buildozer
      with:
        command: buildozer -v android debug
        buildozer_version: master

    - name: Upload Artifact
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk
