from utils.db import db


class Base(db.Model):
    """Base class for the app models

    Args:
        db (SQLAlchemy): This class inherits from the SQLAlchemy Model class
    """

    @classmethod
    def create(cls, **kwargs):
        """Create an entry in the table, with the type of the class/model that inherit this class

        Returns:
            Class: Whatever the class child object may be, it is created and returned
        """
        entity = cls(**kwargs)
        db.session.add(entity)
        db.session.commit()
        
        return entity

    @classmethod
    def get(cls, id):
        """Get an object by id, from the table

        Returns:
            Class: Returns an instance of the model
        """
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_all(cls):
        """Get all rows from the table, as a list of objects

        Returns:
            Class: Returns a list of instances of the model
        """
        return cls.query.all()
    

    def update(self, **kwargs):
        """Update attributes from an instance (a row)

        Returns:
            Class: The object itself with the new values
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
            
        db.session.commit()
        
        return self

    @classmethod
    def delete(cls, id):
        """Remove an object by id, from the table

        Returns:
            Bool: Returns True if the operations has been successful, otherwise returns False
        """
        entity = cls.query.filter_by(id=id).first()
        
        if entity is not None:
            db.session.delete(entity)
            db.session.commit()
            
            return True
        
        return False