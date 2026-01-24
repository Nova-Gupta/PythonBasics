class Server:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Server({self.name})"
    def __repr__(self):
        return f"Server(name={self.name!r})"
# Example usage:
server = Server("MyServer")
print(str(server))   # Output: Server(MyServer)