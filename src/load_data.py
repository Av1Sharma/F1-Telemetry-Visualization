import fastf1
import pandas as pd

def load_telemetry_data():
    try:
        session = fastf1.get_session(2025, 'Chinese', 'Q')
        session.load()

        telemetry = session.laps.pick_driver('VER').get_telemetry()

        positions = telemetry[['X', 'Y', 'Z']]
        speeds = telemetry['Speed'] / 3.6  
        timestamps = telemetry['Time']

        data = pd.DataFrame({'Timestamp': timestamps, 'Speed': speeds, 'X': positions['X'], 'Y': positions['Y'], 'Z': positions['Z']})

        print(f"Loaded {len(data)} rows of telemetry data")

        data.to_csv('data/telemetry_data.csv', index=False)

        print("Data saved to data/telemetry_data.csv")

        return data

    except Exception as e:
        print(f"Error loading telemetry data: {e}")

if __name__ == '__main__':
    load_telemetry_data()
