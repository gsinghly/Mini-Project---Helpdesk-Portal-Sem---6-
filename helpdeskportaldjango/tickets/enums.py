from tickets.utils import ChoiceEnum


class Urgency(ChoiceEnum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class Location(ChoiceEnum):
    ADMIN = 'Admin'
    HOSTEL = 'Hostel'
    HOSTELROOM = 'Hostel Room'
    LIBRARY = 'Library'
    LECTUREHALL1 = 'Lecture Hall 1'
    LECTUREHALL2 = 'Lecture Hall 2'
    PLAYGROUND = 'Playground'
    OTHER = 'Other'

class Category(ChoiceEnum):
    CONNECTIVITY = 'Connectivity'
    MEDICAL = 'Medical'
    PLUMBING = 'Plumbing'
    STRUCTURAL ='Structural'
    ELECTRICAL = 'Electrical'
    OTHER = 'Other'
