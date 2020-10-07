import pytest
import logic





class Test:
    @pytest.mark.base
    def test_list(self):
        lst_coords = logic.get_road(1, 2)
        assert isinstance(lst_coords, list), 'return type is not list '

    @pytest.mark.base
    def test_type(self):
        lst_coords = logic.get_road(1, 2)
        for i, coord in enumerate(lst_coords):
            for num in lst_coords[i]:
                assert isinstance(num, float), 'coordinates wrong type'

    @pytest.mark.base
    def test_point(self):
        lst_coords = logic.get_road(1, 2)
        for i, coord in enumerate(lst_coords):
            assert len(coord) == 2, 'Point have more 2 coordinates'

    @pytest.mark.advanced
    def test_limints(self):
        lst_coords = logic.get_road(1, 2)
        for i, coord in enumerate(lst_coords):
            assert (-90) <= lst_coords[i][0], 'longitude is smaller that her limits'
            assert lst_coords[i][0] <= 90, 'longitude is more that her limits'

        for i, coord in enumerate(lst_coords):
            assert (-180) <= lst_coords[i][1], 'latitude is smaller that her limits'
            assert lst_coords[i][1] <= 180, 'latitude is more that her limits'

    @pytest.mark.advanced
    def test_breakpoint(self):
        lst_coords = logic.get_road(1, 2)
        lst_defer_long = []
        for ind, coord in enumerate(lst_coords):
            if ind > 0:
                defer = lst_coords[ind][0] - lst_coords[ind - 1][0]
                lst_defer_long.append(abs(defer))
        c = min(lst_defer_long) * 10
        for i in lst_defer_long:
            assert c >= i, 'road have break point'
        lst_defer_lat = []
        for ind, coord in enumerate(lst_coords):
            if ind > 0:
                defer = lst_coords[ind][0] - lst_coords[ind - 1][0]
                lst_defer_lat.append(abs(defer))
        c = min(lst_defer_lat) * 10
        for i in lst_defer_lat:
            assert c >= i, 'road have break point'

