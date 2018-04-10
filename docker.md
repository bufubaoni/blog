# Docker 相关
## 基础操作
Dockerfile 的语意为每一个regoin 做cache，这样可以保证文件快速的被解释。

 - docker run -it --rm image_name:version /bin/bash (进入docker 镜像的bash)
    -p 绑定端口
    -v 文件系统
    --mount 双向挂载
 - docker built . （根据当前Dokerfile创建镜像）
 
 - docker tag 
 
 - docker pull <source>:<tag>

 - docker service ls 服务列表

 - docker exec -it <containter id> /bin/bash 进入运行中的 container 
## swarm service
使用docker-compose.yml启动service

 - docker stack deploy -c docker-compose.yml <service name>
 
service数量
 - docker service ls

 - docker service rm <service name> 停止服务

 - docker stop <service>

 - docker ps 可以看到运行中的docker镜像

 - docker-compose up 使用docker compose启动服务

 发生了一个docker 停机的时间，然后导致服务宕了，然后发现了两个docker进程，将两个进程都杀掉以后才恢复了一个，至于为什么会出现两个，可能就是因为一个停止失败了，另一个也没有完全起来