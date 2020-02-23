for x in `cat docker-compose.env`; do export $x; done
for x in `cat __local.env`; do export $x; done