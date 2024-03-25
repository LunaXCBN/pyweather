from beaupy.spinners import Spinner

def wspinner(start: bool, text: str = None):
    vspinner = Spinner([f"> {text} ",
                        f"> {text} █",
                        f"> {text} ██",
                        f"> {text} ███",
                        f"> {text} ████",
                        f"> {text} █████",
                        f"> {text} ██████"], text = "")
    
    if start == False:
        vspinner.stop()

    vspinner.start()

def stop_wspinner():
    vspinner.stop()
