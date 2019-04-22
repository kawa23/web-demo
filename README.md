### Install requirement
```pip install -r requirments.txt```
### Configuration project environment
- ```cp uwsgi/uwsgi.ini.default uwsgi.ini``` and configuration ```uwsgi.ini``` file according to your project
- ```cp supervisor/supervisor.conf.default supervisor/supervisor.conf``` and configuration ```supervisor.conf``` file according to your project
### Run
```supervisord -c supervisor/supervisor.conf```
### Stop and Reload
- ```uwsgi --stop uwsgi/uwsgi.pid```
- ```uwsgi --reload uwsgi/uwsgi.pid```