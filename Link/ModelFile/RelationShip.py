from ModelBase import Base

class RelationShip(Base):
    def __init__(self):
        self.OwnerId = 0
        self.CustomerId = 0
        self.RelationDes = ''
        self.Note = ''