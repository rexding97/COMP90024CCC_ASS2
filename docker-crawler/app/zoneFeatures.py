zones = {'Mel North': ['144.93661451060714', '-37.754348520701726', '7.214881296677225km'], 
         'Mel West': ['144.79562781651458', '-37.806474470182096', '7.649047751946029km'], 
         'Mel East': ['145.1275786504951', '-37.83981675964306', '8.183115868003842km'], 
         'Mel Center': ['144.95774808020107', '-37.829832692325255', '6.357621157540729km'], 
         'Mel SouthEast': ['145.09006024452617', '-37.94902612765296', '7.889969734511317km'], 
         'Syd North': ['151.19573834353753', '-33.81888007954359', '4.22997421124829km'], 
         'Syd Center': ['151.19940462417156', '-33.885837140719175', '4.102251948621608km'], 
         'Syd East': ['151.24518366113938', '-33.93225309726328', '4.71400066794769km'],
         'Syd West': ['151.08924072091597', '-33.890536715035005', '5.916963940711588km'], 
         'Syd Parramatta': ['150.98163391093223', '-33.82067626205178', '7.832544753753492km'],
         'Syd South': ['151.1214042166969', '-33.992511282151625', '8.368375286034787km'], 
         'Bri North': ['153.03703638855677', '-27.38186892509325', '8.482007366384316km'], 
         'Bri Center': ['153.0737086305447', '-27.481273776617194', '9.596138815170248km'], 
         'Bri South': ['153.0951271378391', '-27.587397998359943', '11.349168517993792km'], 
         'Bri West': ['152.8850952849796', '-27.596668303554356', '11.755528212789994km']}
zone_info = {
  "type": "FeatureCollection",
  "crs": {
    "type": "name",
    "properties": {
      "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
    }
  },
  "features": [
    {
      "type": "Feature",
      "properties": {
        "zone": "Geelong",
        "radius": 42.057963501693578,
        "center_longitude": 144.350006,
        "center_latitude": -38.150002
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              144.650006,
              -37.850002
            ],
            [
              144.650006,
              -38.450002
            ],
            [
              144.050006,
              -38.450002
            ],
            [
              144.050006,
              -37.850002
            ],
            [
              144.650006,
              -37.850002
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Melbourne",
        "radius": 42.038189498533008,
        "center_longitude": 144.946457,
        "center_latitude": -37.840935
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              145.246457,
              -37.540935
            ],
            [
              145.246457,
              -38.140935
            ],
            [
              144.646457,
              -38.140935
            ],
            [
              144.646457,
              -37.540935
            ],
            [
              145.246457,
              -37.540935
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Perth",
        "radius": 62.406365948458202,
        "center_longitude": 115.857048,
        "center_latitude": -31.953512
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              116.157048,
              -31.653512
            ],
            [
              116.157048,
              -32.253512
            ],
            [
              115.557048,
              -32.253512
            ],
            [
              115.557048,
              -31.653512
            ],
            [
              116.157048,
              -31.653512
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Brisbane",
        "radius": 44.042124096343258,
        "center_longitude": 153.021072,
        "center_latitude": -27.470125
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              153.321072,
              -27.170125
            ],
            [
              153.321072,
              -27.770125
            ],
            [
              152.721072,
              -27.770125
            ],
            [
              152.721072,
              -27.170125
            ],
            [
              153.321072,
              -27.170125
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Sydney",
        "radius": 41.912668572350952,
        "center_longitude": 151.2099,
        "center_latitude": -33.865143
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              151.5099,
              -33.565143
            ],
            [
              151.5099,
              -34.165143
            ],
            [
              150.9099,
              -34.165143
            ],
            [
              150.9099,
              -33.565143
            ],
            [
              151.5099,
              -33.565143
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Hobart",
        "radius": 38.360539423116769,
        "center_longitude": 147.324997,
        "center_latitude": -42.880554
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              147.624997,
              -42.580554
            ],
            [
              147.624997,
              -43.180554
            ],
            [
              147.024997,
              -43.180554
            ],
            [
              147.024997,
              -42.580554
            ],
            [
              147.624997,
              -42.580554
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Canberra",
        "radius": 41.973647356723255,
        "center_longitude": 149.128998,
        "center_latitude": -35.282001
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              149.428998,
              -34.982001
            ],
            [
              149.428998,
              -35.582001
            ],
            [
              148.828998,
              -35.582001
            ],
            [
              148.828998,
              -34.982001
            ],
            [
              149.428998,
              -34.982001
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Newcastle",
        "radius": 42.160321798904405,
        "center_longitude": 151.75,
        "center_latitude": -32.916668
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              152.05,
              -32.616668
            ],
            [
              152.05,
              -33.216668
            ],
            [
              151.45,
              -33.216668
            ],
            [
              151.45,
              -32.616668
            ],
            [
              152.05,
              -32.616668
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Adelaide",
        "radius": 46.652981069953178,
        "center_longitude": 138.599503,
        "center_latitude": -34.92123
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              138.899503,
              -34.62123
            ],
            [
              138.899503,
              -35.22123
            ],
            [
              138.299503,
              -35.22123
            ],
            [
              138.299503,
              -34.62123
            ],
            [
              138.899503,
              -34.62123
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Bunbury",
        "radius": 60.017343544042269,
        "center_longitude": 115.633331,
        "center_latitude": -33.333332
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              115.933331,
              -33.033332
            ],
            [
              115.933331,
              -33.633332
            ],
            [
              115.333331,
              -33.633332
            ],
            [
              115.333331,
              -33.033332
            ],
            [
              115.933331,
              -33.033332
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "zone": "Ballarat",
        "radius": 42.615748740651476,
        "center_longitude": 143.850006,
        "center_latitude": -37.549999
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              144.150006,
              -37.249999
            ],
            [
              144.150006,
              -37.849999
            ],
            [
              143.550006,
              -37.849999
            ],
            [
              143.550006,
              -37.249999
            ],
            [
              144.150006,
              -37.249999
            ]
          ]
        ]
      }
    }
  ]
}

def column(matrix, i):
    return [row[i] for row in matrix]

def getBoundingbox(zones):
    zoneName2boundingbox = {}
    for zone in zones:
        name = zone["properties"]["zone"]
        box = zone["geometry"]["coordinates"]
        zoneName2boundingbox[name] = [round(min(column(box[0],0)),3),round(min(column(box[0],1)),3),
                                      round(max(column(box[0],0)),3),round(max(column(box[0],1)),3)]
    return zoneName2boundingbox