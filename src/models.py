# Filename: models.py
# This contains Metadata Table Objects
# And Add to Table logic
########################################################################################################################
# 1 - Imports
from typing import Optional

from sqlalchemy import Column, Integer, String, Date, Float, and_
from sqlalchemy import create_engine, select, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


########################################################################################################################
# 2 - Connection to mysql and create base

# 2.1 - Connection String
conn_str = 'mysql+pymysql://Heather:#LAwaItly19@localhost:3306/wsl'

# 2.2 - SQLAlchemy engine that will interact with mysql database
engine = create_engine(conn_str, echo=True)

# 2.3 - SQLAlchemy ORM session that binds to the engine
Session = sessionmaker(bind=engine)

# 2.4 - Base MetaData Object
Base = declarative_base()

########################################################################################################################
# 3.0 - MetaData Table Object


# wsl.continent
class Continent(Base):
    __tablename__ = 'continent'
    continent_id = Column(Integer, primary_key=True)
    continent = Column(String(length=20), unique=True)
    countries = relationship("Country")

    def __repr__(self):
        return f"Continent(id={self.continent_id!r}, " \
               f"name={self.continent!r})"

    # For direct querying
    session = Session()

# wsl.country
class Country(Base):
    __tablename__ = 'country'
    country_id = Column(Integer, primary_key=True)
    country = Column(String(length=50))
    continent_id = Column(Integer, ForeignKey('continent.continent_id'), nullable=False)
    regions = relationship("Region")
    surfers = relationship("Surfers")

    def __repr__(self):
        return f"Country(id={self.country_id!r}, " \
               f"continent_id={self.continent_id!r}, " \
               f"name={self.country!r})"


# wsl.region
class Region(Base):
    __tablename__ = 'region'
    region_id = Column(Integer, primary_key=True)
    region = Column(String(length=50))
    country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    cities = relationship("City")
    break_names = relationship("Break")

    def __repr__(self):
        return f"Region(id={self.region_id!r}, " \
               f"country_id={self.country_id!r}, " \
               f"name={self.region!r}"


# wsl.city
class City(Base):
    __tablename__ = 'city'
    city_id = Column(Integer, primary_key=True)
    city = Column(String(length=50))
    region_id = Column(Integer, ForeignKey('region.region_id'), nullable=False)
    surfers = relationship("Surfers")

    def __repr__(self):
        return f"City(city_id={self.city_id!r}, " \
               f"region_id={self.region_id!r}, " \
               f"name={self.city!r}"


# wsl.break
class Break(Base):
    __tablename__ = 'break'
    break_id = Column(Integer, primary_key=True)
    break_name = Column(String(50))
    region_id = Column(Integer, ForeignKey('region.region_id'), nullable=False)
    break_type = Column(String(length=32))
    reliability = Column(String(length=32))
    ability = Column(String(length=32))
    shoulder_burn = Column(String(length=32))
    clean = Column(Float)
    blown_out = Column(Float)
    too_small = Column(Float)
    events = relationship("Event")

    def __repr__(self):
        return f"Break(break_id={self.break_id!r}, " \
               f"break_name={self.break_name!r}, " \
               f"region_id={self.region_id!r} ", \
               f"break_type={self.break_type!r}, " \
               f"reliability={self.reliability!r}, " \
               f"ability={self.ability!r}, " \
               f"shoulder_burn={self.shoulder_burn!r}, " \
               f"clean={self.clean!r}, " \
               f"blown_out={self.blown_out!r}, " \
               f"too_small={self.too_small!r}, " \



# wsl.surfers
class Surfers(Base):
    __tablename__ = 'surfers'
    surfer_id = Column(Integer, primary_key=True)
    gender = Column(String(length=6), nullable=False)
    first_name = Column(String(length=50), nullable=False)
    last_name = Column(String(length=50), nullable=False)
    full_name = Column(String(length=100), nullable=False)
    stance = Column(String(length=10))
    rep_country_id = Column(Integer, ForeignKey('country.country_id'), nullable=False)
    birthday = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    first_season = Column(Integer)
    first_tour = Column(String(length=50))
    home_city_id = Column(Integer, ForeignKey('city.city_id'), nullable=False)
    heat_surfers = relationship("HeatSurfers")

    def __repr__(self):
        return f"surfer_id={self.surfer_id!r}, " \
               f"gender={self.gender!r}, " \
               f"first_name={self.first_name!r}, " \
               f"last_name={self.last_name!r}, " \
               f"full_name={self.full_name!r}, " \
               f"stance={self.stance!r}, " \
               f"rep_country_id={self.rep_country_id!r}, " \
               f"birthday={self.birthday!r}, " \
               f"height={self.height!r}, " \
               f"weight={self.weight!r}, " \
               f"first_season={self.first_season!r}, " \
               f"first_tour={self.first_tour!r}, " \
               f"home_city_id={self.home_city_id!r}"


# wsl.tour
class Tour(Base):
    __tablename__ = 'tour'
    tour_id = Column(Integer, primary_key=True)
    year = Column(Integer)
    gender = Column(String(length=6))
    tour_type = Column(String(length=50), nullable=False)
    tour_name = Column(String(length=50), nullable=False)
    events = relationship("Event")

    def __repr__(self):
        return f"tour_id={self.tour_id!r}, " \
               f"year={self.year!r}, " \
               f"gender={self.gender!r}, " \
               f"tour_type={self.tour_type!r}, " \
               f"tour_name={self.tour_name!r}"


# wsl.event
class Event(Base):
    __tablename__ = 'event'
    event_id = Column(Integer, primary_key=True)
    event_name = Column(String(length=50), nullable=False)
    tour_id = Column(Integer, ForeignKey('tour.tour_id'), nullable=False)
    stop_nbr = Column(Integer)
    break_id = Column(Integer, ForeignKey('break.break_id'), nullable=False)
    open_date = Column(Date)
    close_date = Column(Date)
    heat_details = relationship("HeatDetails")

    def __repr__(self):
        return f"event_id={self.event_id!r}, " \
               f"event_name={self.event_name!r}, " \
               f"tour_id={self.tour_id!r}, " \
               f"stop_nbr={self.stop_nbr!r}, " \
               f"break_id={self.break_id!r}, " \
               f"open_date={self.open_date!r}, " \
               f"close_date={self.close_date!r}"


# wsl.round
class Round(Base):
    __tablename__ = 'round'
    round_id = Column(Integer, primary_key=True)
    round = Column(String(length=32), nullable=False)
    heat_details = relationship("HeatDetails")

    def __repr__(self):
        return f"round_id={self.round_id!r}, " \
               f"round={self.even!r}"


# wsl.heat_details
class HeatDetails(Base):
    __tablename__ = 'heat_details'
    heat_id = Column(Integer, primary_key=True)
    heat_nbr = Column(String(length=10), nullable=False)
    event_id = Column(Integer, ForeignKey('event.event_id'), nullable=False)
    round_id = Column(Integer, ForeignKey('round.round_id'), nullable=False)
    wind = Column(String(length=32))
    heat_date = Column(Date)
    duration = Column(Integer)
    wave_min = Column(Integer)
    wave_max = Column(Integer)
    heat_surfers = relationship("HeatSurfers")
    heat_results = relationship("HeatResults")

    def repr__(self):
        return f"heat_id={self.heat_id!r}, " \
               f"heat_nbr={self.heat_nbr}, " \
               f"event_id={self.event_id!r}, " \
               f"round_id={self.round_id!r}, " \
               f"wind={self.wind!r}, " \
               f"heat_date={self.heat_date!r}, " \
               f"duration={self.duration!r}, " \
               f"wave_min={self.wave_min!r}, " \
               f"wave_max={self.wave_max!r}"


# wsl.heat_surfers
class HeatSurfers(Base):
    __tablename__ = 'heat_surfers'
    surfer_heat_id = Column(Integer, primary_key=True)
    heat_id = Column(Integer, ForeignKey('heat_details.heat_id'), nullable=False)
    surfer_id = Column(Integer, ForeignKey('surfers.surfer_id'), nullable=False)
    surfer_results = relationship("HeatResults")

    def __repr__(self):
        return f"surfer_heat_id={self.surfer_heat_id!r}, " \
               f"heat_id={self.heat_id!r}, " \
               f"surfer_id={self.surfer_id!r}"


# wsl.heat_results
class HeatResults(Base):
    __tablename__ = 'heat_results'
    heat_result_id = Column(Integer, primary_key=True)
    heat_id = Column(Integer, ForeignKey('heat_details.heat_id'), nullable=False)
    surfer_in_heat_id = Column(Integer, ForeignKey('heat_surfers.surfer_heat_id'), nullable=False)
    pick_to_win_percent = Column(Float)
    jersey_color = Column(String(length=32))
    status = Column(String(length=12))
    wave_1 = Column(Float)
    wave_2 = Column(Float)
    wave_3 = Column(Float)
    wave_4 = Column(Float)
    wave_5 = Column(Float)
    wave_6 = Column(Float)
    wave_7 = Column(Float)
    wave_8 = Column(Float)
    wave_9 = Column(Float)
    wave_10 = Column(Float)
    wave_11 = Column(Float)
    wave_12 = Column(Float)
    wave_13 = Column(Float)
    wave_14 = Column(Float)
    wave_15 = Column(Float)

    def __repr__(self):
        return f"heat_result_id={self.heat_result_id!r}, " \
               f"heat_id={self.heat_id!r}, " \
               f"surfer_in_heat_id={self.surfer_in_heat_id!r}, " \
               f"pick_to_win_percent={self.pick_to_win_percent!r}, " \
               f"jersey_color={self.jersey_color!r}, " \
               f"status={self.status!r}, " \
               f"wave_1={self.wave_1!r}, " \
               f"wave_2={self.wave_2!r}, " \
               f"wave_3={self.wave_3!r}, " \
               f"wave_4={self.wave_4!r}, " \
               f"wave_5={self.wave_5!r}, " \
               f"wave_6={self.wave_6!r}, " \
               f"wave_7={self.wave_7!r}, " \
               f"wave_8={self.wave_8!r}, " \
               f"wave_9={self.wave_9!r}, " \
               f"wave_10={self.wave_10!r}, " \
               f"wave_11={self.wave_11!r}, " \
               f"wave_12={self.wave_12!r}, " \
               f"wave_13={self.wave_13!r}, " \
               f"wave_14={self.wave_14!r}, " \
               f"wave_15={self.wave_15!r}"


#######################################################################################################################
# 4.0 - Table Manipulation

# Check to see if fields were entered and add to mysql tables
class AddLocation:
    def __init__(self,
                 entered_continent: Optional[str] = None,
                 entered_country: Optional[str] = None,
                 entered_region: Optional[str] = None,
                 entered_city: Optional[str] = None,
                 entered_break_name: Optional[str] = None,
                 entered_break_type: Optional[str] = None,
                 entered_reliability: Optional[str] = None,
                 entered_ability: Optional[str] = None,
                 entered_shoulder_burn: Optional[str] = None,
                 entered_clean: Optional[float] = 0,
                 entered_blown_out: Optional[float] = 0,
                 entered_too_small: Optional[float] = 0) -> object:

        self.entered_continent: Optional[str] = entered_continent
        self.entered_country: Optional[str] = entered_country
        self.entered_region: Optional[str] = entered_region
        self.entered_city: Optional[str] = entered_city
        self.entered_break_name: Optional[str] = entered_break_name
        self.entered_break_type: Optional[str] = entered_break_type
        self.entered_reliability: Optional[str] = entered_reliability
        self.entered_ability: Optional[str] = entered_ability
        self.entered_shoulder_burn: Optional[str] = entered_shoulder_burn
        self.entered_clean: Optional[float] = entered_clean
        self.entered_blown_out: Optional[float] = entered_blown_out
        self.entered_too_small: Optional[float] = entered_too_small

    div_dict = {'input_error': ['Input Error', '=', 60],
                'wipe_out_wav': ['Wipe Out', '~', 60]}

    def was_continent_entered(self):
        if self.entered_continent is None or self.entered_continent == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nContinent cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What continent are you on?" 
                              f"\nEntered Continent: {self.entered_continent}")
            raise ValueError(no_entry_error)

    def was_country_entered(self):
        session = Session()

        # Check to see if a country was entered
        if self.entered_country is None or self.entered_country == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nCountry cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What country are you in??" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}")
            raise ValueError(no_entry_error)

    def was_region_entered(self):
        session = Session()

        # Check to see if a region was entered
        if self.entered_region is None or self.entered_region == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nRegion cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What region are you in??" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}"
                              f"\nEntered Region: {self.entered_region}")
            raise ValueError(no_entry_error)

    def was_city_entered(self):
        session = Session()

        # Check to see if a city was entered
        if self.entered_city is None or self.entered_city == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nCity cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What city are you in??" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}"
                              f"\nEntered Region: {self.entered_region}"
                              f"\nEntered City: {self.entered_city}")
            raise ValueError(no_entry_error)

    def was_break_name_entered(self):
        session = Session()

        # Check to see if a break name was entered
        if self.entered_break_name is None or self.entered_break_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nBreak Name cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What break are you at?" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}"
                              f"\nEntered Region: {self.entered_region}"
                              f"\nEntered Break Name: {self.entered_break_name}")
            raise ValueError(no_entry_error)

    def add_new_country(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a country was entered does it already exist on the entered continent?
        query = (select(Country.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                             Continent.continent == self.entered_continent,
                             Country.country == self.entered_country
                             )))
        result = session.execute(query)
        check_country = result.scalar()

        # Did the query return a country? If so it has already been added to wsl.country
        if check_country is not None:
            print(f"\nThe country, {self.entered_country} "
                  f"has already been discovered on {self.entered_continent}.\n")
            # return
        else:
            # Add New Country to wsl.country

            # Get continent_id from continent table
            query = (select(Continent.continent_id)
                     .where(Continent.continent == self.entered_continent))
            result = session.execute(query)
            entered_continent_id = result.scalar()

            # Create an instance of the Country class to add to wsl.country
            new_country = Country(continent_id=entered_continent_id,
                                  country=self.entered_country)

            # Add the new country.
            session.add(new_country)
            session.flush()
            session.commit()

    def add_new_region(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country

        # Was a region entered?
        self.was_region_entered()

        # Does the entered region exist in the entered country on the entered continent?
        query = (select(Region.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                              Continent.continent == self.entered_continent,
                              Country.country == self.entered_country,
                              Region.region == self.entered_region
                            )))

        result = session.execute(query)
        check_region = result.scalar()

        # Did the query return a region? If so it has already been added to wsl.region.
        if check_region is not None:
            print(f"\nThe region, {self.entered_region} in the country, {self.entered_country} "
                  f"on the continent, {self.entered_country} has already been discovered.\n")
            return
        else:
            # Get country_id from continent table
            # We need to run this query again incase a new country was added when checking the entered country
            query = (select(Country.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                  Continent.continent == self.entered_continent,
                                  Country.country == self.entered_country
                                )))

            result = session.execute(query)
            entered_country_id = result.scalar()\

            # Create an instance of the Region class to add the new region to wsl.region.
            new_region = Region(country_id=entered_country_id,
                                region=self.entered_region)

            # Add the new region
            session.add(new_region)
            session.flush()
            session.commit()

    def add_new_city(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country

        # Was a region entered?
        self.was_region_entered()

        # If a valid region was entered and does not already exist add it to wsl.region
        self.add_new_region()

        # Was a city entered?
        self.was_city_entered()

        # Does the entered city exist in the entered region, country, and continent?
        query = (select(City.city_id)
                 .join(Region, Region.region_id == City.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                  Continent.continent == self.entered_continent,
                  Country.country == self.entered_country,
                  Region.region == self.entered_region,
                  City.city == self.entered_city
                 )))

        result = session.execute(query)
        check_city = result.scalar()

        # Did the query return a city? If so it has already been added to wsl.city
        if check_city is not None:
            print(f"{self.entered_city}, {self.entered_region}, {self.entered_country} "
                  f"on the continent of {self.entered_continent} has already been discovered.")
            return
        else:
            # Get region_id from continent table
            query = (select(Region.region_id)
                     .join(Country, Country.country_id == Region.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                                 Region.region == self.entered_region,
                                 Country.country == self.entered_country,
                                 Continent.continent == self.entered_continent
                                 )))
            result = session.execute(query)
            entered_region_id = result.scalar()

            new_city = City(region_id=entered_region_id,
                            city=self.entered_city)

            session.add(new_city)
            session.flush()
            session.commit()

    def add_new_break(self):
        session = Session()

        # Was a continent entered?
        self.was_continent_entered()

        # Was a country entered?
        self.was_country_entered()

        # If a valid country was entered and does not already exist add it to wsl.country
        self.add_new_country

        # Was a region entered?
        self.was_region_entered()

        # If a valid region was entered and does not already exist add it to wsl.region
        self.add_new_region()

        # Was a city entered?
        self.was_break_name_entered()

        # Does the entered break exist in the entered region, country, and continent?
        query = (select(Break.break_id)
                 .join(Region, Region.region_id == Break.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                              Continent.continent == self.entered_continent,
                              Country.country == self.entered_country,
                              Region.region == self.entered_region,
                              Break.break_name == self.entered_break_name
                            )))

        result = session.execute(query)
        check_break = result.scalar()

        # Did the query return a break? If so it has already been added to wsl.break
        if check_break is not None:
            print(f"The wave at {self.entered_break_name} in "
                  f"{self.entered_region}, {self.entered_country} "
                  f"on the continent of {self.entered_continent} has already been discovered.")
            return
        else:
            # Get region_id from continent table
            query = (select(Region.region_id)
                     .join(Country, Country.country_id == Region.country_id)
                     .join(Continent, Continent.continent_id == Country.continent_id)
                     .where(and_(
                      Region.region == self.entered_region,
                      Country.country == self.entered_country,
                      Continent.continent == self.entered_continent
                     )))
            result = session.execute(query)
            entered_region_id = result.scalar()

            new_break = Break(break_name=self.entered_break_name,
                              region_id=entered_region_id,
                              break_type=self.entered_break_type,
                              reliability=self.entered_reliability,
                              ability=self.entered_ability,
                              shoulder_burn=self.entered_shoulder_burn,
                              clean=self.entered_clean,
                              blown_out=self.entered_blown_out,
                              too_small=self.entered_too_small)

            session.add(new_break)
            session.flush()
            session.commit()


class AddSurfer:
    def __init__(self,
                 entered_gender: str = None,
                 entered_first_name: str = None,
                 entered_last_name: str = None,
                 entered_stance: Optional[str] = None,
                 entered_rep_continent: Optional[str] = None,
                 entered_rep_country: str = None,
                 entered_birthday: Optional = None,
                 entered_height: Optional[int] = None,
                 entered_weight: Optional[int] = None,
                 entered_first_season: Optional[int] = None,
                 entered_first_tour: Optional[str] = None,
                 entered_home_continent: Optional[str] = None,
                 entered_home_country: Optional[str] = None,
                 entered_home_region: Optional[str] = None,
                 entered_home_city: Optional[str] = None,
                 entered_home_city_id: Optional[str] = None
                 ):

        self.entered_gender: str = entered_gender
        self.entered_first_name: str = entered_first_name
        self.entered_last_name: str = entered_last_name
        self.entered_stance: Optional[str] = entered_stance
        self.entered_rep_continent: Optional[str] = entered_rep_continent
        self.entered_rep_country: str = entered_rep_country
        self.entered_birthday: Optional = entered_birthday
        self.entered_height: Optional[int] = entered_height
        self.entered_weight: Optional[int] = entered_weight
        self.entered_first_season: Optional[int] = entered_first_season
        self.entered_first_tour: Optional[str] = entered_first_tour
        self.entered_home_continent: Optional[str] = entered_home_continent
        self.entered_home_country: Optional[str] = entered_home_country
        self.entered_home_region: Optional[str] = entered_home_region
        self.entered_home_city: Optional[str] = entered_home_city
        self.entered_home_city_id: Optional[str] = entered_home_city_id

    div_dict = {'input_error': ['Input Error', '=', 60],
                'wipe_out_wav': ['Wipe Out', '~', 60]}

    def was_gender_entered(self):
        if self.entered_gender not in ['Men', 'Women']:
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nThe surfer's gender must be 'Men' or 'Women' because of biology and shit."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Gender: {self.entered_gender}")
            raise ValueError(no_entry_error)

    def was_first_name_entered(self):
        if self.entered_first_name is None or self.entered_first_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nFirst Name cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered First Name: {self.entered_first_name}"
                              f"\nEntered Last Name: {self.entered_last_name}")
            raise ValueError(no_entry_error)

    def was_last_name_entered(self):
        if self.entered_last_name is None or self.entered_last_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nLast Name cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered First Name: {self.entered_first_name}"
                              f"\nEntered Last Name: {self.entered_last_name}")
            raise ValueError(no_entry_error)

    def was_rep_continent_entered(self):

        # Was a rep continent entered?
        if self.entered_rep_continent is None or self.entered_rep_continent == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nRepresentative Continent cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What continent are you on?"
                              f"\nEntered Rep Continent: {self.entered_rep_continent}"
                              f"\nEntered Rep Country: {self.entered_rep_country}")
            raise ValueError(no_entry_error)

    def was_rep_country_entered(self):

        # Was a rep country entered?
        if self.entered_rep_country is None or self.entered_rep_country == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nRepresentative Country cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What country are you in??"
                              f"\nEntered Rep Continent: {self.entered_rep_continent}"
                              f"\nEntered Rep Country: {self.entered_rep_country}")
            raise ValueError(no_entry_error)

    def add_new_surfer(self):
        session = Session()

        # Was gender, first name, and last name entered?
        self.was_gender_entered()
        self.was_first_name_entered()
        self.was_last_name_entered()

        # Was a representative continent and country entered?
        self.was_rep_continent_entered()
        self.was_rep_country_entered()

        # If a home city is entered make sure region, country, and continent was entered too
        if self.entered_home_city is not None or self.entered_home_city != '':
            home_city = True
            was_home_loc_entered = AddLocation(entered_continent=self.entered_home_continent,
                                               entered_country=self.entered_home_country,
                                               entered_region=self.entered_home_region,
                                               entered_city=self.entered_home_city)
            was_home_loc_entered.was_continent_entered()

            # If location data was entered get home city id
            query = (select(City.city_id)
                                    .join(Region, Region.region_id == City.region_id)
                                    .join(Country, Country.country_id == Region.country_id)
                                    .join(Continent, Continent.continent_id == Country.continent_id)
                                    .where(and_(
                                                Continent.continent == self.entered_home_continent,
                                                Country.country == self.entered_home_country,
                                                Region.region == self.entered_home_region,
                                                City.city == self.entered_home_city
                                                )))
            result = session.execute(query)
            check_home_city = result.scalar()

            if check_home_city is None:
                city_inst = AddLocation(entered_continent=self.entered_home_continent,
                                        entered_country=self.entered_home_country,
                                        entered_region=self.entered_home_region,
                                        entered_city=self.entered_home_city)
                city_inst.add_new_city()

        # Check to see if the entered_surfer exists
        query = (select(Surfers.surfer_id)
                 .join(Country, Country.country_id == Surfers.rep_country_id)
                 .where(and_(
                             Surfers.gender == self.entered_gender,
                             Surfers.first_name == self.entered_first_name,
                             Surfers.last_name == self.entered_last_name,
                             Country.country == self.entered_rep_country
                            )))
        result = session.execute(query)
        check_surfer = result.scalar()

        if check_surfer is not None:
            print(f"{self.entered_first_name} {self.entered_last_name} "
                  f"of {self.entered_rep_country} has already been added.")
            return

        # Get country_id from the country table for rep  country
        query = (select(Country.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                            Continent.continent == self.entered_rep_continent,
                            Country.country == self.entered_rep_country
                            )))
        result = session.execute(query)
        entered_rep_country_id = result.scalar()

        # Get home city id
        query = (select(City.city_id)
                 .join(Region, Region.region_id == City.region_id)
                 .join(Country, Country.country_id == Region.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                             Continent.continent == self.entered_home_continent,
                             Country.country == self.entered_home_country,
                             Region.region == self.entered_home_region,
                             City.city == self.entered_home_city
                            )))
        result = session.execute(query)
        entered_home_city_id = result.scalar()

        # Get full name
        entered_full_name = f"{self.entered_first_name} {self.entered_last_name}"

        new_surfer = Surfers(gender=self.entered_gender,
                             first_name=self.entered_first_name,
                             last_name=self.entered_last_name,
                             full_name=entered_full_name,
                             stance=self.entered_stance,
                             rep_country_id=entered_rep_country_id,
                             birthday=self.entered_birthday,
                             height=self.entered_height,
                             weight=self.entered_weight,
                             first_season=self.entered_first_season,
                             first_tour=self.entered_first_tour,
                             home_city_id=entered_home_city_id)

        session.add(new_surfer)
        session.flush()
        session.commit()


class AddTour:
    def __init__(self,
                 entered_year: Optional[int] = None,
                 entered_gender: Optional[str] = None,
                 entered_tour_type: Optional[str] = None,
                 entered_tour_name: Optional[str] = None,
                 entered_event_name: Optional[str] = None,
                 entered_stop_nbr: Optional[int] = None,
                 entered_continent: Optional[str] = None,
                 entered_country: Optional[str] = None,
                 entered_region: Optional[str] = None,
                 entered_break_name: Optional[str] = None,
                 entered_open_date: Optional = None,
                 entered_close_date: Optional = None,
                 entered_round: Optional[str] = None,
                 entered_heat_nbr: Optional[str] = None,
                 entered_wind: Optional[str] = None,
                 entered_heat_date: Optional = None,
                 entered_duration: Optional[int] = None,
                 entered_wave_min: Optional[int] = None,
                 entered_wave_max: Optional[int] = None,
                 entered_surfer: Optional[str] = None,
                 entered_pick_to_win_percent: Optional[float] = None,
                 entered_jersey_color: Optional[str] = None,
                 entered_status: Optional[str] = None,
                 entered_wave_1: Optional[float] = None,
                 entered_wave_2: Optional[float] = None,
                 entered_wave_3: Optional[float] = None,
                 entered_wave_4: Optional[float] = None,
                 entered_wave_5: Optional[float] = None,
                 entered_wave_6: Optional[float] = None,
                 entered_wave_7: Optional[float] = None,
                 entered_wave_8: Optional[float] = None,
                 entered_wave_9: Optional[float] = None,
                 entered_wave_10: Optional[float] = None,
                 entered_wave_11: Optional[float] = None,
                 entered_wave_12: Optional[float] = None,
                 entered_wave_13: Optional[float] = None,
                 entered_wave_14: Optional[float] = None,
                 entered_wave_15: Optional[float] = None):

        self.entered_year: Optional[int] = entered_year
        self.entered_gender: Optional[str] = entered_gender
        self.entered_tour_type: Optional[str] = entered_tour_type
        self.entered_tour_name: Optional[str] = entered_tour_name
        self.entered_event_name: Optional[str] = entered_event_name
        self.entered_stop_nbr: Optional[int] = entered_stop_nbr
        self.entered_continent: Optional[int] = entered_continent
        self.entered_country: Optional[str] = entered_country
        self.entered_region: Optional[str] = entered_region
        self.entered_break_name: Optional[str] = entered_break_name
        self.entered_open_date: Optional = entered_open_date
        self.entered_close_date: Optional = entered_close_date
        self.entered_round: Optional[str] = entered_round
        self.entered_heat_nbr: Optional[str] = entered_heat_nbr
        self.entered_wind: Optional[str] = entered_wind
        self.entered_heat_date: Optional = entered_heat_date
        self.entered_duration: Optional[int] = entered_duration
        self.entered_wave_min: Optional[int] = entered_wave_min
        self.entered_wave_max: Optional[int] = entered_wave_max
        self.entered_surfer: Optional[str] = entered_surfer
        self.entered_pick_to_win_percent: Optional[float] = entered_pick_to_win_percent
        self.entered_jersey_color: Optional[str] = entered_jersey_color
        self.entered_status: Optional[str] = entered_status
        self.entered_wave_1: Optional[float] = entered_wave_1
        self.entered_wave_2: Optional[float] = entered_wave_2
        self.entered_wave_3: Optional[float] = entered_wave_3
        self.entered_wave_4: Optional[float] = entered_wave_4
        self.entered_wave_5: Optional[float] = entered_wave_5
        self.entered_wave_6: Optional[float] = entered_wave_6
        self.entered_wave_7: Optional[float] = entered_wave_7
        self.entered_wave_8: Optional[float] = entered_wave_8
        self.entered_wave_9: Optional[float] = entered_wave_9
        self.entered_wave_10: Optional[float] = entered_wave_10
        self.entered_wave_11: Optional[float] = entered_wave_11
        self.entered_wave_12: Optional[float] = entered_wave_12
        self.entered_wave_13: Optional[float] = entered_wave_13
        self.entered_wave_14: Optional[float] = entered_wave_14
        self.entered_wave_15: Optional[float] = entered_wave_15

    div_dict = {'input_error': ['Input Error', '=', 60],
                'wipe_out_wav': ['Wipe Out', '~', 60]}

    def was_year_entered(self):
        if self.entered_year is None or self.entered_year == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nYear cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost in space-time. What year are you in?"
                              f"\nEntered Year: {self.entered_year}")
            raise ValueError(no_entry_error)

    def was_gender_entered(self):
        if self.entered_gender not in ['Men', 'Women']:
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nThe surfer's gender must be 'Men' or 'Women' because of biology and shit."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Gender: {self.entered_gender}")
            raise ValueError(no_entry_error)

    def was_tour_type_entered(self):
        if self.entered_tour_type is None or self.entered_tour_type == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWhat type of tour is this?"
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Year: {self.entered_year}"
                              f"\nEntered Gender: {self.entered_gender}"
                              f"\nEntered Tour Type: {self.entered_tour_type}")
            raise ValueError(no_entry_error)

    def was_tour_name_entered(self):
        if self.entered_tour_name is None or self.entered_tour_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWhat is the name of this tour?"
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour Name: {self.entered_tour_name}")
            raise ValueError(no_entry_error)

    def was_event_name_entered(self):
        if self.entered_event_name is None or self.entered_event_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWhat is the name of this event?"
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour Name: {self.entered_tour_name}"
                              f"\nEntered Event Name: {self.entered_event_name}")
            raise ValueError(no_entry_error)

    def was_round_entered(self):
        if self.entered_round is None or self.entered_round == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWhat round is this?"
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour Name: {self.entered_tour_name}"
                              f"\nEntered Event Name: {self.entered_event_name}"
                              f"\nEntered Round: {self.entered_round}")
            raise ValueError(no_entry_error)

    def was_heat_nbr_entered(self):
        if self.entered_heat_nbr is None or self.entered_heat_nbr == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWhat heat number is this?"
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour Name: {self.entered_tour_name}"
                              f"\nEntered Event Name: {self.entered_event_name}"
                              f"\nEntered Round: {self.entered_round}"
                              f"\nEntered Heat: {self.entered_heat_nbr}")
            raise ValueError(no_entry_error)

    def was_continent_entered(self):
        if self.entered_continent is None or self.entered_continent == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nContinent cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What continent are you on?" 
                              f"\nEntered Continent: {self.entered_continent}")
            raise ValueError(no_entry_error)

    def was_country_entered(self):
        # Check to see if a country was entered
        if self.entered_country is None or self.entered_country == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nCountry cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What country are you in??" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}")
            raise ValueError(no_entry_error)

    def was_region_entered(self):
        # Check to see if a region was entered
        if self.entered_region is None or self.entered_region == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nRegion cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What region are you in??" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}"
                              f"\nEntered Region: {self.entered_region}")
            raise ValueError(no_entry_error)

    def was_break_name_entered(self):
        # Check to see if a break name was entered
        if self.entered_break_name is None or self.entered_break_name == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}" 
                              f"\nBreak Name cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nYou seem a little lost. What break are you at?" 
                              f"\nEntered Continent: {self.entered_continent}"
                              f"\nEntered Country: {self.entered_country}"
                              f"\nEntered Region: {self.entered_region}"
                              f"\nEntered Break Name: {self.entered_break_name}")
            raise ValueError(no_entry_error)

    def was_surfer_entered(self):
        # Check to see if a surfer was entered
        if self.entered_surfer is None or self.entered_surfer == '':
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nSurfer cannot be None or an empty string."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour: {self.entered_tour_name}"
                              f"\nEntered Event: {self.entered_event_name}"
                              f"\nEntered Round: {self.entered_round}"
                              f"\nEntered Heat Number: {self.entered_heat_nbr}"
                              f"\nEntered Surfer: {self.entered_surfer}")
            raise ValueError(no_entry_error)

    def add_new_tour(self):
        session = Session()

        # Was the tour year entered?
        self.was_year_entered()

        # Was the tour gender entered?
        self.was_gender_entered()

        # Was the tour type entered?
        self.was_tour_type_entered()

        # Check to see if the tour already exists
        query = (select(Tour.tour_id)
                 .where(and_(
                             Tour.year == self.entered_year,
                             Tour.gender == self.entered_gender,
                             Tour.tour_type == self.entered_tour_type
                            )))

        result = session.execute(query)
        check_tour = result.scalar()

        # Does the entered_country exist in the entered_continent
        if check_tour is not None:
            print(f"The {self.entered_year} {self.entered_gender}s {self.entered_tour_type} has already been added.")
            return

        entered_tour_name = f"{self.entered_year} {self.entered_gender}s {self.entered_tour_type}"

        new_tour = Tour(year=self.entered_year,
                        gender=self.entered_gender,
                        tour_type=self.entered_tour_type,
                        tour_name=entered_tour_name)

        session.add(new_tour)
        session.flush()
        session.commit()

    def add_new_event(self):
        session = Session()

        # Was the tour and event entered?
        self.was_tour_name_entered()
        self.was_event_name_entered()

        # Was the break location entered?
        self.was_continent_entered()
        self.was_country_entered()
        self.was_region_entered()
        self.was_break_name_entered()

        # Check to see if the entered_event exists in the entered_tour
        query = (select(Event.event_name)
                 .join(Tour, Tour.tour_id == Tour.tour_id)
                 .where(
                 and_(
                      Tour.tour_name == self.entered_tour_name,
                      Event.stop_nbr == self.entered_stop_nbr
                      )))

        result = session.execute(query)
        check_event = result.scalar()

        # Does the entered_event exist in the entered_tour
        if check_event is not None:
            print(f"The Event has already been entered."
                  f"\nTour Name: {self.entered_tour_name} "
                  f"\nEvent Name: {self.entered_event_name}")
            return

        # Get tour_id from tour table
        query = (select(Tour.tour_id)
                 .where(Tour.tour_name == self.entered_tour_name))
        result = session.execute(query)
        entered_tour_id = result.scalar()

        # Get break_id from break table
        query = (select(Break.break_id)
                 .join(Region, Break.region_id == Region.region_id)
                 .join(Country, Region.country_id == Country.country_id)
                 .join(Continent, Continent.continent_id == Country.continent_id)
                 .where(and_(
                             Break.break_name == self.entered_break_name,
                             Region.region == self.entered_region,
                             Country.country == self.entered_country,
                             Continent.continent == self.entered_continent
                            )))
        result = session.execute(query)
        entered_break_id = result.scalar()

        new_event = Event(event_name=self.entered_event_name,
                          tour_id=entered_tour_id,
                          stop_nbr=self.entered_stop_nbr,
                          break_id=entered_break_id,
                          open_date=self.entered_open_date,
                          close_date=self.entered_close_date)

        session.add(new_event)
        session.flush()
        session.commit()

    def add_new_round(self):
        session = Session()

        # Check that text is entered for round
        self.was_round_entered()

        # Check to see if the round name already exists
        query = (select(Round.round)
                 .where(Round.round == self.entered_round))

        result = session.execute(query)
        check_round = result.scalar()

        # Does the entered_event exist in the entered_tour
        if check_round is not None:
            print(f"The Round Type has already been entered."
                  f"\nEntered Round Type: {self.entered_round}")
            return

        # Create an instance of the Round class to add to wsl.round
        new_round = Round(round=self.entered_round)

        session.add(new_round)
        session.flush()
        session.commit()

    def add_new_heat_details(self):
        session = Session()

        # Was tour, event, round, and heat entered?
        self.was_tour_name_entered()
        self.was_event_name_entered()
        self.was_round_entered()
        self.was_heat_nbr_entered()

        # Does the heat already exist in the round, event, and tour?
        query = (select(HeatDetails.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .where(and_(
                             Tour.tour_name == self.entered_tour_name,
                             Event.event_name == self.entered_event_name,
                             Round.round == self.entered_round,
                             HeatDetails.heat_nbr == self.entered_heat_nbr
                            )))

        result = session.execute(query)
        check_heat_nbr = result.scalar()

        # Does the entered heat number already exist for the round, event, and tour
        if check_heat_nbr is not None:
            print(f"The entered heat number already exists."
                  f"\nEntered Tour: {self.entered_tour_name}"
                  f"\nEntered Event: {self.entered_event_name}"
                  f"\nEntered Round: {self.entered_round}"
                  f"\nEntered Heat Number: {self.entered_heat_nbr}")
            return

        # Get entered_event_id
        query = (select(Event.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .where(and_(Tour.tour_name == self.entered_tour_name,
                             Event.event_name == self.entered_event_name
                             )))

        result = session.execute(query)
        entered_event_id = result.scalar()

        # Get the entered_round_id
        query = (select(Round.round_id)
                 .where(Round.round == self.entered_round))
        result = session.execute(query)
        entered_round_id = result.scalar()

        # Create an instance of the HeatDetails class to add to wsl.heatdetails
        new_heat_details = HeatDetails(heat_nbr=self.entered_heat_nbr,
                                       event_id=entered_event_id,
                                       round_id=entered_round_id,
                                       wind=self.entered_wind,
                                       heat_date=self.entered_heat_date,
                                       duration=self.entered_duration,
                                       wave_min=self.entered_wave_min,
                                       wave_max=self.entered_wave_max
                                       )

        session.add(new_heat_details)
        session.flush()
        session.commit()

    def add_new_surfers_to_heat(self):
        session = Session()

        # was tour, event, round, heat, and surfer entered?
        self.was_tour_name_entered()
        self.was_event_name_entered()
        self.was_round_entered()
        self.was_heat_nbr_entered()
        self.was_surfer_entered()

        # Check to see if heat number exists in tour, event, round
        query = (select(HeatDetails.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .where(and_(
                            Tour.tour_name == self.entered_tour_name,
                            Event.event_name == self.entered_event_name,
                            Round.round == self.entered_round,
                            HeatDetails.heat_nbr == self.entered_heat_nbr
                            )))

        result = session.execute(query)
        entered_heat_id = result.scalar()

        # Does surfer already exist?
        query = (select(Surfers.surfer_id)
                 .where(Surfers.full_name == self.entered_surfer))
        result = session.execute(query)
        entered_surfer_id = result.scalar()

        if entered_surfer_id is None:
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nWe have not met that surfer yet. Add them to the database."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Surfer: {self.entered_surfer}")
            raise ValueError(no_entry_error)

        # Does this surfer aready exist in this heat?
        query = (select(HeatSurfers.surfer_heat_id)
                        .where(and_(HeatSurfers.heat_id == entered_heat_id,
                                    HeatSurfers.surfer_id == entered_surfer_id
                                    )))
        result = session.execute(query)
        check_heat_surfer = result.scalar()

        # Does the entered surfer and heat already exist for the round, event, and tour
        if check_heat_surfer is not None:
            print(f"The entered surfer already exists in the entered heat."
                  f"\nEntered Tour: {self.entered_tour_name}"
                  f"\nEntered Event: {self.entered_event_name}"
                  f"\nEntered Round: {self.entered_round}"
                  f"\nEntered Heat Number: {self.entered_heat_nbr}"
                  f"\nEntered Surfer: {self.entered_surfer}")
            return

        new_surfer_in_heat = HeatSurfers(heat_id=entered_heat_id,
                                         surfer_id=entered_surfer_id)

        session.add(new_surfer_in_heat)
        session.flush()
        session.commit()

    def add_new_heat_results(self):
        session = Session()

        # Was tour, event, round, heat, and surfer entered?
        self.was_tour_name_entered()
        self.was_event_name_entered()
        self.was_round_entered()
        self.was_heat_nbr_entered()
        self.was_surfer_entered()

        # Is the entered surfer in the entered heat?
        query = (select(HeatSurfers.surfer_heat_id)
                 .join(HeatDetails, HeatDetails.heat_id == HeatSurfers.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .join(Surfers, Surfers.surfer_id == HeatSurfers.surfer_id)
                 .where(and_(
                            Tour.tour_name == self.entered_tour_name,
                            Event.event_name == self.entered_event_name,
                            Round.round == self.entered_round,
                            HeatDetails.heat_nbr == self.entered_heat_nbr,
                            Surfers.full_name == self.entered_surfer
                            )))

        result = session.execute(query)
        check_surfer_in_heat = result.scalar()

        # Does the entered surfer and heat already exist for the round, event, and tour
        if check_surfer_in_heat is None:
            no_entry_error = (f"\n"
                              f"{self.div_dict['input_error'][0]:{self.div_dict['input_error'][1]}^{self.div_dict['input_error'][2]}}"
                              f"\nThe surfer has not been entered into the heat."
                              f"\n{self.div_dict['wipe_out_wav'][0]:{self.div_dict['wipe_out_wav'][1]}^{self.div_dict['wipe_out_wav'][2]}}"
                              f"\nEntered Tour Name: {self.entered_tour_name}"
                              f"\nEntered Event Name: {self.entered_event_name}"
                              f"\nEntered Round: {self.entered_round}"
                              f"\nEntered Heat: {self.entered_heat_nbr}"
                              f"\nEntered Surfer: {self.entered_surfer}")
            raise ValueError(no_entry_error)
        else:
            print(f"The entered surfer already exists in the entered heat."
                  f"\nEntered Tour: {self.entered_tour_name}"
                  f"\nEntered Event: {self.entered_event_name}"
                  f"\nEntered Round: {self.entered_round}"
                  f"\nEntered Heat Number: {self.entered_heat_nbr}"
                  f"\nEntered Surfer: {self.entered_surfer}")

        # Has the surfer results already been entered?
        query = (select(HeatResults.surfer_in_heat_id)
                 .join(HeatSurfers, HeatSurfers.surfer_heat_id == HeatResults.surfer_in_heat_id)
                 .join(HeatDetails, HeatDetails.heat_id == HeatSurfers.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .join(Surfers, Surfers.surfer_id == HeatSurfers.surfer_id)
                 .where(and_(
                            Tour.tour_name == self.entered_tour_name,
                            Event.event_name == self.entered_event_name,
                            Round.round == self.entered_round,
                            HeatDetails.heat_nbr == self.entered_heat_nbr,
                            Surfers.full_name == self.entered_surfer
                            )))

        result = session.execute(query)
        check_surfer_in_results = result.scalar()

        # Does the entered heat number already exist for the round, event, and tour
        if check_surfer_in_results is not None:
            print(f"Results for the entered surfer has already been entered into the heat.."
                  f"\nEntered Tour: {self.entered_tour_name}"
                  f"\nEntered Event: {self.entered_event_name}"
                  f"\nEntered Round: {self.entered_round}"
                  f"\nEntered Heat Number: {self.entered_heat_nbr}"
                  f"\nEntered Surfer: {self.entered_surfer}")
            return

        # Get the heat id
        query = (select(HeatDetails.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .where(and_(
                            Tour.tour_name == self.entered_tour_name,
                            Event.event_name == self.entered_event_name,
                            Round.round == self.entered_round,
                            HeatDetails.heat_nbr == self.entered_heat_nbr
                            )))

        result = session.execute(query)
        entered_heat_id = result.scalar()

        # Get the surfer in heat id
        query = (select(HeatSurfers.surfer_heat_id)
                 .join(Surfers, Surfers.surfer_id == HeatSurfers.surfer_id)
                 .join(HeatDetails, HeatDetails.heat_id == HeatSurfers.heat_id)
                 .join(Round, Round.round_id == HeatDetails.round_id)
                 .join(Event, Event.event_id == HeatDetails.event_id)
                 .join(Tour, Tour.tour_id == Event.tour_id)
                 .where(and_(
                            Tour.tour_name == self.entered_tour_name,
                            Event.event_name == self.entered_event_name,
                            Round.round == self.entered_round,
                            HeatDetails.heat_nbr == self.entered_heat_nbr,
                            Surfers.full_name == self.entered_surfer
                            )))

        result = session.execute(query)
        entered_surfer_in_heat_id = result.scalar()

        new_heat_results = HeatResults(heat_id=entered_heat_id,
                                       surfer_in_heat_id=entered_surfer_in_heat_id,
                                       pick_to_win_percent=self.entered_pick_to_win_percent,
                                       jersey_color=self.entered_jersey_color,
                                       status=self.entered_status,
                                       wave_1=self.entered_wave_1,
                                       wave_2=self.entered_wave_2,
                                       wave_3=self.entered_wave_3,
                                       wave_4=self.entered_wave_4,
                                       wave_5=self.entered_wave_5,
                                       wave_6=self.entered_wave_6,
                                       wave_7=self.entered_wave_7,
                                       wave_8=self.entered_wave_8,
                                       wave_9=self.entered_wave_9,
                                       wave_10=self.entered_wave_10,
                                       wave_11=self.entered_wave_11,
                                       wave_12=self.entered_wave_12,
                                       wave_13=self.entered_wave_13,
                                       wave_14=self.entered_wave_14,
                                       wave_15=self.entered_wave_15
                                       )

        session.add(new_heat_results)
        session.flush()
        session.commit()


#######################################################################################################################
# # 6.0 - Return lists
class LocationLists:
    def __init__(self,
                 entered_continent: Optional[str] = None,
                 entered_country: Optional[str] = None,
                 entered_region: Optional[str] = None,
                 ):

        self.entered_continent: Optional[str] = entered_continent
        self.entered_country: Optional[str] = entered_country
        self.entered_region: Optional[str] = entered_region

    @staticmethod
    def return_continents():
        session = Session()

        query = session.query(Continent.continent) \
                       .order_by(Continent.continent) \
                       .all()

        continent_list = []
        for continent in query:
            continent_list.append(continent[0])

        return continent_list

    def return_countries_from_continents(self):
        session = Session()

        query = session.query(Country.country)\
                       .join(Continent)\
                       .filter(Continent.continent == {self.entered_continent})

        country_list = []
        for country in query:
            country_list.append(country[0])

        session.close()

        return country_list

    def return_regions_from_countries(self):
        session = Session()

        query = session.query(Region.region)\
                       .join(Country)\
                       .join(Continent)\
                       .filter(Continent.continent == {self.entered_continent},
                               Country.country == {self.entered_country})

        region_list = []
        for region in query:
            region_list.append(region[0])

        session.close()

        return region_list

    def return_cities_from_regions(self):
        session = Session()

        query = session.query(City.city)\
                       .join(Region)\
                       .join(Country)\
                       .join(Continent)\
                       .filter(Continent.continent == {self.entered_continent},
                               Country.country == {self.entered_country},
                               Region.region == {self.entered_region})

        city_list = []
        for city in query:
            city_list.append(city[0])

        session.close()

        return city_list

# 7.0 - Return Tours
class TourLists:
    def __init__(self):
        pass

    @staticmethod
    def return_tour_years():
        session = Session()

        query = session.query(Tour.year) \
            .distinct() \
            .order_by(Tour.year) \
            .all()

        year_list = []
        for year in query:
            year_list.append(str(year[0]))

        return year_list

########################################################################################################################
# 6.0 - Testing


# # Enter a New Country
# inst = AddLocationDialog(entered_continent='North America',
#                    entered_country='USA')
# inst.add_new_country()


# # Enter a New Region
# inst = AddLocationDialog(entered_continent='South America',
#                    entered_country='Brazil',
#                    entered_region='Sao Paulo')
#
# inst.add_new_region()


# # Enter a New City
# inst = AddLocationDialog(entered_continent='North America',
#                    entered_country='Hawaii',
#                    entered_region='Oahu',
#                    entered_city='Honolulu')
#
# inst.add_new_city()

# # Enter a New Break
# inst = AddLocationDialog(entered_continent='North America',
#                    entered_country='Hawaii',
#                    entered_region='Oahu',
#                    entered_break_name='Pipeline',
#                    entered_break_type='Reef',
#                    entered_reliability='Consistent',
#                    entered_ability=None,
#                    entered_shoulder_burn=None,
#                    entered_clean=44,
#                    entered_blown_out=36,
#                    entered_too_small=20)
#
# inst.add_new_break()

# # Enter a New Surfer
# inst = AddSurfer(entered_gender='Men',
#                  entered_first_name='Ezekiel',
#                  entered_last_name='Lau',
#                  entered_stance='Regular',
#                  entered_rep_continent='North America',
#                  entered_rep_country='Hawaii',
#                  entered_birthday='1993-11-23',
#                  entered_height=186,
#                  entered_weight=92,
#                  entered_first_season=2008,
#                  entered_first_tour='Qualifying Series',
#                  entered_home_continent='North America',
#                  entered_home_country='Hawaii',
#                  entered_home_region='Oahu',
#                  entered_home_city='Honolulu')
# inst.add_new_surfer()

# # Enter a New Tour
# inst = AddTour(entered_year=2022,
#                entered_gender='Men',
#                entered_tour_type='Championship Tour')
# inst.add_new_tour()

# # Enter a New Event
# inst = AddTour(entered_tour_name='2022 Mens Championship Tour',
#                entered_event_name='Billabong Prop Pipeline',
#                entered_stop_nbr=1,
#                entered_continent='North America',
#                entered_country='Hawaii',
#                entered_region='Oahu',
#                entered_break_name='Pipeline',
#                entered_open_date='2022-01-29',
#                entered_close_date='2022-02-10')
# inst.add_new_event()

# # Enter a new round type
# inst = AddTour(entered_round='Opening Round')
# inst.add_new_round()

# # Enter details for a new heat
# inst = AddTour(entered_heat_nbr='1',
#                entered_tour_name='2022 Mens Championship Tour',
#                entered_event_name='Billabong Prop Pipeline',
#                entered_round='Opening Round',
#                entered_wind='Calm',
#                entered_heat_date='2022-01-29',
#                entered_duration=30,
#                entered_wave_min=4,
#                entered_wave_max=6)
# inst.add_new_heat_details()

# # Add new surfer to a heat
# inst = AddTour(entered_tour_name='2022 Mens Championship Tour',
#                entered_event_name='Billabong Prop Pipeline',
#                entered_round='Opening Round',
#                entered_heat_nbr='1',
#                entered_surfer='Ezekiel Lau'
#                )
# inst.add_new_surfers_to_heat()

# # Add New Heat Results
# inst = AddTour(entered_tour_name='2022 Mens Championship Tour',
#                entered_event_name='Billabong Prop Pipeline',
#                entered_round='Opening Round',
#                entered_heat_nbr='1',
#                entered_surfer='Ezekiel Lau',
#                entered_pick_to_win_percent=31,
#                entered_jersey_color='Black',
#                entered_status='Advanced',
#                entered_wave_1=4.50,
#                entered_wave_2=1.00,
#                entered_wave_3=0.73,
#                entered_wave_4=2.50
#                )
# inst.add_new_heat_results()


