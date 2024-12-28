def main():
    import time
    from pit_stop import PitStop
    from lap_timer import LapTimer

    pit_stop = PitStop()
    lap_timer = LapTimer()

    while True:
        action = input("Enter 'p' for pit stop, 'l' for lap, or 'q' to quit: ").strip().lower()

        if action == 'p':
            pit_stop.start_stop()
            input("Press Enter to end the pit stop...")
            pit_stop.end_stop()
            print(f"Pit Stop Duration: {pit_stop.duration:.2f} seconds")

        elif action == 'l':
            lap_timer.start_lap()
            input("Press Enter to end the lap...")
            lap_timer.end_lap()
            print(f"Lap Time: {lap_timer.lap_time:.2f} seconds")

        elif action == 'q':
            print("Exiting the application.")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()