# python-solr-processor
*Functionality isn't final*

Document processors written in python. Application processes xml, csv, or json into appropriate json schema and index
into Solr

### Start API application
* `uvicorn app.main:app --reload`

### Start RabbitMq
* ` docker run -d --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management`
