import matplotlib.pyplot as plt

class PlotOperations:
    """
    A class to handle plotting operations using matplotlib.
    """

    def __init__(self):
        """Initialize the PlotOperations class."""
        pass

    def create_boxplot(self, data, start_year, end_year):
        """
        Create a boxplot of mean temperature data for the range of years.
        
        Args:
            data (dict): A dictionary where the keys are months (1-12) and values are lists of mean temperatures.
            start_year (int): The start year for the data range.
            end_year (int): The end year for the data range.
        """
        plt.figure(figsize=(10, 6))
        months = list(data.keys())
        temperatures = list(data.values())
        
        plt.boxplot(temperatures, labels=[f"Month {m}" for m in months])
        plt.title(f"Mean Temperatures ({start_year} - {end_year})")
        plt.xlabel("Month")
        plt.ylabel("Mean Temperature (°C)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def create_lineplot(self, data, year, month):
        """
        Create a line plot of mean daily temperatures for a specific month and year.
        
        Args:
            data (list): A list of mean daily temperatures for the specified month and year.
            year (int): The year of the data.
            month (int): The month of the data.
        """
        days = range(1, len(data) + 1)

        plt.figure(figsize=(10, 6))
        plt.plot(days, data, marker='o', linestyle='-', color='b')
        plt.title(f"Mean Daily Temperatures - {year}-{month:02}")
        plt.xlabel("Day of the Month")
        plt.ylabel("Mean Temperature (°C)")
        plt.xticks(days)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    def process_boxplot_data(self, raw_data):
        """
        Process raw data to prepare it for the boxplot.
        
        Args:
            raw_data (list): A list of tuples containing date and mean temperature.
        
        Returns:
            dict: A dictionary with months as keys and lists of mean temperatures as values.
        """
        processed_data = {}
        for date, mean_temp in raw_data:
            year, month, day = map(int, date.split('-'))
            if month not in processed_data:
                processed_data[month] = []
            processed_data[month].append(mean_temp)
        return processed_data

    def process_lineplot_data(self, raw_data, target_month):
        """
        Process raw data to prepare it for the line plot.
        
        Args:
            raw_data (list): A list of tuples containing date and mean temperature.
            target_month (int): The target month to extract daily mean temperatures.
        
        Returns:
            list: A list of mean temperatures for the specified month.
        """
        processed_data = []
        for date, mean_temp in raw_data:
            year, month, day = map(int, date.split('-'))
            if month == target_month:
                processed_data.append(mean_temp)
        return processed_data
