import pandas as pd

def createSampleData() -> pd.DataFrame:
    df = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']})

    return df

def printData():
    data = createSampleData().to_json()
    print(data)

if __name__ == '__main__':
    printData()
