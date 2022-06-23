"""
ContainerInterface.py
--------------------

File that defines the class ContainerInterface, an abstract class that works as an interface for the containers in the project

"""

#Built-in modules
from abc import ABC, abstractmethod

class ContainerInterface(ABC):
    """
    Interface for the container classes. Forces the creation of a main container and a load method

    Attributes:
    -----------
    container : Any
        It's an attribute (with only a getter method as the idea is to not be able to modify its contents without the correct method) that is defined through a method so that we can apply two decorators to it:
            @property -> to define it as an attribute
            @abstractmethod -> to impose the creations of the abstract methods

    Methods:
    --------
    load(self, path)
        Method that chooses the correct implementation to load data for the container attribute.
    """

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
        This metod calls the correct method to read a file and fill the container attribute
        
        Parameters
        ----------
        path : str
            A string for the path with the file to read (extension included)
        
        """

        pass
