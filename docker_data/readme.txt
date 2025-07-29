CONTAINER ID   IMAGE                              COMMAND                  CREATED      STATUS          PORTS                    NAMES
e74ada0e99a3   nginx                              "/docker-entrypoint.…"   2 days ago   Up 3 seconds    0.0.0.0:9000->80/tcp     nginx-app
c0144a93ab19   sunilgadhe/click-counter:web-app   "flask run"              2 days ago   Up 12 seconds   0.0.0.0:8085->5000/tcp   clickcounter
2fc4ff2eca9e   redis                              "docker-entrypoint.s…"   2 days ago   Up 33 seconds   0.0.0.0:6379->6379/tcp   redis
