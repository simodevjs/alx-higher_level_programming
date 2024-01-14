class Base:    
    """Base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class

        Args:
            id (int, optional): id of the instance, Defaults to None.
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects



