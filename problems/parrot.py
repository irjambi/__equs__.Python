''' Parrot class '''
class Parrot():
    '''
    Defines a Parrot class with a few properties such as squawk, is_alive and colour
    '''
    def __init__(self, squawk, colours='multi-colour', is_alive=True):
        self.parrot_squawk = squawk
        self.is_alive = is_alive
        self.colour = colours

    def __call__(self):
        return self.parrot_squawk

    def squawk(self):
        if self.is_alive:
            return self.parrot_squawk

        print("This is an ex parrot")
