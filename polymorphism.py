class CloudProvider:
    def deploy(self):
        pass
class AWS(CloudProvider):
    def deploy(self):
        return "Deploying on AWS"
class Azure(CloudProvider):
    def deploy(self):
        return "Deploying on Azure"
class GCP(CloudProvider):
    def deploy(self):
        return "Deploying on GCP"
def deploy_application(provider: CloudProvider):
    print(provider.deploy())
# Example usage
if __name__ == "__main__":
    aws = AWS()
    azure = Azure()
    gcp = GCP()
    deploy_application(aws)
    deploy_application(azure)
    deploy_application(gcp)