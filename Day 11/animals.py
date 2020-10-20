class Animal:
    name = "Lion"
    noise = "Rrrrr"
    color = "Gray"
    def make_noise(self):
        print(f"{self.noise}")
    def get_noise(self):
        return self.noise
    def set_noise(self, new_noise):
        self.noise = new_noise
    def show_name(self):
        print(f"{self.name}")
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def show_color(self):
        print(f"{self.color}")
    def get_name(self):
        return self.color
    def set_noise(self, new_color):
        self.color = new_color


class Wolf(Animal):
    noise = "GRrrrrrr"