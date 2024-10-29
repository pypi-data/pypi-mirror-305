def netcdf(nc_file, shapefile, output_file):
    """
    Description:
    ------------------
    Reads in a NetCDF file, converts it into a dataframe, clips to an uploaded shapefile, merges shapefile attributes, and saves the file as a geodataframe for upload into QGIS.

        Notes:
            CRS of input .nc file is assumed to be 3857 in this case
            Datasets must be in the same workplace directory as the python script

        Parameters:
        ------------------
        nc_file = Name of the .nc file name

        shapefile = Name of desired shapefile

        output_file = filename of desired output file

        
        Example:
        ------------------
        netcdf("data_file.nc", "shape_file.shp", "merged_dataset.gpkg")

    """

    # Create a list of steps for the progress bar
    steps = [
        "Opening .nc file",
        "Converting .nc to dataframe",
        "Creating geometry column",
        "Converting to GeoDataFrame",
        "Setting CRS to EPSG:3857",
        "Transforming CRS to WGS84 (EPSG:4326)",
        "Reading shapefile",
        "Ensuring CRS match between .nc data and shapefile",
        "Clipping .nc data to shapefile boundary",
        "Merging shapefile attributes with .nc data",
        "Saving as Geopackage"
    ]

    with tqdm(total=len(steps), desc="Processing NetCDF", unit="step") as pbar:
    

        # Open .nc file
        ds = xr.open_dataset(nc_file)
        pbar.set_description(steps[0])
        pbar.update(1)
        print(".nc file opened")
    
        # Convert to a dataframe
        df = ds.to_dataframe().reset_index()
        pbar.set_description(steps[1])
        pbar.update(1)
        print(".nc file converted to dataframe")
    
        # Convert x and y to a geometry column
        geometry = [Point(xy) for xy in zip(df['x'], df['y'])]
        pbar.set_description(steps[2])
        pbar.update(1)
        print("x and y coordinates converted into a geometry column")
        
        # Convert to a gpd
        geo_df = gpd.GeoDataFrame(df, geometry=geometry)
        pbar.set_description(steps[3])
        pbar.update(1)
        print(".nc dataframe converted into a geodataframe")
        
        # Set CRS, hard-coded into this script as 3857 is the default CRS for this specific file
        geo_df.set_crs(epsg = 3857, inplace=True)
        pbar.set_description(steps[4])
        pbar.update(1)
        
        # Set CRS to WGS84
        geo_df.to_crs(epsg=4326, inplace=True)
        pbar.set_description(steps[5])
        pbar.update(1)
        print("CRS set to 4326")
    
        # Read in shapefile
        shp = gpd.read_file(shapefile)
        pbar.set_description(steps[6])
        pbar.update(1)
        print("Shapefile uploaded")

        # Ensure CRS match
        if geo_df.crs != shp.crs:
            points = geo_df.to_crs(shp.crs)
            pbar.set_description(steps[7])
        pbar.update(1)

    
        # Clip the .nc file to the shapefile boundary
        clip = gpd.clip(geo_df, shp)
        pbar.set_description(steps[8])
        pbar.update(1)
        print(".nc file clipped to shapefile")
    
        # Merge shapefile attributes to the .nc geometry and drop duplicate coordinates
        merged = gpd.sjoin(geo_df, shp, how="inner", predicate="intersects")
        merged = merged.drop_duplicates(subset = "geometry")
        pbar.set_description(steps[9])
        pbar.update(1)
        print("Shapefile attributes merged with .nc dataframe")
    
        # Save new file as a Geopackage file
        merged.to_file(output_file, driver="GPKG")
        pbar.set_description(steps[10])
        pbar.update(1)
        print("Geopackage saved to directory")