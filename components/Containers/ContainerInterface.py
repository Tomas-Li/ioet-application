from abc import ABC, abstractmethod

class ContainerInterface(ABC):
    
    #This will force to declare an adequate container in all children
    @property
    @abstractmethod
    def container(self) -> None:
        """
        Getter for container. The setting of the variable is done through the load methods
        """
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """
        This metod calls the correct method to read a file
        """



