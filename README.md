# Simple Noteapp

> This app is still in development.

This is a simple noteapp with basic CRUD function for notes.

Users need to be authenticated before creating/editing/deleting their note.

It should be a good project for beginners of frontned development.

## Deploy

### Download the source code 

You can download the zip file of the source code by clicking the green button `Code` in this page or in the releases, and select `Download ZIP`.

You can also clone this project using `git` by the following comand:

```bash
git clone https://github.com/truc0/simple-noteapp.git
```

Then changing directory into the source code folder by:

```bash
cd simple-noteapp
```

### Create a Virtual Environment (Optional)

A virtual environment helps solving the conflict dependencies of different applications.

You can create a virtual environment by the following command:

```bash
python3 -m venv <path>
```

Change `<path>` to your installation location. Example:

```bash
python3 -m venv /home/truc0/venv
```

Then activate this virtual environment by:

```bash
source <path>/bin/activate  # For Unix-like OS
```

### Install Dependencies

The dependencies are specified in `requirements.txt`. You can use the following command to install them:

```bash
pip install -r requirements.txt
```

### Configure the app

Copy `noteapp/config.example.py` to `noteapp/config.py` using the following command:

```bash
cp noteapp/config.example.py noteapp/config.py
```

Please make sure the `DEBUG` option in `config.py` is set to `False` in production environment.

Then change other options such as `ALLOW_REGISTER`.

#### Django Secret Key

You can create a secret key by the following command:

```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Configure uWSGI (Optional)

It is recommended to use [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) to deploy this app but it is not required.

There is an example configuration of `uwsgi` in the root directory of this app (`uwsgi.example.ini`).

Copy the configuration by using:

```bash
cp uwsgi.example.ini uwsgi.ini
```

- The `chdir` option can be the directory of the source code
- The `home` directory **must contains** your python executable file, you can delete this line if you are using the global one instead of a virutal environment
- The `processes` option is the number of process allowed
- The `socket` option is a combination of `IP` and `port`. You can use `http` option instead if you want uWSGI directly serve content by `HTTP` 

### Start the app

Using the following command to start the app:

```bash
uwsgi --ini uwsgi.ini
```

More info about deploying app with `uWSGI` can be found in [uWSGI docs](https://uwsgi-docs.readthedocs.io/en/latest/).

#### Ubuntu & Debian Users Guide

For Ubuntu & Debian users, there is another way for installing the app.

First, install `uwsgi` and `uwsgi-plugin-python3` in system level:

```bash
sudo apt install uwsgi uwsgi-plugin-python3
```

Then, copy the configuration to `/etc/uwsgi/apps-enabled` by:

```bash
cp uwsgi.example.ini /etc/uwsgi/apps-available/noteapp.ini
ln -s /etc/uwsgi/apps-available/noteapp.ini /etc/uwsgi/apps-enabled/
```

Note that the commands above actually move the configuration to `/etc/uwsgi/apps-available` and create a symbol link to `/etc/uwsgi/apps-enabled`, you can directly copy the configuration to `/etc/uwsgi/apps-enabled` instead.


## API docs

TBA