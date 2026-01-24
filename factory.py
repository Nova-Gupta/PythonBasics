class AWS:
    pass

class Azure:
    pass

class CloudFactory:
    @staticmethod
    def get_provider(name):
        if name == "aws":
            return AWS()
        elif name == "azure":
            return Azure()
        else:
            raise ValueError(f"Unknown provider: {name}")
# Example usage:
provider = CloudFactory.get_provider("aws")
print(type(provider))  # <class '__main__.AWS'>
provider = CloudFactory.get_provider("azure")
print(type(provider))  # <class '__main__.Azure'>
#provider = CloudFactory.get_provider("gcp")  # Raises ValueError