"""
Class: HdfMesh

Attribution: A substantial amount of code in this file is sourced or derived 
from the https://github.com/fema-ffrd/rashdf library, 
released under MIT license and Copyright (c) 2024 fema-ffrd

The file has been forked and modified for use in RAS Commander.
"""
from pathlib import Path
import h5py
import numpy as np
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Polygon, Point, LineString, MultiLineString, MultiPolygon
from shapely.ops import polygonize  # Importing polygonize to resolve the undefined name error
from typing import List, Tuple, Optional, Dict, Any
import logging
from .HdfBase import HdfBase
from .HdfUtils import HdfUtils
from .Decorators import standardize_input, log_call
from .LoggingConfig import setup_logging, get_logger

logger = get_logger(__name__)


class HdfMesh:
    """
    A class for handling mesh-related operations on HEC-RAS HDF files.

    This class provides methods to extract and analyze mesh data from HEC-RAS HDF files,
    including mesh area names, mesh areas, cell polygons, cell points, cell faces, and
    2D flow area attributes.

    Methods in this class are designed to work with the mesh geometry data stored in
    HEC-RAS HDF files, providing functionality to retrieve and process various aspects
    of the 2D flow areas and their associated mesh structures.

    Note: This class relies on HdfBase and HdfUtils for some underlying operations.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @staticmethod
    @standardize_input(file_type='plan_hdf')
    def mesh_area_names(hdf_path: Path) -> List[str]:
        """
        Return a list of the 2D mesh area names of the RAS geometry.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        List[str]
            A list of the 2D mesh area names (str) within the RAS geometry if 2D areas exist.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                if "Geometry/2D Flow Areas" not in hdf_file:
                    return list()
                return list(
                    [
                        HdfUtils.convert_ras_hdf_string(n.decode('utf-8'))  # Decode as UTF-8
                        for n in hdf_file["Geometry/2D Flow Areas/Attributes"][()]["Name"]
                    ]
                )
        except Exception as e:
            self.logger.error(f"Error reading mesh area names from {hdf_path}: {str(e)}")
            return list()

    @staticmethod
    @standardize_input(file_type='geom_hdf')
    def mesh_areas(hdf_path: Path) -> GeoDataFrame:
        """
        Return 2D flow area perimeter polygons.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        GeoDataFrame
            A GeoDataFrame containing the 2D flow area perimeter polygons if 2D areas exist.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                mesh_area_names = HdfMesh.mesh_area_names(hdf_path)
                if not mesh_area_names:
                    return GeoDataFrame()
                mesh_area_polygons = [
                    Polygon(hdf_file["Geometry/2D Flow Areas/{}/Perimeter".format(n)][()])
                    for n in mesh_area_names
                ]
                return GeoDataFrame(
                    {"mesh_name": mesh_area_names, "geometry": mesh_area_polygons},
                    geometry="geometry",
                    crs=HdfUtils.projection(hdf_file),  # Pass the h5py.File object instead of the path
                )
        except Exception as e:
            logger.error(f"Error reading mesh areas from {hdf_path}: {str(e)}")
            return GeoDataFrame()

    @staticmethod
    @standardize_input(file_type='geom_hdf')
    def mesh_cell_polygons(hdf_path: Path) -> GeoDataFrame:
        """
        Return 2D flow mesh cell polygons.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        GeoDataFrame
            A GeoDataFrame containing the 2D flow mesh cell polygons.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                mesh_area_names = HdfMesh.mesh_area_names(hdf_path)
                if not mesh_area_names:
                    return GeoDataFrame()

                face_gdf = HdfMesh.mesh_cell_faces(hdf_path)

                cell_dict = {"mesh_name": [], "cell_id": [], "geometry": []}
                for i, mesh_name in enumerate(mesh_area_names):
                    cell_cnt = hdf_file["Geometry/2D Flow Areas/Cell Info"][()][i][1]
                    cell_ids = list(range(cell_cnt))
                    cell_face_info = hdf_file[
                        "Geometry/2D Flow Areas/{}/Cells Face and Orientation Info".format(mesh_name)
                    ][()]
                    cell_face_values = hdf_file[
                        "Geometry/2D Flow Areas/{}/Cells Face and Orientation Values".format(mesh_name)
                    ][()][:, 0]
                    face_id_lists = list(
                        np.vectorize(
                            lambda cell_id: str(
                                cell_face_values[
                                    cell_face_info[cell_id][0] : cell_face_info[cell_id][0]
                                    + cell_face_info[cell_id][1]
                                ]
                            )
                        )(cell_ids)
                    )
                    mesh_faces = (
                        face_gdf[face_gdf.mesh_name == mesh_name][["face_id", "geometry"]]
                        .set_index("face_id")
                        .to_numpy()
                    )
                    cell_dict["mesh_name"] += [mesh_name] * cell_cnt
                    cell_dict["cell_id"] += cell_ids
                    cell_dict["geometry"] += list(
                        np.vectorize(
                            lambda face_id_list: (
                                lambda geom_col: Polygon(list(polygonize(geom_col))[0])
                            )(
                                np.ravel(
                                    mesh_faces[
                                        np.array(face_id_list.strip("[]").split()).astype(int)
                                    ]
                                )
                            )
                        )(face_id_lists)
                    )
                return GeoDataFrame(cell_dict, geometry="geometry", crs=HdfUtils.projection(hdf_file))
        except Exception as e:
            logger.error(f"Error reading mesh cell polygons from {hdf_path}: {str(e)}")
            return GeoDataFrame()
    @staticmethod
    @standardize_input(file_type='plan_hdf')
    def mesh_cell_points(hdf_path: Path) -> GeoDataFrame:
        """
        Return 2D flow mesh cell center points.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        GeoDataFrame
            A GeoDataFrame containing the 2D flow mesh cell center points.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                mesh_area_names = HdfMesh.mesh_area_names(hdf_path)
                if not mesh_area_names:
                    return GeoDataFrame()
                
                pnt_dict = {"mesh_name": [], "cell_id": [], "geometry": []}
                for mesh_name in mesh_area_names:
                    cell_center_coords = hdf_file[f"Geometry/2D Flow Areas/{mesh_name}/Cells Center Coordinate"][()]
                    cell_count = len(cell_center_coords)
                    
                    pnt_dict["mesh_name"] += [mesh_name] * cell_count
                    pnt_dict["cell_id"] += range(cell_count)
                    pnt_dict["geometry"] += list(
                        np.vectorize(lambda coords: Point(coords), signature="(n)->()")(
                            cell_center_coords
                        )
                    )
                return GeoDataFrame(pnt_dict, geometry="geometry", crs=HdfUtils.projection(hdf_path))
        except Exception as e:
            logger.error(f"Error reading mesh cell points from {hdf_path}: {str(e)}")
            return GeoDataFrame()

    @staticmethod
    @standardize_input(file_type='plan_hdf')
    def mesh_cell_faces(hdf_path: Path) -> GeoDataFrame:
        """
        Return 2D flow mesh cell faces.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        GeoDataFrame
            A GeoDataFrame containing the 2D flow mesh cell faces.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                mesh_area_names = HdfMesh.mesh_area_names(hdf_path)
                if not mesh_area_names:
                    return GeoDataFrame()
                face_dict = {"mesh_name": [], "face_id": [], "geometry": []}
                for mesh_name in mesh_area_names:
                    facepoints_index = hdf_file[
                        "Geometry/2D Flow Areas/{}/Faces FacePoint Indexes".format(mesh_name)
                    ][()]
                    facepoints_coordinates = hdf_file[
                        "Geometry/2D Flow Areas/{}/FacePoints Coordinate".format(mesh_name)
                    ][()]
                    faces_perimeter_info = hdf_file[
                        "Geometry/2D Flow Areas/{}/Faces Perimeter Info".format(mesh_name)
                    ][()]
                    faces_perimeter_values = hdf_file[
                        "Geometry/2D Flow Areas/{}/Faces Perimeter Values".format(mesh_name)
                    ][()]
                    face_id = -1
                    for pnt_a_index, pnt_b_index in facepoints_index:
                        face_id += 1
                        face_dict["mesh_name"].append(mesh_name)
                        face_dict["face_id"].append(face_id)
                        coordinates = list()
                        coordinates.append(facepoints_coordinates[pnt_a_index])
                        starting_row, count = faces_perimeter_info[face_id]
                        if count > 0:
                            coordinates += list(
                                faces_perimeter_values[starting_row : starting_row + count]
                            )
                        coordinates.append(facepoints_coordinates[pnt_b_index])
                        face_dict["geometry"].append(LineString(coordinates))
                return GeoDataFrame(face_dict, geometry="geometry", crs=HdfUtils.projection(hdf_path))
        except Exception as e:
            self.logger.error(f"Error reading mesh cell faces from {hdf_path}: {str(e)}")
            return GeoDataFrame()

    @staticmethod
    @standardize_input(file_type='geom_hdf')
    def get_geom_2d_flow_area_attrs(hdf_path: Path) -> Dict[str, Any]:
        """
        Return geometry 2D flow area attributes from a HEC-RAS HDF file.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the 2D flow area attributes.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                d2_flow_area = hdf_file.get("Geometry/2D Flow Areas/Attributes")
                if d2_flow_area is not None and isinstance(d2_flow_area, h5py.Dataset):
                    result = {}
                    for name in d2_flow_area.dtype.names:
                        try:
                            value = d2_flow_area[name][()]
                            if isinstance(value, bytes):
                                value = value.decode('utf-8')  # Decode as UTF-8
                            result[name] = value
                        except Exception as e:
                            logger.warning(f"Error converting attribute '{name}': {str(e)}")
                    return result
                else:
                    logger.info("No 2D Flow Area attributes found or invalid dataset.")
                    return {}
        except Exception as e:
            logger.error(f"Error reading 2D flow area attributes from {hdf_path}: {str(e)}")
            return {}


    @staticmethod
    @standardize_input(file_type='geom_hdf')
    def get_face_property_tables(hdf_path: Path) -> Dict[str, pd.DataFrame]:
        """
        Extract Face Property Tables for each Face in all 2D Flow Areas.

        Parameters
        ----------
        hdf_path : Path
            Path to the HEC-RAS geometry HDF file.

        Returns
        -------
        Dict[str, pd.DataFrame]
            A dictionary where keys are mesh names and values are DataFrames
            containing the Face Property Tables for all faces in that mesh.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                mesh_area_names = HdfMesh.mesh_area_names(hdf_path)
                if not mesh_area_names:
                    return {}

                result = {}
                for mesh_name in mesh_area_names:
                    area_elevation_info = hdf_file[f"Geometry/2D Flow Areas/{mesh_name}/Faces Area Elevation Info"][()]
                    area_elevation_values = hdf_file[f"Geometry/2D Flow Areas/{mesh_name}/Faces Area Elevation Values"][()]
                    
                    face_data = []
                    for face_id, (start_index, count) in enumerate(area_elevation_info):
                        face_values = area_elevation_values[start_index:start_index+count]
                        for z, area, wetted_perimeter, mannings_n in face_values:
                            face_data.append({
                                'Face ID': face_id,
                                'Z': z.decode('utf-8'),  # Decode as UTF-8
                                'Area': area.decode('utf-8'),  # Decode as UTF-8
                                'Wetted Perimeter': wetted_perimeter.decode('utf-8'),  # Decode as UTF-8
                                "Manning's n": mannings_n.decode('utf-8')  # Decode as UTF-8
                            })
                    
                    result[mesh_name] = pd.DataFrame(face_data)
                
                return result

        except Exception as e:
            logger.error(f"Error extracting face property tables from {hdf_path}: {str(e)}")
            return {}
