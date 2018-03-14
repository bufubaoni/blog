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