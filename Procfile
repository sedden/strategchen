#web: gunicorn strategchen.wsgi --log-file -
web: newrelic-admin run-program gunicorn strategchen.wsgi --log-file -
worker: celery --app=strategchen worker -l info
