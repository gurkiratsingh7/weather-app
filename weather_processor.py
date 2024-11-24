class WeatherProcessor:
    def __init__(self, weather_scraper, db_operations, plot_operations):
        # Initialize with the necessary classes for scraping, database, and plotting
        self.weather_scraper = weather_scraper
        self.db_operations = db_operations
        self.plot_operations = plot_operations
    
    def prompt_user(self):
        while True:
            # Display the main menu for the user
            print("\nWeather Data Processor")
            print("1. Download full weather data")
            print("2. Update weather data")
            print("3. Generate box plot (year range)")
            print("4. Generate line plot (month/year)")
            print("5. Exit")
            choice = input("Please select an option (1-5): ")
            
            if choice == '1':
                self.download_full_data()
            elif choice == '2':
                self.update_data()
            elif choice == '3':
                self.generate_box_plot()
            elif choice == '4':
                self.generate_line_plot()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")
    
    def download_full_data(self):
        # Trigger full weather data download from the scraper
        url = self.weather_scraper.get_starting_url()
        data = self.weather_scraper.scrape_weather_data(url)
        
        # Store the data in the database
        self.db_operations.save_data(data)
        print("Weather data has been downloaded and stored.")
    
    def update_data(self):
        # Check today's date and the latest date in the DB
        latest_date_in_db = self.db_operations.get_latest_date()
        today = self.weather_scraper.get_today_date()

        if latest_date_in_db < today:
            missing_data = self.weather_scraper.scrape_weather_data_for_missing_dates(latest_date_in_db, today)
            self.db_operations.save_data(missing_data)
            print("Weather data has been updated.")
        else:
            print("No new data to update.")
    
    def generate_box_plot(self):
        # Get the year range from the user for the box plot
        from_year = input("Enter starting year (e.g., 2000): ")
        to_year = input("Enter ending year (e.g., 2020): ")
        
        # Fetch data and generate box plot
        weather_data = self.db_operations.fetch_data_for_box_plot(from_year, to_year)
        self.plot_operations.create_box_plot(weather_data, from_year, to_year)
        print(f"Box plot generated for {from_year}-{to_year}.")
    
    def generate_line_plot(self):
        # Get the year and month from the user for the line plot
        year = input("Enter year (e.g., 2020): ")
        month = input("Enter month (1-12): ")
        
        # Fetch data and generate line plot
        weather_data = self.db_operations.fetch_data_for_line_plot(year, month)
        self.plot_operations.create_line_plot(weather_data, year, month)
        print(f"Line plot generated for {month}/{year}.")
