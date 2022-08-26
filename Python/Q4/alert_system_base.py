
class User:
    def __init__(self, name):
        self.name = name
        self.infected = False

    def __repr__(self):
        return '({0}, {1})'.format(self.name, str(self.infected))

    def got_virus(self):
        self.infected = True

    def got_healed(self):
        self.infected = False


class AlertSystemBase:

    def __init__(self):
        pass

    def add_person(self, person: User):
        """
        Adds a person to the system.
        :return: True if the person was successfully added,
                 False if they are already in the system
        """
        raise NotImplementedError('must be implemented by subclass')

    def remove_person(self, person: User):
        """
        Removes a person to the system.
        :return: True if a person is successfully removed,
                 False if they were not in the system
        """
        raise NotImplementedError('must be implemented by subclass')

    def add_contact(self, person1: User, person2: User):
        """
        Adds a contact between two people.
        :return: True if a contact is successfully added,
                 False otherwise
        """
        raise NotImplementedError('must be implemented by subclass')

    def count_contacts(self, person: User):
        """
        Counts how many contacts the person has.
        :return: the number of contacts the person has, or
                 -1 if the person is not in the system
        """
        raise NotImplementedError('must be implemented by subclass')

    def remove_contact(self, person1: User, person2: User):
        """
        Removes a contact between two people.
        :return: True if the contact was successfully removed,
                 False otherwise
        """
        raise NotImplementedError('must be implemented by subclass')

    def mark_infected(self, infected_person: User, virus_degree: int = 0):
        """
        Marks a person as infected.
        Based on the virus degree, marks infected:
                virus_degree = 1: the infected person's contacts,
                virus_degree = 2: the infected person's contacts and the contacts of the contacts,
                virus_degree = 3: the infected person's contacts, the contacts of the contacts, and
                                 the contacts of the contacts of the contacts,
                and so on.
        """
        raise NotImplementedError('must be implemented by subclass')

    def mark_healed(self, person: User):
        """
        Marks a person as healed.
        Only the given person is marked as healed, not their contacts.
        """
        person.got_healed()
