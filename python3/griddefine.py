import numpy as np

def gauss_latlons(nx, ny):
    lons = np.arange(nx) * (360./nx)
    if ny == 48:
        lats = np.array((
  -87.159101,
  -83.478927,
  -79.777053,
  -76.070248,
  -72.361585,
  -68.652021,
  -64.941951,
  -61.231574,
  -57.520991,
  -53.810273,
  -50.099455,
  -46.388558,
  -42.677604,
  -38.966612,
  -35.255582,
  -31.544525,
  -27.833444,
  -24.122348,
  -20.411238,
  -16.700118,
  -12.988989,
   -9.277853,
   -5.566713,
   -1.855572,
    1.855572,
    5.566713,
    9.277853,
   12.988989,
   16.700118,
   20.411238,
   24.122348,
   27.833444,
   31.544525,
   35.255582,
   38.966612,
   42.677604,
   46.388558,
   50.099455,
   53.810273,
   57.520991,
   61.231574,
   64.941951,
   68.652021,
   72.361585,
   76.070248,
   79.777053,
   83.478927,
   87.159101))
    elif ny == 94:
        lats = np.array((
  -88.541962,
  -86.653148,
  -84.753236,
  -82.850762,
  -80.947352,
  -79.043484,
  -77.139357,
  -75.235053,
  -73.330653,
  -71.426184,
  -69.521661,
  -67.617097,
  -65.712512,
  -63.807894,
  -61.903261,
  -59.998608,
  -58.093949,
  -56.189275,
  -54.284602,
  -52.379915,
  -50.475217,
  -48.570520,
  -46.665816,
  -44.761109,
  -42.856398,
  -40.951687,
  -39.046969,
  -37.142248,
  -35.237526,
  -33.332805,
  -31.428084,
  -29.523356,
  -27.618628,
  -25.713900,
  -23.809170,
  -21.904439,
  -19.999707,
  -18.094976,
  -16.190243,
  -14.285511,
  -12.380777,
  -10.476043,
   -8.571308,
   -6.666573,
   -4.761838,
   -2.857103,
   -0.952368,
    0.952368,
    2.857103,
    4.761838,
    6.666573,
    8.571308,
   10.476043,
   12.380777,
   14.285511,
   16.190243,
   18.094976,
   19.999707,
   21.904439,
   23.809170,
   25.713900,
   27.618628,
   29.523356,
   31.428084,
   33.332805,
   35.237526,
   37.142248,
   39.046969,
   40.951687,
   42.856398,
   44.761109,
   46.665816,
   48.570520,
   50.475217,
   52.379915,
   54.284602,
   56.189275,
   58.093949,
   59.998608,
   61.903261,
   63.807894,
   65.712512,
   67.617097,
   69.521661,
   71.426184,
   73.330653,
   75.235053,
   77.139357,
   79.043484,
   80.947352,
   82.850762,
   84.753236,
   86.653148,
   88.541962))
    elif ny == 190:
        lats = np.array((
  -89.276658,
  -88.339761,
  -87.397291,
  -86.453536,
  -85.509310,
  -84.564873,
  -83.620285,
  -82.675629,
  -81.730938,
  -80.786187,
  -79.841428,
  -78.896635,
  -77.951829,
  -77.007016,
  -76.062196,
  -75.117369,
  -74.172528,
  -73.227694,
  -72.282854,
  -71.338000,
  -70.393145,
  -69.448298,
  -68.503437,
  -67.558576,
  -66.613715,
  -65.668854,
  -64.723993,
  -63.779132,
  -62.834264,
  -61.889396,
  -60.944528,
  -59.999660,
  -59.054785,
  -58.109924,
  -57.165050,
  -56.220182,
  -55.275304,
  -54.330439,
  -53.385561,
  -52.440693,
  -51.495815,
  -50.550944,
  -49.606069,
  -48.661198,
  -47.716320,
  -46.771448,
  -45.826570,
  -44.881696,
  -43.936817,
  -42.991943,
  -42.047071,
  -41.102197,
  -40.157315,
  -39.212440,
  -38.267566,
  -37.322684,
  -36.377810,
  -35.432931,
  -34.488057,
  -33.543182,
  -32.598300,
  -31.653419,
  -30.708544,
  -29.763666,
  -28.818791,
  -27.873912,
  -26.929033,
  -25.984155,
  -25.039279,
  -24.094401,
  -23.149523,
  -22.204644,
  -21.259766,
  -20.314887,
  -19.370008,
  -18.425130,
  -17.480252,
  -16.535374,
  -15.590496,
  -14.645618,
  -13.700739,
  -12.755861,
  -11.810983,
  -10.866104,
   -9.921225,
   -8.976346,
   -8.031468,
   -7.086589,
   -6.141711,
   -5.196832,
   -4.251954,
   -3.307075,
   -2.362197,
   -1.417318,
   -0.472439,
    0.472439,
    1.417318,
    2.362197,
    3.307075,
    4.251954,
    5.196832,
    6.141711,
    7.086589,
    8.031468,
    8.976346,
    9.921225,
   10.866104,
   11.810983,
   12.755861,
   13.700739,
   14.645618,
   15.590496,
   16.535374,
   17.480252,
   18.425130,
   19.370008,
   20.314887,
   21.259766,
   22.204644,
   23.149523,
   24.094401,
   25.039279,
   25.984155,
   26.929033,
   27.873912,
   28.818791,
   29.763666,
   30.708544,
   31.653419,
   32.598300,
   33.543182,
   34.488057,
   35.432931,
   36.377810,
   37.322684,
   38.267566,
   39.212440,
   40.157315,
   41.102197,
   42.047071,
   42.991943,
   43.936817,
   44.881696,
   45.826570,
   46.771448,
   47.716320,
   48.661198,
   49.606069,
   50.550944,
   51.495815,
   52.440693,
   53.385561,
   54.330439,
   55.275304,
   56.220182,
   57.165050,
   58.109924,
   59.054785,
   59.999660,
   60.944528,
   61.889396,
   62.834264,
   63.779132,
   64.723993,
   65.668854,
   66.613715,
   67.558576,
   68.503437,
   69.448298,
   70.393145,
   71.338000,
   72.282854,
   73.227694,
   74.172528,
   75.117369,
   76.062196,
   77.007016,
   77.951829,
   78.896635,
   79.841428,
   80.786187,
   81.730938,
   82.675629,
   83.620285,
   84.564873,
   85.509310,
   86.453536,
   87.397291,
   88.339761,
   89.276658))
    else:
        raise ValueError("Unsupported 'ny' (lat grid #).")
    return (lons, lats)
