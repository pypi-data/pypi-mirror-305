from geo_skeletons import PointSkeleton, GriddedSkeleton
import numpy as np
from geo_skeletons.decorators import add_datavar

import geo_parameters as gp


def test_point():
    points = PointSkeleton(lon=(1, 2, 3, 4), lat=(10, 20, 30, 40))

    np.testing.assert_array_almost_equal(
        points.lon(), points.sel(inds=slice(0, 10)).lon()
    )

    np.testing.assert_array_almost_equal([3, 4], points.sel(inds=slice(2, 4)).lon())
    np.testing.assert_array_almost_equal([1, 4], points.sel(inds=[0, 3]).lon())

    np.testing.assert_array_almost_equal([10, 40], points.sel(inds=[0, 3]).lat())

    np.testing.assert_array_almost_equal(
        points.lon(), points.isel(inds=slice(0, 10)).lon()
    )

    np.testing.assert_array_almost_equal([3, 4], points.isel(inds=slice(2, 4)).lon())
    np.testing.assert_array_almost_equal([1, 4], points.isel(inds=[0, 3]).lon())

    np.testing.assert_array_almost_equal([10, 40], points.isel(inds=[0, 3]).lat())


def test_point_old_datavar():
    @add_datavar(name="dummyvar")
    class Dummy(PointSkeleton):
        pass

    points = Dummy(lon=(1, 2, 3, 4), lat=(10, 20, 30, 40))

    points.set_dummyvar(5)
    assert points.core.data_vars() == ["dummyvar"]

    points2 = points.isel(inds=1)
    assert points2.core.data_vars() == ["dummyvar"]


def test_point_dynamic_datavar():
    class Dummy(PointSkeleton):
        pass

    points = Dummy.add_datavar("dummyvar")(lon=(1, 2, 3, 4), lat=(10, 20, 30, 40))
    points.set_dummyvar(5)
    assert points.core.data_vars() == ["dummyvar"]

    points2 = points.isel(inds=1)
    assert points2.core.data_vars() == ["dummyvar"]


def test_point_dynamic_datavar_geoparam():
    class Dummy(PointSkeleton):
        pass

    points = Dummy.add_datavar(gp.wave.Hs("hsig"))(
        lon=(1, 2, 3, 4), lat=(10, 20, 30, 40)
    )

    points.set_hsig(5)
    assert points.core.data_vars() == ["hsig"]

    points2 = points.isel(inds=1)
    assert points2.core.data_vars() == ["hsig"]
    assert points2.meta.get("hsig") == points.meta.get("hsig")


def test_point_dynamic_datavars_from_ds():

    class Dummy(PointSkeleton):
        pass

    points = Dummy.add_datavar(gp.wave.Hs("hsig"))(
        lon=(1, 2, 3, 4), lat=(10, 20, 30, 40)
    )
    points.set_hsig(5)
    assert points.core.data_vars() == ["hsig"]

    ds = points.ds()
    points2 = PointSkeleton.from_ds(ds, dynamic=True, keep_ds_names=True)

    assert points2.core.data_vars() == ["hsig"]
    assert points2.meta.get("hsig") == points.meta.get("hsig")

    points3 = PointSkeleton.from_ds(ds, dynamic=True)

    assert points3.core.data_vars() == ["hs"]
    assert points3.meta.get("hs") == points.meta.get("hsig")


def test_gridded():
    points = GriddedSkeleton(lon=(1, 2, 3, 4), lat=(10, 20, 30, 40))
    np.testing.assert_array_almost_equal(
        points.lon(), points.sel(lon=slice(0, 10)).lon()
    )
    np.testing.assert_array_almost_equal(points.lon(), points.sel(lat=10).lon())
    np.testing.assert_array_almost_equal([1, 2, 3], points.sel(lon=slice(1, 3)).lon())

    np.testing.assert_array_almost_equal(
        [1, 2, 3], points.sel(lon=slice(1, 3), lat=10).lon()
    )

    np.testing.assert_array_almost_equal([1, 2, 4], points.sel(lon=[1, 2, 4]).lon())

    np.testing.assert_array_almost_equal([1, 2, 4], points.isel(lon=[0, 1, 3]).lon())
    np.testing.assert_array_almost_equal(points.lat(), points.isel(lon=[0, 1, 3]).lat())

    np.testing.assert_array_almost_equal([1, 2, 4], points.isel(lon=[0, 0, 1, 3]).lon())
