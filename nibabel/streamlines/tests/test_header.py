import numpy as np

from nose.tools import assert_equal, assert_true
from numpy.testing import assert_array_equal

from nibabel.streamlines.header import StreamlinesHeader


def test_streamlines_header():
    header = StreamlinesHeader()
    assert_true(header.nb_streamlines is None)
    assert_true(header.nb_scalars_per_point is None)
    assert_true(header.nb_properties_per_streamline is None)
    assert_array_equal(header.voxel_sizes, (1, 1, 1))
    assert_array_equal(header.voxel_to_world, np.eye(4))
    assert_equal(header.extra, {})

    # Modify simple attributes
    header.nb_streamlines = 1
    header.nb_scalars_per_point = 2
    header.nb_properties_per_streamline = 3
    assert_equal(header.nb_streamlines, 1)
    assert_equal(header.nb_scalars_per_point, 2)
    assert_equal(header.nb_properties_per_streamline, 3)

    # Modifying voxel_sizes should be reflected in voxel_to_world
    header.voxel_sizes = (2, 3, 4)
    assert_array_equal(header.voxel_sizes, (2, 3, 4))
    assert_array_equal(np.diag(header.voxel_to_world), (2, 3, 4, 1))

    # Modifying scaling of voxel_to_world should be reflected in voxel_sizes
    header.voxel_to_world = np.diag([4, 3, 2, 1])
    assert_array_equal(header.voxel_sizes, (4, 3, 2))
    assert_array_equal(header.voxel_to_world, np.diag([4, 3, 2, 1]))

    # Test that we can run __repr__ without error.
    repr(header)
