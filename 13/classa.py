

class Fabric:

    def create(self, tip):

        if tip == 'auto':

            class Auto:
                pass

            return Auto

        elif tip == 'fruit':

            class Fruit:
                pass

            return Fruit

        return None




class Garage:

    def get_car(self):

        class Auto:
            pass

        return Auto()