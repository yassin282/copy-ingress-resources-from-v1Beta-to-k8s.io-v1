""" Transform ingress resources to be compaitable with networking.k8s.io/v1"""
import yaml


def transform_ingress(file_name):
    with open(file_name, "r") as f:
        data = yaml.safe_load(f)

    for item in data["items"]:
        if item["kind"] == "Ingress" and item["apiVersion"] == "extensions/v1beta1":
            item["apiVersion"] = "networking.k8s.io/v1"

            for rule in item["spec"]["rules"]:
                for path in rule["http"]["paths"]:
                    path["pathType"] = "ImplementationSpecific"

                    backend_data = path.pop("backend")
                    new_backend_data = {
                        "service": {
                            "name": backend_data["serviceName"],
                            "port": {"number": backend_data["servicePort"]},
                        }
                    }
                    path["backend"] = new_backend_data

    with open("transformed_" + file_name, "w") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    transform_ingress("ingress.yaml")
