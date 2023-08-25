#!/bin/bash

$SRC_KUBE_CONFIG = ""
$DES_KUBE_CONFIG = ""
export KUBECONFIG = $SRC_KUBE_CONFIG
kubectl get ingress -A -o yaml > ingress.yaml

python3 transform_ingress.py
export KUBECONFIG = $DES_KUBE_CONFIG

kubectl apply -f transformed_ingress.yaml

rm ingress.yaml
rm transformed_ingress.yaml
