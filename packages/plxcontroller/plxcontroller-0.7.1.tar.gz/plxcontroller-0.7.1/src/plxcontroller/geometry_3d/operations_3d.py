from __future__ import annotations

import numpy as np
from skspatial.objects import Plane as ScikitSpatialPlane

from plxcontroller.geometry_3d.point_3d import Point3D
from plxcontroller.geometry_3d.polygon_3d import Polygon3D
from plxcontroller.globals import ABS_TOL


def project_vertically_point_onto_polygon_3d(
    point: Point3D,
    polygon: Polygon3D,
    tol: float | None = None,
) -> Point3D | None:
    """Returns the vertical projection of the Point3D onto Polygon3D.
    If the point is not within the boundaries of the projection of the polygon
    in the xy plane, then None is returned.

    Parameters
    ----------
    point : Point3D
        the point to project.
    polygon : Polygon3D
        the polygon to project onto.
    tol: float | None, optional
        the allowed tolerance to compared the coordinates of the cut_volumes
        and the polygons.
        If None given, then the globals.ABS_TOL will be used.
        Defaults to None.

    Returns
    -------
    Point3D | None
        the projected point onto the polygon.

    Raises
    ------
    TypeError
        if any parameter is not of the expected type.
    ValueError
        if tol is not >= 0.
    """
    # Validate input
    if not isinstance(point, Point3D):
        raise TypeError(
            f"Unexpected type for point. Expected Point3D, but got {type(point)}."
        )

    if not isinstance(polygon, Polygon3D):
        raise TypeError(
            f"Unexpected type for polygon. Expected Polygon3D, but got {type(point)}."
        )

    if tol is not None:
        if not isinstance(tol, (float, int)):
            raise TypeError(
                f"Unexpected type for tol. Expected float, but got {type(tol)}."
            )
        if not tol >= 0:
            raise ValueError(f"tol must be >= 0, but got {tol}.")

    # Initialize tol
    if tol is None:
        tol = ABS_TOL

    # Check whether the point is inside the projection of the polygon in the xy plane
    if not polygon.shapely_polygon_xy_plane.contains(
        point.shapely_point_xy_plane
    ) and not polygon.shapely_polygon_xy_plane.intersects(
        point.shapely_point_xy_plane.buffer(distance=tol)
    ):
        return None

    # Make plane using first three points of the polygon.
    # Note that all points in Polygon3D are coplanar, so it does not matter which
    # poitns are taken.
    plane = ScikitSpatialPlane.from_points(
        *[coord for coord in polygon.coordinates[:3]]
    )

    # Calculate the z-coordinate using the equation of the plane with the
    # point x and y coordinates input
    a, b, c, d = plane.cartesian()
    if not np.isclose(c, 0.0):
        z = (-d - a * point.x - b * point.y) / c
    else:
        # if the coefficient c is close to zero, it means that
        # the plane is parallel to the z-axis, so the z-coordinate
        # is the same as the point itself.
        z = point.z

    return Point3D(x=point.x, y=point.y, z=z)
