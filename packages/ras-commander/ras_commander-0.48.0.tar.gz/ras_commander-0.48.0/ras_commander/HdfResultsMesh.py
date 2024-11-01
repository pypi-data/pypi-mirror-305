"""
Class: HdfResultsMesh

Attribution: A substantial amount of code in this file is sourced or derived 
from the https://github.com/fema-ffrd/rashdf library, 
released under MIT license and Copyright (c) 2024 fema-ffrd

The file has been forked and modified for use in RAS Commander.
"""

import numpy as np
import pandas as pd
import xarray as xr
from pathlib import Path
import h5py
from typing import Union, List, Optional, Dict, Any, Tuple
from .HdfMesh import HdfMesh
from .HdfBase import HdfBase
from .HdfUtils import HdfUtils
from .Decorators import log_call, standardize_input
from .LoggingConfig import setup_logging, get_logger

logger = get_logger(__name__)

class HdfResultsMesh:
    """
    A class for handling mesh-related results from HEC-RAS HDF files.

    This class provides methods to extract and analyze mesh summary outputs,
    timeseries data, and various mesh-specific results such as water surface
    elevations, velocities, and errors.

    The class works with HEC-RAS plan HDF files and uses HdfBase and HdfUtils
    for common operations and utilities.

    Methods in this class use the @log_call decorator for logging and the
    @standardize_input decorator to handle different input types (e.g., 
    plan number, file path).

    Attributes:
        None

    Note:
        This class is designed to work with HEC-RAS version 6.0 and later.
    """

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_summary_output(hdf_path: Path, var: str, round_to: str = "100ms") -> pd.DataFrame:
        """
        Return the summary output data for a given variable.

        Args:
            hdf_path (Path): Path to the HEC-RAS plan HDF file.
            var (str): The summary output variable to retrieve.
            round_to (str): The time unit to round the datetimes to. Default: "100ms" (100 milliseconds).

        Returns:
            pd.DataFrame: DataFrame containing the summary output data.

        Raises:
            ValueError: If there's an error processing the summary output data.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, var, round_to)
        except Exception as e:
            logger.error(f"Error in mesh_summary_output: {str(e)}")
            logger.error(f"Variable: {var}")
            raise ValueError(f"Failed to get summary output: {str(e)}")

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_timeseries_output(hdf_path: Path, mesh_name: str, var: str, truncate: bool = True) -> xr.DataArray:
        """
        Get timeseries output for a specific mesh and variable.

        Args:
            hdf_path (Path): Path to the HDF file.
            mesh_name (str): Name of the mesh.
            var (str): Variable to retrieve. Valid options include:
                "Water Surface", "Face Velocity", "Cell Velocity X", "Cell Velocity Y",
                "Face Flow", "Face Water Surface", "Cell Volume", "Cell Volume Error",
                "Cell Water Surface Error", "Cell Courant", "Face Courant",
                "Cell Hydraulic Depth", "Cell Invert Depth",
                "Cell Cumulative Precipitation Depth", "Cell Divergence Term",
                "Cell Eddy Viscosity X", "Cell Eddy Viscosity Y", "Cell Flow Balance",
                "Cell Storage Term", "Cell Water Source Term", "Face Cumulative Volume",
                "Face Eddy Viscosity", "Face Flow Period Average", "Face Friction Term",
                "Face Pressure Gradient Term", "Face Shear Stress", "Face Tangential Velocity"
            truncate (bool): Whether to truncate the output (default True).

        Returns:
            xr.DataArray: DataArray containing the timeseries output.
        """
        with h5py.File(hdf_path, 'r') as hdf_file:
            return HdfResultsMesh._get_mesh_timeseries_output(hdf_file, mesh_name, var, truncate)

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_faces_timeseries_output(hdf_path: Path, mesh_name: str) -> xr.Dataset:
        """
        Get timeseries output for all face-based variables of a specific mesh.

        Args:
            hdf_path (Path): Path to the HDF file.
            mesh_name (str): Name of the mesh.

        Returns:
            xr.Dataset: Dataset containing the timeseries output for all face-based variables.
        """
        face_vars = ["Face Velocity", "Face Flow"]
        datasets = []
        
        for var in face_vars:
            try:
                da = HdfResultsMesh.mesh_timeseries_output(hdf_path, mesh_name, var)
                # Assign the variable name as the DataArray name
                da.name = var.lower().replace(' ', '_')
                datasets.append(da)
            except Exception as e:
                logger.warning(f"Failed to process {var} for mesh {mesh_name}: {str(e)}")
        
        if not datasets:
            logger.error(f"No valid data found for mesh {mesh_name}")
            return xr.Dataset()
        
        try:
            return xr.merge(datasets)
        except Exception as e:
            logger.error(f"Failed to merge datasets: {str(e)}")
            return xr.Dataset()

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_cells_timeseries_output(hdf_path: Path, mesh_names: Optional[Union[str, List[str]]] = None, var: Optional[str] = None, truncate: bool = False, ras_object: Optional[Any] = None) -> Dict[str, xr.Dataset]:
        """
        Get mesh cells timeseries output for specified meshes and variables.

        Args:
            hdf_path (Union[str, Path]): Path to the HDF file.
            mesh_names (Optional[Union[str, List[str]]]): Name(s) of the mesh(es). If None, processes all available meshes.
            var (Optional[str]): Name of the variable to retrieve. If None, retrieves all variables.
            truncate (bool): If True, truncates the output to remove trailing zeros.
            ras_object (Optional[Any]): RAS object, if available.

        Returns:
            Dict[str, xr.Dataset]: A dictionary of xarray Datasets, one for each mesh, containing the mesh cells timeseries output.

        Raises:
            ValueError: If there's an error processing the timeseries output data.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._mesh_cells_timeseries_output(hdf_file, mesh_names, var, truncate)
        except Exception as e:
            logger.error(f"Error in mesh_cells_timeseries_output: {str(e)}")
            raise ValueError(f"Error processing timeseries output data: {e}")

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_last_iter(hdf_path: Path) -> pd.DataFrame:
        """
        Get last iteration count for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.

        Returns:
            pd.DataFrame: DataFrame containing last iteration counts.
        """
        return HdfResultsMesh._get_mesh_summary_output(hdf_path, "Cell Last Iteration")


    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_max_ws(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get maximum iteration count for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing maximum iteration counts.

        Raises:
            ValueError: If there's an error processing the maximum iteration data.
            
        Note: The Maximum Iteration is labeled as "Cell Last Iteration" in the HDF file 
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Maximum Water Surface", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_max_ws: {str(e)}")
            raise ValueError(f"Failed to get maximum water surface: {str(e)}")
        




    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_min_ws(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get minimum water surface elevation for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing minimum water surface elevations.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Minimum Water Surface", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_min_ws: {str(e)}")
            raise ValueError(f"Failed to get minimum water surface: {str(e)}")

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_max_face_v(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get maximum face velocity for each mesh face.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing maximum face velocities.

        Raises:
            ValueError: If there's an error processing the maximum face velocity data.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Maximum Face Velocity", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_max_face_v: {str(e)}")
            raise ValueError(f"Failed to get maximum face velocity: {str(e)}")

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_min_face_v(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get minimum face velocity for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing minimum face velocities.

        Raises:
            ValueError: If there's an error processing the minimum face velocity data.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Minimum Face Velocity", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_min_face_v: {str(e)}")
            raise ValueError(f"Failed to get minimum face velocity: {str(e)}")

    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_max_ws_err(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get maximum water surface error for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing maximum water surface errors.

        Raises:
            ValueError: If there's an error processing the maximum water surface error data.
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Cell Maximum Water Surface Error", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_max_ws_err: {str(e)}")
            raise ValueError(f"Failed to get maximum water surface error: {str(e)}")


    @staticmethod
    @log_call
    @standardize_input(file_type='plan_hdf')
    def mesh_max_iter(hdf_path: Path, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get maximum iteration count for each mesh cell.

        Args:
            hdf_path (Path): Path to the HDF file.
            round_to (str): Time rounding specification (default "100ms").

        Returns:
            pd.DataFrame: DataFrame containing maximum iteration counts.

        Raises:
            ValueError: If there's an error processing the maximum iteration data.
            
        Note: The Maximum Iteration is labeled as "Cell Last Iteration" in the HDF file 
        """
        try:
            with h5py.File(hdf_path, 'r') as hdf_file:
                return HdfResultsMesh._get_mesh_summary_output(hdf_file, "Cell Last Iteration", round_to)
        except Exception as e:
            logger.error(f"Error in mesh_max_iter: {str(e)}")
            raise ValueError(f"Failed to get maximum iteration count: {str(e)}")
        
        
        


    @staticmethod
    def _get_mesh_timeseries_output_path(mesh_name: str, var_name: str) -> str:
        """
        Get the HDF path for mesh timeseries output.

        Args:
            mesh_name (str): Name of the mesh.
            var_name (str): Name of the variable.

        Returns:
            str: The HDF path for the specified mesh and variable.
        """
        return f"Results/Unsteady/Output/Output Blocks/Base Output/Unsteady Time Series/2D Flow Areas/{mesh_name}/{var_name}"


    @staticmethod
    def _mesh_cells_timeseries_output(hdf_file: h5py.File, mesh_names: Optional[Union[str, List[str]]] = None, var: Optional[str] = None, truncate: bool = False) -> Dict[str, xr.Dataset]:
        """
        Get mesh cells timeseries output for specified meshes and variables.

        Args:
            hdf_file (h5py.File): Open HDF file object.
            mesh_names (Optional[Union[str, List[str]]]): Name(s) of the mesh(es). If None, processes all available meshes.
            var (Optional[str]): Name of the variable to retrieve. If None, retrieves all variables.
            truncate (bool): If True, truncates the output to remove trailing zeros.

        Returns:
            Dict[str, xr.Dataset]: A dictionary of xarray Datasets, one for each mesh, containing the mesh cells timeseries output.

        Raises:
            ValueError: If there's an error processing the timeseries output data.
        """
        TIME_SERIES_OUTPUT_VARS = {
            "cell": [
                "Water Surface", "Depth", "Velocity", "Velocity X", "Velocity Y",
                "Froude Number", "Courant Number", "Shear Stress", "Bed Elevation",
                "Precipitation Rate", "Infiltration Rate", "Evaporation Rate",
                "Percolation Rate", "Groundwater Elevation", "Groundwater Depth",
                "Groundwater Flow", "Groundwater Velocity", "Groundwater Velocity X",
                "Groundwater Velocity Y"
            ],
            "face": [
                "Face Velocity", "Face Flow", "Face Water Surface", "Face Courant",
                "Face Cumulative Volume", "Face Eddy Viscosity", "Face Flow Period Average",
                "Face Friction Term", "Face Pressure Gradient Term", "Face Shear Stress",
                "Face Tangential Velocity"
            ]
        }

        try:
            start_time = HdfBase._get_simulation_start_time(hdf_file)
            time_stamps = HdfBase._get_unsteady_datetimes(hdf_file)

            if mesh_names is None:
                mesh_names = HdfResultsMesh._get_available_meshes(hdf_file)
            elif isinstance(mesh_names, str):
                mesh_names = [mesh_names]

            if var:
                variables = [var]
            else:
                variables = TIME_SERIES_OUTPUT_VARS["cell"] + TIME_SERIES_OUTPUT_VARS["face"]

            datasets = {}
            for mesh_name in mesh_names:
                data_vars = {}
                for variable in variables:
                    try:
                        path = HdfResultsMesh._get_mesh_timeseries_output_path(mesh_name, variable)
                        dataset = hdf_file[path]
                        values = dataset[:]
                        units = dataset.attrs.get("Units", "").decode("utf-8")

                        if truncate:
                            last_nonzero = np.max(np.nonzero(values)[1]) + 1 if values.size > 0 else 0
                            values = values[:, :last_nonzero]
                            truncated_time_stamps = time_stamps[:last_nonzero]
                        else:
                            truncated_time_stamps = time_stamps

                        if values.shape[0] != len(truncated_time_stamps):
                            logger.warning(f"Mismatch between time steps ({len(truncated_time_stamps)}) and data shape ({values.shape}) for variable {variable}")
                            continue

                        # Determine if this is a face-based or cell-based variable
                        id_dim = "face_id" if any(face_var in variable for face_var in TIME_SERIES_OUTPUT_VARS["face"]) else "cell_id"

                        data_vars[variable] = xr.DataArray(
                            data=values,
                            dims=['time', id_dim],
                            coords={'time': truncated_time_stamps, id_dim: np.arange(values.shape[1])},
                            attrs={'units': units}
                        )
                    except KeyError:
                        logger.warning(f"Variable '{variable}' not found in the HDF file for mesh '{mesh_name}'. Skipping.")
                    except Exception as e:
                        logger.error(f"Error processing variable '{variable}' for mesh '{mesh_name}': {str(e)}")

                if data_vars:
                    datasets[mesh_name] = xr.Dataset(
                        data_vars=data_vars,
                        attrs={'mesh_name': mesh_name, 'start_time': start_time}
                    )
                else:
                    logger.warning(f"No valid data variables found for mesh '{mesh_name}'")

            return datasets
        except Exception as e:
            logger.error(f"Error in _mesh_cells_timeseries_output: {str(e)}")
            raise ValueError(f"Error processing timeseries output data: {e}")



    @staticmethod
    def _get_mesh_timeseries_output(hdf_file: h5py.File, mesh_name: str, var: str, truncate: bool = True) -> xr.DataArray:
        """
        Get timeseries output for a specific mesh and variable.

        Args:
            hdf_file (h5py.File): Open HDF file object.
            mesh_name (str): Name of the mesh.
            var (str): Variable name to retrieve.
            truncate (bool): Whether to truncate the output to remove trailing zeros (default True).

        Returns:
            xr.DataArray: DataArray containing the timeseries output.

        Raises:
            ValueError: If the specified path is not found in the HDF file or if there's an error processing the data.
        """
        try:
            path = HdfResultsMesh._get_mesh_timeseries_output_path(mesh_name, var)
            
            if path not in hdf_file:
                raise ValueError(f"Path {path} not found in HDF file")

            dataset = hdf_file[path]
            values = dataset[:]
            units = dataset.attrs.get("Units", "").decode("utf-8")
            times = HdfBase._get_unsteady_datetimes(hdf_file)

            if truncate:
                non_zero = np.nonzero(values)[0]
                if len(non_zero) > 0:
                    start, end = non_zero[0], non_zero[-1] + 1
                    values = values[start:end]
                    times = times[start:end]

            # Determine if this is a face-based or cell-based variable
            id_dim = "face_id" if "Face" in var else "cell_id"
            dims = ["time", id_dim] if values.ndim == 2 else ["time"]
            coords = {"time": times}
            if values.ndim == 2:
                coords[id_dim] = np.arange(values.shape[1])

            return xr.DataArray(
                values,
                coords=coords,
                dims=dims,
                attrs={"units": units, "mesh_name": mesh_name, "variable": var},
            )
        except Exception as e:
            logger.error(f"Error in get_mesh_timeseries_output: {str(e)}")
            raise ValueError(f"Failed to get timeseries output: {str(e)}")


    @staticmethod
    def _get_mesh_timeseries_output_values_units(hdf_file: h5py.File, mesh_name: str, var: str) -> Tuple[np.ndarray, str]:
        """
        Get the mesh timeseries output values and units for a specific variable from the HDF file.

        Args:
            hdf_file (h5py.File): Open HDF file object.
            mesh_name (str): Name of the mesh.
            var (str): Variable name to retrieve.

        Returns:
            Tuple[np.ndarray, str]: A tuple containing the output values and units.
        """
        path = HdfResultsMesh._get_mesh_timeseries_output_path(mesh_name, var)
        group = hdf_file[path]
        values = group[:]
        units = group.attrs.get("Units")
        if units is not None:
            units = units.decode("utf-8")
        return values, units


    @staticmethod
    def _get_available_meshes(hdf_file: h5py.File) -> List[str]:
        """
        Get the names of all available meshes in the HDF file.

        Args:
            hdf_file (h5py.File): Open HDF file object.

        Returns:
            List[str]: A list of mesh names.
        """
        mesh_names = []
        base_path = "Geometry/2D Flow Areas"
        if base_path in hdf_file:
            for name in hdf_file[base_path]:
                if isinstance(hdf_file[f"{base_path}/{name}"], h5py.Group):
                    mesh_names.append(name)
        return mesh_names
    
    @staticmethod
    def _get_mesh_summary_output(hdf_file: h5py.File, var: str, round_to: str = "100ms") -> pd.DataFrame:
        """
        Get the summary output data for a given variable from the HDF file.

        Parameters
        ----------
        hdf_file : h5py.File
            Open HDF file object.
        var : str
            The summary output variable to retrieve.
        round_to : str, optional
            The time unit to round the datetimes to. Default is "100ms".

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the summary output data with attributes as metadata.

        Raises
        ------
        ValueError
            If the HDF file cannot be opened or read, or if the requested data is not found.
        """
        try:
            dfs = []
            start_time = HdfBase._get_simulation_start_time(hdf_file)
            
            logger.info(f"Processing summary output for variable: {var}")
            for mesh_name, cell_count in HdfBase._get_2d_flow_area_names_and_counts(hdf_file):
                logger.debug(f"Processing mesh: {mesh_name} with {cell_count} cells")
                group = HdfResultsMesh._get_mesh_summary_output_group(hdf_file, mesh_name, var)
                
                data = group[:]
                logger.debug(f"Data shape for {var} in {mesh_name}: {data.shape}")
                logger.debug(f"Data type: {data.dtype}")
                logger.debug(f"Attributes: {dict(group.attrs)}")
                
                if data.ndim == 2 and data.shape[0] == 2:
                    # Handle 2D datasets (e.g. Maximum Water Surface)
                    row_variables = group.attrs.get('Row Variables', [b'Value', b'Time'])
                    row_variables = [v.decode('utf-8').strip() for v in row_variables]
                    
                    df = pd.DataFrame({
                        "mesh_name": [mesh_name] * data.shape[1],
                        "cell_id" if "Face" not in var else "face_id": range(data.shape[1]),
                        f"{var.lower().replace(' ', '_')}": data[0, :],
                        f"{var.lower().replace(' ', '_')}_time": HdfUtils._ras_timesteps_to_datetimes(
                            data[1, :], start_time, time_unit="days", round_to=round_to
                        )
                    })
                    
                elif data.ndim == 1:
                    # Handle 1D datasets (e.g. Cell Last Iteration)
                    df = pd.DataFrame({
                        "mesh_name": [mesh_name] * len(data),
                        "cell_id" if "Face" not in var else "face_id": range(len(data)),
                        var.lower().replace(' ', '_'): data
                    })
                    
                else:
                    raise ValueError(f"Unexpected data shape for {var} in {mesh_name}. "
                                  f"Got shape {data.shape}")
                
                # Add geometry based on variable type
                if "Face" in var:
                    face_df = HdfMesh.mesh_cell_faces(hdf_file)
                    if not face_df.empty:
                        df = df.merge(face_df[['mesh_name', 'face_id', 'geometry']], 
                                    on=['mesh_name', 'face_id'], 
                                    how='left')
                else:
                    cell_df = HdfMesh.mesh_cell_points(hdf_file)
                    if not cell_df.empty:
                        df = df.merge(cell_df[['mesh_name', 'cell_id', 'geometry']], 
                                    on=['mesh_name', 'cell_id'], 
                                    how='left')
                
                # Add group attributes as metadata
                df.attrs['mesh_name'] = mesh_name
                for attr_name, attr_value in group.attrs.items():
                    if isinstance(attr_value, bytes):
                        attr_value = attr_value.decode('utf-8')
                    elif isinstance(attr_value, np.ndarray):
                        attr_value = attr_value.tolist()
                    df.attrs[attr_name] = attr_value
                
                dfs.append(df)
            
            if not dfs:
                return pd.DataFrame()
                
            result = pd.concat(dfs, ignore_index=True)
            
            # Combine attributes from all meshes
            combined_attrs = {}
            for df in dfs:
                for key, value in df.attrs.items():
                    if key not in combined_attrs:
                        combined_attrs[key] = value
                    elif combined_attrs[key] != value:
                        combined_attrs[key] = f"Multiple values: {combined_attrs[key]}, {value}"
            
            result.attrs.update(combined_attrs)
            
            logger.info(f"Processed {len(result)} rows of summary output data")
            return result
        
        except Exception as e:
            logger.error(f"Error processing summary output data: {e}")
            raise ValueError(f"Error processing summary output data: {e}")
        

    @staticmethod
    def _get_mesh_summary_output_group(hdf_file: h5py.File, mesh_name: str, var: str) -> Union[h5py.Group, h5py.Dataset]:
        """
        Return the HDF group for a given mesh and summary output variable.

        Args:
            hdf_file (h5py.File): Open HDF file object.
            mesh_name (str): Name of the mesh.
            var (str): Name of the summary output variable.

        Returns:
            Union[h5py.Group, h5py.Dataset]: The HDF group or dataset for the specified mesh and variable.

        Raises:
            ValueError: If the specified group or dataset is not found in the HDF file.
        """
        output_path = f"Results/Unsteady/Output/Output Blocks/Base Output/Summary Output/2D Flow Areas/{mesh_name}/{var}"
        output_item = hdf_file.get(output_path)
        if output_item is None:
            raise ValueError(f"Could not find HDF group or dataset at path '{output_path}'")
        return output_item

    @staticmethod
    def plot_mesh_variable(variable_df: pd.DataFrame, variable_name: str, colormap: str = 'viridis', point_size: int = 10) -> None:
        """
        Plot any mesh variable with consistent styling.
        
        Args:
            variable_df (pd.DataFrame): DataFrame containing the variable data
            variable_name (str): Name of the variable (for labels)
            colormap (str): Matplotlib colormap to use. Default: 'viridis'
            point_size (int): Size of the scatter points. Default: 10

        Returns:
            None

        Raises:
            ImportError: If matplotlib is not installed
            ValueError: If required columns are missing from variable_df
        """
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            logger.error("matplotlib is required for plotting. Please install it with 'pip install matplotlib'")
            raise ImportError("matplotlib is required for plotting")

        # Get cell coordinates if not in variable_df
        if 'geometry' not in variable_df.columns:
            cell_coords = HdfMesh.mesh_cell_points(plan_hdf_path)
            merged_df = pd.merge(variable_df, cell_coords, on=['mesh_name', 'cell_id'])
        else:
            merged_df = variable_df
            
        # Extract coordinates, handling None values
        merged_df = merged_df.dropna(subset=['geometry'])
        merged_df['x'] = merged_df['geometry'].apply(lambda geom: geom.x if geom is not None else None)
        merged_df['y'] = merged_df['geometry'].apply(lambda geom: geom.y if geom is not None else None)
        
        # Drop any rows with None coordinates
        merged_df = merged_df.dropna(subset=['x', 'y'])
        
        if len(merged_df) == 0:
            logger.error("No valid coordinates found for plotting")
            raise ValueError("No valid coordinates found for plotting")
            
        # Create plot
        fig, ax = plt.subplots(figsize=(12, 8))
        scatter = ax.scatter(merged_df['x'], merged_df['y'], 
                           c=merged_df[variable_name], 
                           cmap=colormap, 
                           s=point_size)
        
        # Customize plot
        ax.set_title(f'{variable_name} per Cell')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        plt.colorbar(scatter, label=variable_name)
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.rcParams.update({'font.size': 12})
        plt.tight_layout()
        plt.show()

