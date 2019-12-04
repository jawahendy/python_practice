# # # factory method design pattern
# # work in repl

# from __future__ import annotations
# from abc import ABC, abstractclassmethod

# class Creator(ABC):
#   # @abstractmethod
#   def factory_method(self):
#     pass

#   def some_operation(self) -> str:
#     product = self.factory_method()
#     result = f" Creator : this is factory method"

#     return result

# class ConcreteCreator1(Creator):
#   def factory_method(self) -> ConcreteCreator1:
#     return ConcreteCreator1()

# class ConcreteCreator2(Creator):
#   def factory_method(self) -> ConcreteCreator2:
#     return ConcreteCreator2()

# class Product(ABC):

#   def operation(self) -> str:
#     pass

# class ConcreateProduct1(Product):
#   def operation(self) -> str:
#     return "{Result of the ConcreateProduct1}"

# class ConcreateProduct2(Product):
#   def operation(self) -> str:
#     return "{Result of Concreate product 2}"


# def client_code(creator : Creator) -> None:
#     print(f"Client: I'm not aware of the creator's class, but it still works.\n"f"{creator.some_operation()}", end="")

# if __name__ == "__main__":
#   print("App : Launched with concreate1")
#   client_code(ConcreteCreator1())
#   print("\n")

#   print("App : Launched with ConcreteCreator2")
#   client_code(ConcreteCreator2())