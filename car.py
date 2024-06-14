class Car:
    def __init__(
        self, make, model, year, mileage, price, description, features, category, images
    ):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.description = description
        self.features = features
        self.category = category
        self.images = images

    def view_car_details(self):
        return str(self)

    def __repr__(self) -> str:
        str = "Make: {}, Model: {}, Year: {}, Mileage: {}KM, Price: {}, Description: {}, Features: {}, Category: {}, Images: {}\n"
        str = str.format(
            self.make,
            self.model,
            self.year,
            self.mileage,
            self.price,
            self.description,
            self.features,
            self.category,
            self.images,
        )
        return str

    def __addToGarage__(self):
        return str(self)
    
    def __removeFromGarage__(self):
        return str(self)
