### Install requirement
```pip install -r requirments.txt```
### Configure
- ```cp uwsgi/uwsgi.ini.default uwsgi.ini``` and configure ```uwsgi.ini``` file according to your project
- ```cp supervisor/supervisor.conf.default supervisor/supervisor.conf``` and configure ```supervisor.conf``` file according to your project
### Run
```supervisord -c supervisor/supervisor.conf```
### Stop and Reload
- ```uwsgi --stop uwsgi/uwsgi.pid```
- ```uwsgi --reload uwsgi/uwsgi.pid```