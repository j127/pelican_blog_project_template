# Pelican Site Template

## Installation

Make a Python 3 virtual environment and install the dependencies:

```text
$ pip install -r requirements.txt
```

## Write

```text
$ make newpost title='the title of the post'
```

## Build

```text
$ make build
```

The output will be in the `build` directory.

## Deploy

After configuring the settings, this will build the blog and upload it to the live server over `scp`:

```text
$ make publish
```
