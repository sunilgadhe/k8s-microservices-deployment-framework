
## Kubernetes Infra Monitoring & Alerting Using Prometheus & Grafana

### Key components:
    1. Prometheus server - Processes and stores metrics data
    2. Alert Manager - Sends alerts to any systems/channels
    3. Grafana - Visualize scraped data in UI


### Installation Method:
- The are are many ways you can setup Prometheus and Grafana. You can install in following ways:

1. Create all configuration files of both Prometheus and Grafana and execute them in right order.
2. Prometheus Operator - to simplify and automate the configuration and management of the Prometheus monitoring stack running on a Kubernetes cluster
3. Helm chart (Recommended) - Using helm to install Prometheus Operator including Grafana

### Pre-requisites:
1. EKS Cluster needs to be up and running.
2. Install Helm3
3. EC2 instance to access EKS cluster

### Implementation steps:
#### 1. Add stable repo
-  We need to add the Helm Stable Charts for your local client. Execute the below command:
helm repo add stable https://charts.helm.sh/stable

#### 2. Add prometheus Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm search repo prometheus-community

#### 3. Create Prometheus namespace
kubectl create namespace prometheus

#### 4. Install kube-prometheus-stack
1. Below is helm command to install kube-prometheus-stack. The helm repo kube-stack-prometheus (formerly prometheus-operator) comes with a grafana deployment embedded.
- helm install stable prometheus-community/kube-prometheus-stack -n prometheus

2. Lets check if prometheus and grafana pods are running already
- kubectl get pods -n prometheus
- kubectl get svc -n prometheus


3. In order to make prometheus and grafana available outside the cluster, edit prometheus and grafana service & use LoadBalancer or NodePort instead of ClusterIP.
- kubectl edit svc stable-kube-prometheus-sta-prometheus -n prometheus
- kubectl edit svc stable-grafana -n prometheus

4. Verify if service is changed to LoadBalancer and also to get the Load Balancer URL.
- kubectl get svc -n prometheus

5. Access Grafana UI in the browser using LB DNS or custom DNS
- UserName: admin
- Password: prom-operator

6. Create Dashboard in Grafana
Import grafana dashboard as per your requirement (ID: 18283) & select prometheus data source
