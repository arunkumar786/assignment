# assignment

programming tasks:
------------------
mergedictionary.py 

mergedictionary2.py  
       
urlsexample.py

Deployment tasks:
sentry_demo.yml

to run the above yaml, we need to setup the minikube first on ubuntu

follow the link to setup

https://linuxhint.com/install-minikube-ubuntu/

then do the following 

minikube start

kubectl create -f sentry_demo.yml

How to access the pods:
----------------------
1. kubectl get pods --> to check whether the pod is creating or not.
2. kubectl decribe <podname> --> also check the pod status.
3. next to port forward to access the application.

   kubectl port-forward 4000:7000 sentry.example.com

4. curl http://localhost:7000/run
