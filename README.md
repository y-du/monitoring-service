### GET /logs/{container_name}

_Get complete log of a container._

### GET /logs/{container_name}?lines=100

_Get last 100 lines._

### GET /logs/{container_name}?since=2020-04-25T11:10:30Z

_Get all lines since 2020-04-25T11:10:30Z UTC._

### GET /logs/{container_name}?until=2020-04-25T11:10:30Z

_Get all lines up until 2020-04-25T11:10:30Z UTC._

### GET /logs/{container_name}?since=2020-04-25T11:10:30Z&until=2020-04-25T11:15:00Z

_Get all lines since 2020-04-25T11:10:30Z UTC up until 2020-04-25T11:15:00Z UTC._


**Timestamp Format: Y-m-dTH:M:SZ**