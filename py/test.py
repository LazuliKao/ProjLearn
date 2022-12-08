class TestClass:
    def __init__(self) -> None:
        print("new")
    @classmethod
    def fuck(cls):
        print(cls.__name__)
        newItem=cls()
        newItem=TestClass()
    def print(self,data):
        print(data)



TestClass.fuck()

print(TestClass.__name__)