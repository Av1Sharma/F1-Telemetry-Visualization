import fastf1
import pandas as pd

DRIVER_CODES = {
    "verstappen": "VER", "perez": "PER", "hamilton": "HAM", "russell": "RUS", "leclerc": "LEC", 
    "sainz": "SAI", "norris": "NOR", "piastri": "PIA", "alonso": "ALO", "stroll": "STR", 
    "ocon": "OCO", "gasly": "GAS", "bottas": "BOT", "zhou": "ZHO", "magnussen": "MAG", 
    "hulkenberg": "HUL", "tsunoda": "TSU", "ricciardo": "RIC", "albon": "ALB", "sargeant": "SAR"
}

def load_telemetry_data(year, race, session_type, driver_name):
    try:
        driver_code = DRIVER_CODES.get(driver_name.lower())

        if not driver_code:
            print(f"Driver '{driver_name}' not found. Please enter a valid last name.")
            return
        
        print(f"Loading telemetry for {driver_name.title()} ({driver_code}) in {race} {year} - {session_type} session...")

        session = fastf1.get_session(year, race, session_type)
        session.load()

        telemetry = session.laps.pick_driver(driver_code).get_telemetry()

        data = pd.DataFrame({
            'Timestamp': telemetry['Time'],
            'Speed': telemetry['Speed'] / 3.6,
            'X': telemetry['X'],
            'Y': telemetry['Y'],
            'Z': telemetry['Z']
        })

        print(f"Loaded {len(data)} rows of telemetry data.")

        data.to_csv('data/telemetry.csv', index=False)

        print("Data saved to data/telemetry.csv")

        return data

    except Exception as e:
        print(f"Error loading telemetry data: {e}")

if __name__ == '__main__':
    year = int(input("Enter race year: "))
    race = input("Enter race name: ")
    session_type = input("Enter session type (R, Q, FP1, FP2, FP3): ").upper()
    driver_name = input("Enter driver last name: ").strip()

    load_telemetry_data(year, race, session_type, driver_name)
