# car_rental_module.py
from datetime import datetime, timedelta
from random import randint 

class CarRental:
    def __init__(self, total_cars):
        self.total_cars = total_cars
        self.available_cars = total_cars
        self.rental_records = {}

    def display_available_cars(self):
        return f"Available cars: {self.available_cars}"

    def rent_hourly(self, num_cars, code):
        return self._rent_car(num_cars, "hourly", code)

    def rent_daily(self, num_cars, code):
        return self._rent_car(num_cars, "daily", code)

    def rent_weekly(self, num_cars,code):
        return self._rent_car(num_cars, "weekly", code)

    def _rent_car(self, num_cars, rental_mode,code):
        if num_cars > 0 and num_cars <= self.available_cars:
            current_time = datetime.now()
            code = str(randint(1000,9999))
            self.available_cars -= num_cars
            self.rental_records[code] = {"num_cars": num_cars, "rental_mode": rental_mode, "rental_time": current_time}
            return f"Renting {num_cars} cars for {rental_mode} for code {code}"
        else:
            return "Invalid request. Please check the number of cars and availability."
    


    def calculate_bill(self, rental_mode, rental_time, num_cars):
        current_time = datetime.now()
        rental_period = int((current_time - rental_time).total_seconds()//60)
        #print(rental_period)
        #print(datetime.now())
        #print(rental_time)
        if rental_mode == "hourly":
            return num_cars * rental_period *10
        elif rental_mode == "daily":
            return num_cars * rental_period * 0.5
        elif rental_mode == "weekly":
            return num_cars * rental_period *0.2
        
    def return_cars(self, code, rental_mode, num_cars):

        if code in self.rental_records and num_cars > 0:
            rented_info = self.rental_records[code]
            current_time = datetime.now()
            rental_time = rented_info['rental_time']
            rental_period = int((current_time - rental_time).total_seconds()//60)
            
            if rented_info["rental_mode"] == rental_mode and rented_info["num_cars"] == num_cars:
                del self.rental_records[code]
                self.available_cars += num_cars

                bill_amount = self.calculate_bill(rented_info["rental_mode"], rental_time, rented_info["num_cars"])
                return f"Cars returned. Bill amount: ${bill_amount}"
        return "Invalid return request. Please check the details."
   
