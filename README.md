# Celery/AMPQ Example 

### Pull docker image with port forwarding
`docker run -d --hostname my-rabbit --name some-rabbit -p 8888:15672 -p 5671:5672 rabbitmq:3-management`

### Start celery workers
`celery -A tasks worker --concurrency 4 -P eventlet --loglevel=info`

### Dive into python and send reverse task 
`python`
`from tasks import reverse`
`r = reverse.delay("Vladimir Zhelnov")`
`print(r.status)`
`exit()`

### SQLite tasks results
`sqlite3 results.db`
`.tables`
`select * from celery_taskmeta;`
`.exit`
