from beaupy.spinners import Spinner

lonlat_spinner = Spinner(['Converting location to lon/lat... ',
                        'Converting location to lon/lat... █',
                        'Converting location to lon/lat... ██',
                        'Converting location to lon/lat... ███',
                        'Converting location to lon/lat... ████',
                        'Converting location to lon/lat... █████',
                        'Converting location to lon/lat... ██████'], text="")

weather_spinner = Spinner(['Getting weather data... ',
                        'Getting weather data... █',
                        'Getting weather data... ██',
                        'Getting weather data... ███',
                        'Getting weather data... ████',
                        'Getting weather data... █████',
                        'Getting weather data... ██████'], text="")
