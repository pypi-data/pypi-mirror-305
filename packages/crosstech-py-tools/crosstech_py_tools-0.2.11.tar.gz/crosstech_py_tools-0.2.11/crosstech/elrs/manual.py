import json
import geopandas as gpd
from tqdm import tqdm
from google.cloud import storage


class ManualModel:
    @staticmethod
    def download() -> gpd.GeoDataFrame:
        """
        Downloads the Manual Network Model from the Google Cloud Storage bucket.
        Manual Network Model is a derivative of the Full Network Model.

        Source:
        - Google Cloud Storage Bucket: hubble-elr-geojsons
        - Blob: Data/2024-March-Altered-Mileages/NetworkModel.geojson

        Returns:
        --------
        elr_gdf : gpd.GeoDataFrame
            GeoDataFrame of the Manual Network Model.

        Notes:
        ------
        See docs: https://docs.crosstech.co.uk/doc/network-model-kfGqIB0lxL
        """
        client = storage.Client()
        bucket = client.get_bucket("hubble-elr-geojsons")
        blob = bucket.blob("Data/2024-March-Altered-Mileages/NetworkModel.geojson")

        elr_string = json.loads(blob.download_as_string())
        elr_gdf = gpd.GeoDataFrame.from_features(elr_string["features"])
        elr_gdf.crs = "EPSG:27700"

        return elr_gdf

    @staticmethod
    def into_chunks(gdf: gpd.GeoDataFrame, **kwargs) -> list[gpd.GeoDataFrame]:
        """
        Splits an input GeoDataFrame into chunks by ELR Eighth. This is intended
        to be used for the Manual Network Model.
        
        Useful for investigating ELR Eighths in isolation, in conjunction with the
        `explore` method from this library, module `crosstech.locations.explore`.
        
        Chunk is defined as a collection of linestrings that are associated with
        a single ELR Eighth.
        
        Parameters:
        -----------
        gdf : gpd.GeoDataFrame
            The GeoDataFrame to be split into chunks.
            
        show_progress : bool (optional)
            Whether to show progress bar. Default is True.
            
        Returns:
        --------
        chunks : list[gpd.GeoDataFrame]
            A list of GeoDataFrames, each representing a chunk.
            
        Notes:
        ------
        See docs: https://docs.crosstech.co.uk/doc/elr-eighths-F2t3yi6OvV
        """
        if "elr_eighth_id" not in gdf.columns:
            raise ValueError(
                "The GeoDataFrame does not have the 'elr_eighth_id' column. Cannot proceed."
            )

        if "show_progress" in kwargs:
            show_progress = kwargs["show_progress"]
        else:
            show_progress = True

        # Control if we want to see progress
        if show_progress:
            iterator = tqdm(
                gdf["elr_eighth_id"].unique(),
                desc="Chunking by ELR Eighth",
                unit="ELR Eighth",
            )
        else:
            iterator = gdf["elr_eighth_id"].unique()

        chunks = []

        for ee_id in iterator:
            chunks.append(gdf[gdf["elr_eighth_id"] == ee_id])

        return chunks
