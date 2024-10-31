from __future__ import annotations

import os
import pathlib
import re
from itertools import combinations

import geopandas as gpd
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from shapely import Polygon
from tqdm.auto import tqdm

from mapreader.utils.load_frames import load_from_csv, load_from_geojson


class Runner:
    def __init__() -> None:
        """Initialise the Runner class."""
        # empty in the base class

    def _load_df(
        self,
        patch_df: pd.DataFrame | gpd.GeoDataFrame | str | pathlib.Path,
        parent_df: pd.DataFrame | gpd.GeoDataFrame | str | pathlib.Path,
        delimiter: str = ",",
    ):
        """Load the patch and parent dataframes.

        Parameters
        ----------
        patch_df : pd.DataFrame or gpd.GeoDataFrame or str or pathlib.Path
            The dataframe containing patch information. If a string, it should be the path to a csv file.
        parent_df : pd.DataFrame or gpd.GeoDataFrame or str or pathlib.Path
            The dataframe containing parent information. If a string, it should be the path to a csv file.
        delimiter : str, optional
            The delimiter used in the csv file, by default ",".
        """
        if isinstance(patch_df, pd.DataFrame):
            self.patch_df = patch_df

        elif isinstance(patch_df, (str, pathlib.Path)):
            print(f'[INFO] Reading "{patch_df}"')
            if re.search(r"\..?sv$", str(patch_df)):
                self.patch_df = load_from_csv(
                    patch_df,
                    delimiter=delimiter,
                )
            elif re.search(r"\..*?json$", str(patch_df)):
                self.patch_df = load_from_geojson(patch_df)
            else:
                raise ValueError(
                    "[ERROR] ``patch_df`` must be a path to a CSV/TSV/etc or geojson file, a pandas DataFrame or a geopandas GeoDataFrame."
                )

        else:
            raise ValueError(
                "[ERROR] ``patch_df`` must be a path to a CSV/TSV/etc or geojson file, a pandas DataFrame or a geopandas GeoDataFrame."
            )

        if isinstance(parent_df, pd.DataFrame):
            self.parent_df = parent_df

        elif isinstance(parent_df, (str, pathlib.Path)):
            print(f'[INFO] Reading "{parent_df}"')
            if re.search(r"\..?sv$", str(parent_df)):
                self.parent_df = load_from_csv(
                    parent_df,
                    delimiter=delimiter,
                )
            elif re.search(r"\..*?json$", str(parent_df)):
                self.parent_df = load_from_geojson(parent_df)
            else:
                raise ValueError(
                    "[ERROR] ``parent_df`` must be a path to a CSV/TSV/etc or geojson file, a pandas DataFrame or a geopandas GeoDataFrame."
                )

        else:
            raise ValueError(
                "[ERROR] ``parent_df`` must be a path to a CSV/TSV/etc or geojson file, a pandas DataFrame or a geopandas GeoDataFrame."
            )

    def run_all(
        self,
        return_dataframe: bool = False,
        min_ioa: float = 0.7,
    ) -> dict | pd.DataFrame:
        """Run the model on all images in the patch dataframe.

        Parameters
        ----------
        return_dataframe : bool, optional
            Whether to return the predictions as a pandas DataFrame, by default False
        min_ioa : float, optional
            The minimum intersection over area to consider two polygons the same, by default 0.7

        Returns
        -------
        dict or pd.DataFrame or gpd.GeoDataFrame
            A dictionary of predictions for each patch image or a DataFrame if `return_dataframe` is True.
        """
        img_paths = self.patch_df["image_path"].to_list()

        patch_predictions = self.run_on_images(
            img_paths, return_dataframe=return_dataframe, min_ioa=min_ioa
        )
        return patch_predictions

    def run_on_images(
        self,
        img_paths: str | pathlib.Path | list,
        return_dataframe: bool = False,
        min_ioa: float = 0.7,
    ) -> dict | pd.DataFrame:
        """Run the model on a list of images.

        Parameters
        ----------
        img_paths : str, pathlib.Path or list
            A list of image paths to run the model on.
        return_dataframe : bool, optional
            Whether to return the predictions as a pandas DataFrame, by default False
        min_ioa : float, optional
            The minimum intersection over area to consider two polygons the same, by default 0.7

        Returns
        -------
        dict or pd.DataFrame
            A dictionary of predictions for each image or a DataFrame if `return_dataframe` is True.
        """

        if isinstance(img_paths, (str, pathlib.Path)):
            img_paths = [img_paths]

        for img_path in tqdm(img_paths):
            _ = self.run_on_image(img_path, return_outputs=False, min_ioa=min_ioa)

        if return_dataframe:
            return self._dict_to_dataframe(
                self.patch_predictions, geo=False, parent=False
            )
        return self.patch_predictions

    def run_on_image(
        self,
        img_path: str | pathlib.Path,
        return_outputs=False,
        return_dataframe: bool = False,
        min_ioa: float = 0.7,
    ) -> dict | pd.DataFrame:
        """Run the model on a single image.

        Parameters
        ----------
        img_path : str or pathlib.Path
            The path to the image to run the model on.
        return_outputs : bool, optional
            Whether to return the outputs direct from the model, by default False
        return_dataframe : bool, optional
            Whether to return the predictions as a pandas DataFrame, by default False
        min_ioa : float, optional
            The minimum intersection over area to consider two polygons the same, by default 0.7

        Returns
        -------
        dict or pd.DataFrame
            The predictions for the image or the outputs from the model if `return_outputs` is True.
        """
        # load image
        img = Image.open(img_path).convert("RGB")
        img_array = np.array(img)

        # run inference
        outputs = self.predictor(img_array)
        outputs["image_id"] = os.path.basename(img_path)
        outputs["img_path"] = img_path

        if return_outputs:
            return outputs

        self.get_patch_predictions(outputs, min_ioa=min_ioa)

        if return_dataframe:
            return self._dict_to_dataframe(
                self.patch_predictions, geo=False, parent=False
            )
        return self.patch_predictions

    def _deduplicate(self, image_id, min_ioa=0.7):
        polygons = [instance[0] for instance in self.patch_predictions[image_id]]

        def calc_ioa(polygons, i, j):
            return polygons[i].intersection(polygons[j]).area / polygons[i].area

        # create an intersection matrix
        i_matrix = np.zeros((len(polygons), len(polygons)))

        for i, j in combinations(range(len(polygons)), 2):
            if polygons[i].intersects(polygons[j]):
                ioa_i = calc_ioa(polygons, i, j)
                ioa_j = calc_ioa(polygons, j, i)
                # bigger ioa means more overlap, so keep the one with the bigger ioa (only if more than min_ioa)
                if ioa_i > ioa_j and ioa_i > min_ioa:
                    i_matrix[i, j] = ioa_i
                elif ioa_j > ioa_i and ioa_j > min_ioa:
                    i_matrix[j, i] = ioa_j

        # if there is an intersection with another polygon then remove this polygon
        for i, row in enumerate(i_matrix):
            if any([ioa != 0 for ioa in row]):
                self.patch_predictions[image_id][i] = None
                i_matrix[:, i] = 0

        # remove the None values
        self.patch_predictions[image_id] = [
            prediction
            for prediction in self.patch_predictions[image_id]
            if prediction is not None
        ]

    def convert_to_parent_pixel_bounds(
        self,
        return_dataframe: bool = False,
        deduplicate: bool = False,
        min_ioa: float = 0.7,
    ) -> dict | pd.DataFrame:
        """Convert the patch predictions to parent predictions by converting pixel bounds.

        Parameters
        ----------
        return_dataframe : bool, optional
            Whether to return the predictions as a pandas DataFrame, by default False
        deduplicate : bool, optional
            Whether to deduplicate the parent predictions, by default False.
            Depending on size of parent images, this can be slow.
        min_ioa : float, optional
            The minimum intersection over area to consider two polygons the same, by default 0.7
            This is only used if `deduplicate` is True.

        Returns
        -------
        dict or pd.DataFrame
            A dictionary of predictions for each parent image or a DataFrame if `return_dataframe` is True.
        """

        for image_id, prediction in self.patch_predictions.items():
            parent_id = self.patch_df.loc[image_id, "parent_id"]
            if parent_id not in self.parent_predictions.keys():
                self.parent_predictions[parent_id] = []

            for instance in prediction:
                polygon = instance[0]

                xx, yy = (np.array(i) for i in polygon.exterior.xy)
                xx = xx + self.patch_df.loc[image_id, "pixel_bounds"][0]  # add min_x
                yy = yy + self.patch_df.loc[image_id, "pixel_bounds"][1]  # add min_y

                parent_polygon = Polygon(zip(xx, yy)).buffer(0)
                self.parent_predictions[parent_id].append(
                    [parent_polygon, *instance[1:], image_id]
                )

        if deduplicate:
            for parent_id in self.parent_predictions.keys():
                self._deduplicate_parent_level(parent_id, min_ioa=min_ioa)

        if return_dataframe:
            return self._dict_to_dataframe(
                self.parent_predictions, geo=False, parent=True
            )
        return self.parent_predictions

    def _deduplicate_parent_level(self, image_id, min_ioa=0.7):
        # get parent predictions for selected parent image
        parent_preds = np.array(self.parent_predictions[image_id])

        all_patches = parent_preds[:, -1]
        patches = np.unique(all_patches).tolist()

        for patch_i, patch_j in combinations(patches, 2):
            # get patch bounds
            patch_bounds_i = Polygon.from_bounds(
                *self.patch_df.loc[patch_i, "pixel_bounds"]
            )
            patch_bounds_j = Polygon.from_bounds(
                *self.patch_df.loc[patch_j, "pixel_bounds"]
            )

            if patch_bounds_i.intersects(patch_bounds_j):
                # get patch intersection
                intersection = patch_bounds_i.intersection(patch_bounds_j)

                # get polygons that overlap with the patch intersection
                polygons = []
                for i, pred in enumerate(parent_preds):
                    if pred[-1] in [patch_i, patch_j] and pred[0].intersects(
                        intersection
                    ):
                        polygons.append([i, pred[0]])

                def calc_ioa(polygons, i, j):
                    return (
                        polygons[i][1].intersection(polygons[j][1]).area
                        / polygons[i][1].area
                    )

                # create an intersection matrix
                i_matrix = np.zeros((len(polygons), len(polygons)))

                # calculate intersection over area for these polygons
                for i, j in combinations(range(len(polygons)), 2):
                    if polygons[i][1].intersects(polygons[j][1]):
                        ioa_i = calc_ioa(polygons, i, j)
                        ioa_j = calc_ioa(polygons, j, i)
                        # bigger ioa means more overlap, so keep the one with the bigger ioa (only if more than min_ioa)
                        if ioa_i > ioa_j and ioa_i > min_ioa:
                            i_matrix[i, j] = ioa_i
                        elif ioa_j > ioa_i and ioa_j > min_ioa:
                            i_matrix[j, i] = ioa_j

                # if there is an intersection with another polygon then remove this polygon
                for i, row in enumerate(i_matrix):
                    # index of the polygon in the parent_preds array
                    index = polygons[i][0]
                    if any([ioa != 0 for ioa in row]):
                        self.parent_predictions[image_id][index] = None
                        i_matrix[:, i] = 0

        # remove the None values
        self.parent_predictions[image_id] = [
            prediction
            for prediction in self.parent_predictions[image_id]
            if prediction is not None
        ]

    def convert_to_coords(
        self,
        return_dataframe: bool = False,
    ) -> dict | gpd.GeoDataFrame:
        """Convert the parent predictions to georeferenced predictions by converting pixel bounds to coordinates.

        Parameters
        ----------
        return_dataframe : bool, optional
            Whether to return the predictions as a geopandas GeoDataFrame, by default False

        Returns
        -------
        dict or gpd.GeoDataFrame
            A dictionary of predictions for each parent image or a DataFrame if `return_dataframe` is True.
        """
        if self.parent_predictions == {}:
            print("[INFO] Converting patch pixel bounds to parent pixel bounds.")
            _ = self.convert_to_parent_pixel_bounds()

        for parent_id, prediction in self.parent_predictions.items():
            if parent_id not in self.geo_predictions.keys():
                self.geo_predictions[parent_id] = []

                for instance in prediction:
                    polygon = instance[0]

                    xx, yy = (np.array(i) for i in polygon.exterior.xy)
                    xx = (
                        xx * self.parent_df.loc[parent_id, "dlon"]
                        + self.parent_df.loc[parent_id, "coordinates"][0]
                    )
                    yy = (
                        self.parent_df.loc[parent_id, "coordinates"][3]
                        - yy * self.parent_df.loc[parent_id, "dlat"]
                    )

                    crs = self.parent_df.loc[parent_id, "crs"]

                    parent_polygon_geo = Polygon(zip(xx, yy)).buffer(0)
                    self.geo_predictions[parent_id].append(
                        [parent_polygon_geo, crs, *instance[1:]]
                    )

        if return_dataframe:
            return self._dict_to_dataframe(self.geo_predictions, geo=True, parent=True)
        return self.geo_predictions

    def save_to_geojson(
        self,
        save_path: str | pathlib.Path,
    ) -> None:
        """Save the georeferenced predictions to a GeoJSON file.

        Parameters
        ----------
        save_path : str | pathlib.Path, optional
            Path to save the GeoJSON file
        """

        geo_df = self._dict_to_dataframe(self.geo_predictions, geo=True, parent=True)
        geo_df.to_file(save_path, driver="GeoJSON", engine="pyogrio")

    def show(
        self,
        image_id: str,
        figsize: tuple | None = (10, 10),
        border_color: str | None = "r",
        text_color: str | None = "b",
        image_width_resolution: int | None = None,
        return_fig: bool = False,
    ) -> None:
        """Show the predictions on an image.

        Parameters
        ----------
        image_id : str
            The image ID to show the predictions on.
        figsize : tuple | None, optional
            The size of the figure, by default (10, 10)
        border_color : str | None, optional
            The color of the border of the polygons, by default "r"
        text_color : str | None, optional
            The color of the text, by default "b"
        image_width_resolution : int | None, optional
            The maximum resolution of the image width, by default None
        return_fig : bool, optional
            Whether to return the figure, by default False

        Returns
        -------
        fig
            The matplotlib figure if `return_fig` is True.

        Raises
        ------
        ValueError
            If the image ID is not found in the patch or parent predictions.
        """

        if image_id in self.patch_predictions.keys():
            preds = self.patch_predictions
            image_path = self.patch_df.loc[image_id, "image_path"]

        elif image_id in self.parent_predictions.keys():
            preds = self.parent_predictions
            image_path = self.parent_df.loc[image_id, "image_path"]

        else:
            raise ValueError(
                f"[ERROR] {image_id} not found in patch or parent predictions."
            )

        img = Image.open(image_path)

        # if image_width_resolution is specified, resize the image
        if image_width_resolution:
            new_width = int(image_width_resolution)
            rescale_factor = new_width / img.width
            new_height = int(img.height * rescale_factor)
            img = img.resize((new_width, new_height), Image.LANCZOS)

        fig = plt.figure(figsize=figsize)
        ax = plt.gca()

        # check if grayscale
        if len(img.getbands()) == 1:
            ax.imshow(img, cmap="gray", vmin=0, vmax=255, zorder=1)
        else:
            ax.imshow(img, zorder=1)

        for instance in preds[image_id]:
            polygon = np.array(instance[0].exterior.coords.xy)
            center = instance[0].centroid.coords.xy
            patch = patches.Polygon(polygon.T, edgecolor=border_color, facecolor="none")
            ax.add_patch(patch)
            ax.text(
                center[0][0], center[1][0], instance[1], fontsize=8, color=text_color
            )

        plt.axis("off")
        plt.title(image_id)

        if return_fig:
            return fig
