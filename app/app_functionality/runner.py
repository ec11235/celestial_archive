from classes.space_obj_classes.space_objects import *
from app.app_functionality.app import *
from classes.app_classes.catalog import Catalog
from classes.app_classes.library import Library


def initialize_public_library():
    lib = Library()
    
    # Create and add 10 stars
    star_catalog = Catalog()
    stars = [
        Star(name="Alpha Centauri", luminosity=0.9183, abs_magnitude=4.38, radius=1.22, temp=5790, host_galaxy="Milky Way", coordinates="14h 39m 36.49400s -60° 50′ 02.3737″", s_type="G2V"),
        Star(name="Betelgeuse", luminosity=126000, abs_magnitude=-5.85, radius=887, temp=3500, host_galaxy="Milky Way", coordinates="05h 55m 10.3053s +07° 24′ 25.426″", s_type="M2Iab"),
        Star(name="Sirius", luminosity=25.4, abs_magnitude=1.42, radius=1.711, temp=9940, host_galaxy="Milky Way", coordinates="06h 45m 08.9173s -16° 42′ 58.017″", s_type="A1V"),
        Star(name="Vega", luminosity=40.12, abs_magnitude=0.58, radius=2.362, temp=9602, host_galaxy="Milky Way", coordinates="18h 36m 56.3364s +38° 47′ 01.280″", s_type="A0V"),
        Star(name="Proxima Centauri", luminosity=0.0017, abs_magnitude=15.53, radius=0.1542, temp=3042, host_galaxy="Milky Way", coordinates="14h 29m 42.9487s -62° 40′ 46.163″", s_type="M5.5V"),
        Star(name="Rigel", luminosity=120000, abs_magnitude=-6.92, radius=78.9, temp=12130, host_galaxy="Milky Way", coordinates="05h 14m 32.27210s -08° 12′ 05.8981″", s_type="B8Iab"),
        Star(name="Polaris", luminosity=2500, abs_magnitude=-3.64, radius=50, temp=6015, host_galaxy="Milky Way", coordinates="02h 31m 49.09456s +89° 15′ 50.7923″", s_type="F7Ib"),
        Star(name="Arcturus", luminosity=170, abs_magnitude=-0.30, radius=25.4, temp=4286, host_galaxy="Milky Way", coordinates="14h 15m 39.6721s +19° 10′ 56.673″", s_type="K1.5III"),
        Star(name="Aldebaran", luminosity=518, abs_magnitude=-0.63, radius=44.2, temp=3910, host_galaxy="Milky Way", coordinates="04h 35m 55.23907s +16° 30′ 33.488″", s_type="K5III"),
        Star(name="Antares", luminosity=75000, abs_magnitude=-5.28, radius=680, temp=3200, host_galaxy="Milky Way", coordinates="16h 29m 24.45970s -26° 25′ 55.2094″", s_type="M1.5Iab")
    ]
    for star in stars:
        star_catalog.add_to_catalog(star)
    lib.add_to_library(star_catalog)

    # Create and add 10 planets
    planet_catalog = Catalog()
    planets = [
        Planet(name="Earth", size="large", habitability="excellent", star_system="Solar System", coordinates="1 AU", orbital_period=365.25),
        Planet(name="Mars", size="medium", habitability="poor", star_system="Solar System", coordinates="1.524 AU", orbital_period=687),
        Planet(name="Jupiter", size="giant", habitability="fatal", star_system="Solar System", coordinates="5.204 AU", orbital_period=4331),
        Planet(name="Saturn", size="giant", habitability="fatal", star_system="Solar System", coordinates="9.582 AU", orbital_period=10747),
        Planet(name="Venus", size="medium", habitability="poor", star_system="Solar System", coordinates="0.723 AU", orbital_period=225),
        Planet(name="Neptune", size="giant", habitability="fatal", star_system="Solar System", coordinates="30.07 AU", orbital_period=60190),
        Planet(name="Uranus", size="giant", habitability="fatal", star_system="Solar System", coordinates="19.218 AU", orbital_period=30688),
        Planet(name="Mercury", size="small", habitability="fatal", star_system="Solar System", coordinates="0.387 AU", orbital_period=88),
        Planet(name="Kepler-22b", size="super-earth", habitability="unknown", star_system="Kepler-22", coordinates="600 light-years", orbital_period=290),
        Planet(name="Proxima b", size="super-earth", habitability="unknown", star_system="Proxima Centauri", coordinates="4.24 light-years", orbital_period=11.2)
    ]
    for planet in planets:
        planet_catalog.add_to_catalog(planet)
    lib.add_to_library(planet_catalog)

    # Create and add 10 nebulas
    nebula_catalog = Catalog()
    nebulas = [
        Nebula(name="Orion Nebula", coordinates="05h 35m 17s -05° 23′ 28″"),
        Nebula(name="Eagle Nebula", coordinates="18h 18m 48s -13° 49′ 00″"),
        Nebula(name="Crab Nebula", coordinates="05h 34m 31s +22° 00′ 52″"),
        Nebula(name="Helix Nebula", coordinates="22h 29m 38s -20° 50′ 14″"),
        Nebula(name="Horsehead Nebula", coordinates="05h 40m 59s -02° 27′ 30″"),
        Nebula(name="Cat's Eye Nebula", coordinates="17h 58m 33.4s +66° 37′ 59″"),
        Nebula(name="Carina Nebula", coordinates="10h 45m 08s -59° 41′ 04″"),
        Nebula(name="Ring Nebula", coordinates="18h 53m 35.1s +33° 01′ 45″"),
        Nebula(name="Dumbbell Nebula", coordinates="19h 59m 36.3s +22° 43′ 16″"),
        Nebula(name="Lagoon Nebula", coordinates="18h 03m 37s -24° 23′ 12″")
    ]
    for nebula in nebulas:
        nebula_catalog.add_to_catalog(nebula)
    lib.add_to_library(nebula_catalog)

    # Create and add 10 galaxies
    galaxy_catalog = Catalog()
    galaxies = [
        Galaxy(name="Milky Way", size="large", coordinates="13h 00m 00s -49° 00′ 00″"),
        Galaxy(name="Andromeda", size="large", coordinates="00h 42m 44s +41° 16′ 09″"),
        Galaxy(name="Triangulum", size="medium", coordinates="01h 33m 51s +30° 39′ 36″"),
        Galaxy(name="Whirlpool", size="medium", coordinates="13h 29m 53s +47° 11′ 43″"),
        Galaxy(name="Sombrero", size="medium", coordinates="12h 39m 59s -11° 37′ 23″"),
        Galaxy(name="Pinwheel", size="large", coordinates="14h 03m 12s +54° 20′ 56″"),
        Galaxy(name="Tadpole", size="small", coordinates="16h 06m 03s +55° 25′ 33″"),
        Galaxy(name="Cigar", size="medium", coordinates="09h 55m 52s +69° 40′ 47″"),
        Galaxy(name="Black Eye", size="medium", coordinates="12h 56m 11s +21° 41′ 00″"),
        Galaxy(name="Hoag's Object", size="medium", coordinates="15h 17m 14s +21° 35′ 09″")
    ]
    for galaxy in galaxies:
        galaxy_catalog.add_to_catalog(galaxy)
    lib.add_to_library(galaxy_catalog)

    # Create and add 10 star clusters
    star_cluster_catalog = Catalog()
    star_clusters = [
        StarCluster(o_type="open", number_of_stars=1000, age=10, coordinates="06h 45m 09s +24° 00′ 55″"),
        StarCluster(o_type="globular", number_of_stars=100000, age=12, coordinates="17h 40m 42s -53° 40′ 40″"),
        StarCluster(o_type="open", number_of_stars=500, age=5, coordinates="20h 34m 12s +42° 21′ 00″"),
        StarCluster(o_type="globular", number_of_stars=200000, age=13, coordinates="16h 12m 36s -26° 31′ 30″"),
        StarCluster(o_type="open", number_of_stars=200, age=8, coordinates="23h 24m 50s -12° 57′ 21″"),
        StarCluster(o_type="globular", number_of_stars=150000, age=11, coordinates="02h 21m 29s +57° 00′ 40″"),
        StarCluster(o_type="open", number_of_stars=700, age=6, coordinates="05h 34m 32s +32° 00′ 18″"),
        StarCluster(o_type="globular", number_of_stars=250000, age=14, coordinates="13h 26m 45s -47° 29′ 24″"),
        StarCluster(o_type="open", number_of_stars=300, age=7, coordinates="12h 15m 24s +25° 25′ 48″"),
        StarCluster(o_type="globular", number_of_stars=120000, age=10, coordinates="18h 31m 18s -26° 24′ 25″")
    ]
    for star_cluster in star_clusters:
        star_cluster_catalog.add_to_catalog(star_cluster)
    lib.add_to_library(star_cluster_catalog)

    # Create and add 10 black holes
    black_hole_catalog = Catalog()
    black_holes = [
        BlackHole(name="Sagittarius A*", mass=4.1e6, event_horizon="13 million km", coordinates="17h 45m 40.04s -29° 00′ 28.1″", spin_rate=0.1),
        BlackHole(name="Cygnus X-1", mass=14.8, event_horizon="44 km", coordinates="19h 58m 21.68s +35° 12′ 05.8″", spin_rate=0.5),
        BlackHole(name="M87*", mass=6.5e9, event_horizon="19 billion km", coordinates="12h 30m 49.42338s +12° 23′ 28.0439″", spin_rate=0.9),
        BlackHole(name="GRO J1655-40", mass=5.4, event_horizon="16 km", coordinates="16h 54m 00.137s -39° 50′ 44.90″", spin_rate=0.7),
        BlackHole(name="V404 Cygni", mass=9, event_horizon="27 km", coordinates="20h 24m 03.83s +33° 52′ 01.9″", spin_rate=0.2),
        BlackHole(name="XTE J1650-500", mass=4, event_horizon="12 km", coordinates="16h 50m 55.606s -49° 57′ 45.70″", spin_rate=0.8),
        BlackHole(name="LMC X-1", mass=10.91, event_horizon="33 km", coordinates="05h 39m 38.9s -69° 44′ 36″", spin_rate=0.1),
        BlackHole(name="Swift J1753.5-0127", mass=5, event_horizon="15 km", coordinates="17h 53m 28s -01° 27′ 06″", spin_rate=0.6),
        BlackHole(name="GS 1354-64", mass=7.6, event_horizon="23 km", coordinates="13h 58m 09.6s -64° 44′ 02″", spin_rate=0.4),
        BlackHole(name="XTE J1118+480", mass=7.5, event_horizon="23 km", coordinates="11h 18m 10.8s +48° 02′ 12″", spin_rate=0.3)
    ]
    for black_hole in black_holes:
        black_hole_catalog.add_to_catalog(black_hole)
    lib.add_to_library(black_hole_catalog)

    # Create and add 10 satellites
    satellite_catalog = Catalog()
    satellites = [
        Satellite(name="Hubble Space Telescope", orbital_period=95.42, distance_from_earth="547 km", image="hubble.jpg"),
        Satellite(name="International Space Station", orbital_period=92.68, distance_from_earth="408 km", image="iss.jpg"),
        Satellite(name="Landsat 8", orbital_period=99.05, distance_from_earth="705 km", image="landsat8.jpg"),
        Satellite(name="Terra", orbital_period=98.88, distance_from_earth="705 km", image="terra.jpg"),
        Satellite(name="Aqua", orbital_period=98.44, distance_from_earth="705 km", image="aqua.jpg"),
        Satellite(name="Sentinel-2", orbital_period=98.57, distance_from_earth="786 km", image="sentinel2.jpg"),
        Satellite(name="GOES-16", orbital_period=1436.1, distance_from_earth="35786 km", image="goes16.jpg"),
        Satellite(name="Suomi NPP", orbital_period=101.41, distance_from_earth="824 km", image="suomi.jpg"),
        Satellite(name="Jason-3", orbital_period=112.4, distance_from_earth="1336 km", image="jason3.jpg"),
        Satellite(name="Gaofen-4", orbital_period=1436.1, distance_from_earth="35786 km", image="gaofen4.jpg")
    ]
    for satellite in satellites:
        satellite_catalog.add_to_catalog(satellite)
    lib.add_to_library(satellite_catalog)

    # Create and add 10 asteroids
    asteroid_catalog = Catalog()
    asteroids = [
        Asteroid(composition="rocky", size="10 km", orbital_path="Mars-Jupiter belt", image="asteroid1.jpg"),
        Asteroid(composition="metallic", size="5 km", orbital_path="Mars-Jupiter belt", image="asteroid2.jpg"),
        Asteroid(composition="rocky", size="15 km", orbital_path="Mars-Jupiter belt", image="asteroid3.jpg"),
        Asteroid(composition="carbonaceous", size="7 km", orbital_path="Mars-Jupiter belt", image="asteroid4.jpg"),
        Asteroid(composition="metallic", size="12 km", orbital_path="Mars-Jupiter belt", image="asteroid5.jpg"),
        Asteroid(composition="rocky", size="8 km", orbital_path="Mars-Jupiter belt", image="asteroid6.jpg"),
        Asteroid(composition="carbonaceous", size="3 km", orbital_path="Mars-Jupiter belt", image="asteroid7.jpg"),
        Asteroid(composition="metallic", size="6 km", orbital_path="Mars-Jupiter belt", image="asteroid8.jpg"),
        Asteroid(composition="rocky", size="4 km", orbital_path="Mars-Jupiter belt", image="asteroid9.jpg"),
        Asteroid(composition="carbonaceous", size="11 km", orbital_path="Mars-Jupiter belt", image="asteroid10.jpg")
    ]
    for asteroid in asteroids:
        asteroid_catalog.add_to_catalog(asteroid)
    lib.add_to_library(asteroid_catalog)

    # Create and add 10 comets
    comet_catalog = Catalog()
    comets = [
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="10 million km", tail_color="white", image="comet1.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="5 million km", tail_color="blue", image="comet2.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Kuiper Belt", tail_length="8 million km", tail_color="yellow", image="comet3.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="12 million km", tail_color="red", image="comet4.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Kuiper Belt", tail_length="7 million km", tail_color="green", image="comet5.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="15 million km", tail_color="blue", image="comet6.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Kuiper Belt", tail_length="9 million km", tail_color="white", image="comet7.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="6 million km", tail_color="yellow", image="comet8.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Kuiper Belt", tail_length="13 million km", tail_color="red", image="comet9.jpg"),
        Comet(nucleus_composition="ice", orbital_path="Oort Cloud", tail_length="11 million km", tail_color="green", image="comet10.jpg")
    ]
    for comet in comets:
        comet_catalog.add_to_catalog(comet)
    lib.add_to_library(comet_catalog)

    # Create and add 10 molecular clouds
    molecular_cloud_catalog = Catalog()
    molecular_clouds = [
        MolecularCloud(mass="10,000 solar masses", temp=10, chemical_composition="H2, CO, NH3", coordinates="20h 29m 24.5s +40° 10′ 36″", image="cloud1.jpg"),
        MolecularCloud(mass="15,000 solar masses", temp=12, chemical_composition="H2, CO, NH3", coordinates="15h 20m 43.5s -12° 30′ 36″", image="cloud2.jpg"),
        MolecularCloud(mass="20,000 solar masses", temp=8, chemical_composition="H2, CO, NH3", coordinates="12h 45m 32.5s +14° 30′ 36″", image="cloud3.jpg"),
        MolecularCloud(mass="25,000 solar masses", temp=15, chemical_composition="H2, CO, NH3", coordinates="17h 30m 44.5s -22° 30′ 36″", image="cloud4.jpg"),
        MolecularCloud(mass="30,000 solar masses", temp=9, chemical_composition="H2, CO, NH3", coordinates="22h 45m 24.5s +10° 30′ 36″", image="cloud5.jpg"),
        MolecularCloud(mass="12,000 solar masses", temp=11, chemical_composition="H2, CO, NH3", coordinates="10h 35m 24.5s -15° 30′ 36″", image="cloud6.jpg"),
        MolecularCloud(mass="18,000 solar masses", temp=13, chemical_composition="H2, CO, NH3", coordinates="08h 25m 24.5s +20° 30′ 36″", image="cloud7.jpg"),
        MolecularCloud(mass="22,000 solar masses", temp=7, chemical_composition="H2, CO, NH3", coordinates="05h 15m 24.5s -05° 30′ 36″", image="cloud8.jpg"),
        MolecularCloud(mass="28,000 solar masses", temp=10, chemical_composition="H2, CO, NH3", coordinates="02h 45m 24.5s +15° 30′ 36″", image="cloud9.jpg"),
        MolecularCloud(mass="35,000 solar masses", temp=6, chemical_composition="H2, CO, NH3", coordinates="01h 55m 24.5s -10° 30′ 36″", image="cloud10.jpg")
    ]
    for molecular_cloud in molecular_clouds:
        molecular_cloud_catalog.add_to_catalog(molecular_cloud)
    lib.add_to_library(molecular_cloud_catalog)
    lib.save_lib_to_pickle_pub()

    
initialize_public_library()
app = App()
app.run_app()

print("done")

