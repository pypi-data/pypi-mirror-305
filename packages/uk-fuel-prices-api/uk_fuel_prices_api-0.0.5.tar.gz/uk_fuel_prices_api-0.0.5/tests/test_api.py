import pytest
import pandas as pd
from datetime import datetime, timedelta
from uk_fuel_prices_api import UKFuelPricesApi

class TestUKFuelPricesApi:
    api: UKFuelPricesApi = None

    @pytest.fixture
    async def setup_api(self):
        """Fixture to initialize and populate the API with data."""
        if self.api is not None:
            return self.api

        self.api = UKFuelPricesApi()
        success = await self.api.get_prices()
        assert success, "Failed to fetch initial price data"
        return self.api

    @pytest.mark.asyncio
    async def test_api_initialization(self, setup_api):
        """Test basic API initialization and data fetching."""
        api = await setup_api
        
        assert isinstance(api, UKFuelPricesApi)
        assert isinstance(api.stations, pd.DataFrame)
        assert not api.stations.empty
        assert api._cache_timestamp is not None
        assert isinstance(api._cache_timestamp, datetime)

    @pytest.mark.asyncio
    async def test_cache_functionality(self, setup_api):
        """Test the caching mechanism."""
        api = await setup_api
        
        # Store initial cache timestamp
        initial_timestamp = api._cache_timestamp
        
        # Request data again without force refresh
        success = await api.get_prices(force_refresh=False)
        assert success
        assert api._cache_timestamp == initial_timestamp
        
        # Force refresh and check timestamp updates
        api._cache_timestamp = datetime.now() - timedelta(hours=2)  # Ensure cache is old
        success = await api.get_prices(force_refresh=True)
        assert success
        assert api._cache_timestamp > initial_timestamp

    @pytest.mark.asyncio
    async def test_search_functionality(self, setup_api):
        """Test the search functionality."""
        api = await setup_api

        # Test valid search
        stations = api.search("ESSO")
        assert isinstance(stations, list)
        assert len(stations) > 0
        assert all(isinstance(station, dict) for station in stations)
        assert "brand" in stations[0]
        assert "site_id" in stations[0]
        
        # Test search with limit
        limited_stations = api.search("ESSO", n=3)
        assert len(limited_stations) <= 3
        
        # Test invalid searches
        assert api.search("") == []
        assert api.search(None) == []
        assert api.search("NONEXISTENTBRAND123456789") == []

    @pytest.mark.asyncio
    async def test_get_station(self, setup_api):
        """Test retrieving individual stations."""
        api = await setup_api
        
        # First get a valid station ID from the dataset
        test_station_id = api.stations.iloc[0]['site_id']
        
        # Test valid station retrieval
        station = api.get_station(test_station_id)
        assert isinstance(station, dict)
        assert station['site_id'] == test_station_id
        
        # Test invalid station IDs
        assert api.get_station("") is None
        assert api.get_station(None) is None
        assert api.get_station("NONEXISTENT123") is None

    def test_distance_calculation(self):
        """Test the static distance calculation method."""
        # Test known distances
        # London (51.5074, -0.1278) to Manchester (53.4808, -2.2426)
        dist = UKFuelPricesApi.distance(51.5074, -0.1278, 53.4808, -2.2426)
        assert isinstance(dist, float)
        assert 260 <= dist <= 264  # Roughly 262 km
        
        # Test same point
        dist = UKFuelPricesApi.distance(51.5074, -0.1278, 51.5074, -0.1278)
        assert dist == 0.0
        
        # Test invalid inputs
        with pytest.raises(Exception):
            UKFuelPricesApi.distance(None, None, None, None)

    @pytest.mark.asyncio
    async def test_stations_within_radius(self, setup_api):
        """Test finding stations within a given radius."""
        api = await setup_api
        
        # Use London coordinates for testing
        lat, lon = 51.5074, -0.1278
        
        # Test small radius
        small_radius = 1
        nearby_stations = api.stationsWithinRadius(lat, lon, small_radius)
        assert isinstance(nearby_stations, list)
        for station in nearby_stations:
            assert station['dist'] <= small_radius
            assert 'brand' in station
            assert 'site_id' in station
            assert 'latitude' in station
            assert 'longitude' in station
        
        # Test larger radius should return more stations
        larger_radius = 5
        more_stations = api.stationsWithinRadius(lat, lon, larger_radius)
        assert len(more_stations) >= len(nearby_stations)
        
        # Test invalid inputs
        assert api.stationsWithinRadius(None, None, 1) == []
        assert api.stationsWithinRadius(lat, lon, -1) == []
        assert api.stationsWithinRadius(lat, lon, 0) == []

    @pytest.mark.asyncio
    async def test_price_format_correction(self, setup_api):
        """Test the price format correction functionality."""
        api = await setup_api
        
        # Verify all fuel prices are in pounds (less than 10)
        for fuel_type in ['B7', 'E10', 'E5', 'SDV']:
            if fuel_type in api.stations.columns:
                prices = api.stations[fuel_type].dropna()
                assert all(price < 10 for price in prices), f"Found {fuel_type} prices that appear to be in pence"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        """Test the async context manager functionality."""
        async with UKFuelPricesApi() as api:
            assert api.session is not None
            assert not api.session.closed
            success = await api.get_prices()
            assert success
        
        assert api.session.closed