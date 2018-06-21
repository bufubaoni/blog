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
其实本地的swarm 一直就没有启动成功。
还是打算使用k8s来管理项目吧。

## k8s
minikube v0.25.2
minikube 安装需要google的镜像，总结出来了，如果镜像不能用，从阿里自行搜索
 -  docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-sidecar-amd64:1.14.5
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-sidecar-amd64:1.14.5 k8s.gcr.io/k8s-dns-sidecar-amd64:1.14.5
 
 -  docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-kube-dns-amd64:1.14.5
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-kube-dns-amd64:1.14.5 k8s.gcr.io/k8s-dns-kube-dns-amd64:1.14.5

 -  docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-dnsmasq-nanny-amd64:1.14.5
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/k8s-dns-dnsmasq-nanny-amd64:1.14.5 k8s.gcr.io/k8s-dns-dnsmasq-nanny-amd64:1.14.5

 -  docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/kube-addon-manager:v6.5
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/kube-addon-manager:v6.5 gcr.io/google-containers/kube-addon-manager:v6.5

 -  docker pull registry.cn-hangzhou.aliyuncs.com/kube_containers/kubernetes-dashboard-amd64:v1.8.1
 -  docker tag registry.cn-hangzhou.aliyuncs.com/kube_containers/kubernetes-dashboard-amd64:v1.8.1 k8s.gcr.io/kubernetes-dashboard-amd64:v1.8.1

 -  docker pull registry.cn-hangzhou.aliyuncs.com/google-containers/pause-amd64:3.0
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google-containers/pause-amd64:3.0 gcr.io/google_containers/pause-amd64:3.0
 -  docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/storage-provisioner:v1.8.1
 -  docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/storage-provisioner:v1.8.1 gcr.io/k8s-minikube/storage-provisioner:v1.8.1

 - docker pull registry.cn-hangzhou.aliyuncs.com/junv/kubernetes-bootcamp:v1 
 - docker tag registry.cn-hangzhou.aliyuncs.com/junv/kubernetes-bootcamp:v1 gcr.io/google-samples/kubernetes-bootcamp:v1

获取所有服务及pods
 - kubectl get all
创建服务
 - kubectl create -f xxx.yaml

更新compose config
- kubectl apply -f xxx.yaml

更新pod 的image
- ubectl set image deployment/app-deployment app=app-image

查看logs
- kubectl logs <deployment-instance>
