### Install requirement
```pip install -r requirments.txt```

### Configure
- configure uwsgi 

    ```cp uwsgi/uwsgi.ini.default uwsgi.ini``` and configure ```uwsgi.ini``` file according to your project

- configure supervisor

    ```cp supervisor/supervisor.conf.default supervisor/supervisor.conf``` and configure ```supervisor.conf``` file according to your project
    
- configure database

    ```cp config.ini.default config.ini``` and configure ```config.ini``` file according to your project
    
### Run
```supervisord -c supervisor/supervisor.conf```

### Stop and Reload
- ```uwsgi --stop uwsgi/uwsgi.pid```
- ```uwsgi --reload uwsgi/uwsgi.pid```