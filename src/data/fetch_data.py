import requests
import ee
import geemap  
import folium  

ee.Authenticate()
ee.Initialize(project='ee-raedambach')
longitude = -149.56194 
latitude = -17.00872


def download_satellite_data():
    # Placeholder for downloading satellite data
    print('Downloading satellite images...')
    reef = ee.Geometry.Point([longitude, latitude])  
    dataset = ee.ImageCollection('COPERNICUS/S2_HARMONIZED').filterBounds(reef).filterDate('2024-01-01', '2024-01-02')
    print('Number of images in collection:', dataset.size().getInfo())
    dataset = dataset.median()  
    Map = geemap.Map()  
    Map.centerObject(reef, 10)  
    Map.addLayer(dataset, {'bands': ['B4', 'B3', 'B2'], 'min': 0, 'max': 3000}, 'Sentinel-2')  
    Map 

    print('Finished')

if __name__ == '__main__':
    download_satellite_data()