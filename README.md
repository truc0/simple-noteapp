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
- The `daemonize` option is the log of **uWSGI daemon**, **NOT THE APP**. Please make sure the user who starts `uWSGI` has permission in that directory

### Start the app

Using the following command to start the app:

```bash
uwsgi --ini uwsgi.ini
```

More info about deploying app with `uWSGI` can be found in [uWSGI docs](https://uwsgi-docs.readthedocs.io/en/latest/).


## API docs

TBA