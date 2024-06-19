class Star:
    def __init__(self, name=None, luminosity=None, abs_magnitude=None, radius=None, temp=None, o_type=None, host_galaxy=None, coordinates=None, s_type=None, image=None):
        self.o_type = "star"
        self.name = name
        self.luminosity = luminosity
        self.abs_magnitude = abs_magnitude
        self.radius = radius
        self.temp = temp
        self.host_galaxy = host_galaxy
        self.coordinates = coordinates
        self.image = image
        self.s_type = s_type 

class Planet:
    def __init__(self, name=None, size=None, habitability=None, star_system=None, coordinates=None, orbital_period=None, image=None):
        self.o_type = "planet"
        self.name = name
        self.size = size
        self.habitability = habitability
        self.star_system = star_system
        self.coordinates = coordinates
        self.orbital_period = orbital_period
        self.image = image

class Nebula:
    def __init__(self, name=None, o_type=None, coordinates=None, image=None):
        self.o_type = "nebula"
        self.name = name
        self.coordinates = coordinates
        self.image = image

class Galaxy:
    def __init__(self, name=None, o_type=None, size=None, coordinates=None, image=None):
        self.o_type = "galaxy"
        self.name = name
        self.size = size
        self.coordinates = coordinates
        self.image = image

class StarCluster:
    def __init__(self, o_type=None, number_of_stars=None, age=None, coordinates=None, image=None):
        self.o_type = "star_cluster"
        self.number_of_stars = number_of_stars
        self.age = age
        self.coordinates = coordinates
        self.image = image

class BlackHole:
    def __init__(self, name=None, o_type=None, mass=None, event_horizon=None, coordinates=None, spin_rate=None, image=None):
        self.o_type = "black_hole"
        self.name = name
        self.mass = mass
        self.event_horizon = event_horizon
        self.coordinates = coordinates
        self.spin_rate = spin_rate
        self.image = image

class Satellite:
    def __init__(self, name=None, o_type=None, orbital_period=None, distance_from_earth=None, image=None):
        self.o_type = "satallite"
        self.name = name
        self.orbital_period = orbital_period
        self.distance_from_earth = distance_from_earth
        self.image = image

class Asteroid:
    def __init__(self, composition=None, o_type=None, size=None, orbital_path=None, image=None):
        self.o_type ="asteroid"
        self.composition = composition       
        self.size = size
        self.orbital_path = orbital_path
        self.image = image

class Comet:
    def __init__(self, nucleus_composition=None, o_type=None, orbital_path=None, tail_length=None, tail_color=None, image=None):
        self.o_type = "comet"
        self.nucleus_composition = nucleus_composition       
        self.orbital_path = orbital_path
        self.tail_length = tail_length
        self.tail_color = tail_color
        self.image = image

class MolecularCloud:
    def __init__(self, mass=None, o_type=None, temp=None, chemical_composition=None, coordinates=None, image=None):
        self.o_type = "molecular_cloud"
        self.mass = mass
        self.temp = temp
        self.chemical_composition = chemical_composition
        self.coordinates = coordinates
        self.image = image

__all__ = [
    'Star', 'Planet', 'Nebula', 'Galaxy', 'StarCluster', 'BlackHole',
    'Satellite', 'Asteroid', 'Comet', 'MolecularCloud'
]   
