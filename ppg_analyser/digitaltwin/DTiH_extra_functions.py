predictor_data = {
    'rmssd': {"AF":45,  "NAF":27}, 
    'pnn50': {"AF":0.11,"NAF":0.04}, 
    'lf/hf': {"AF":0.88,"NAF":2.75}
}


def interpolation(x: float, p: str = 'rmssd') -> float:
    value = (x - predictor_data[p]["NAF"]) * ((1)/(predictor_data[p]["AF"] - predictor_data[p]["NAF"]))

    if value > 1:
        return 1

    if value < 0:
        return 0

    return value

def compute_ppg_signal(filename):
    with open(filename) as f:
        print(f.read())