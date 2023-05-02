import pdb
from models.Manufacturer import Manufacturer
from models.SuperpowerProduct import SuperpowerProduct

import repositories.manufacturer_repository as manufacturer_repository
import repositories.superpower_product_repository as superpower_product_repository

superpower_product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("SuperFlower Limited", "The mere aroma of these flowers will allow you to fly amongst the stars.", "superflower_support@superf.com", "Santa Marta del Cerro, Spain")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Super-Magnet Corporation", "Teleport to a different dimension with your friends, using our magnets.", "super_magnet_support@supermagnetcorp.com", "County Wicklow, Ireland")
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Shadow-Power Enterprise", "Be invisible by sinking into your shadow.", "shadow.power_support@shadow_power_enterprise.com", "Forest Hills, Queens, NY, United States")
manufacturer_repository.save(manufacturer_3)

manufacturer_4 = Manufacturer("Asteroid Eyes Corporation", "Wear contact lenses that give you 20/20 vision and also lets you gaze at the stars as though they're right beside you.", "asteroid_eyes_support@asteroid_eyes_corp.com", "Dublin, Ireland")
manufacturer_repository.save(manufacturer_4)

superpower_product_1 = SuperpowerProduct("Sapphire Glow", "This flower allows you to glow in the dark as you fly.", 70, 12.0, 30.0, manufacturer_1)
superpower_product_repository.save(superpower_product_1)

superpower_product_2 = SuperpowerProduct("Violet Flow Magnet", "This magnet makes you sing pitch-perfectly so you can sing with the birds or with Beyonce.", 3, 10.0, 20.0, manufacturer_2)
superpower_product_repository.save(superpower_product_2)

superpower_product_3 = SuperpowerProduct("Rosy Cheeky Juice", "This shadow catcher drink enables you to be more confident and have super speed - effects last for up to 48 hours.", 100, 14.0, 35.0, manufacturer_3)
superpower_product_repository.save(superpower_product_3)

superpower_product_4 = SuperpowerProduct("Asteroids Floating Contact Lenses", "These contact lenses let you see the stratosphere and the moon whilst teleporting there!", 0, 30.0, 70.0, manufacturer_4)
superpower_product_repository.save(superpower_product_4)


# Checking that superpower_product select_all() function is working

# all = superpower_product_repository.select_all()

# for superpower_product in all:
#     print(superpower_product.manufacturer.__dict__)
#     print(superpower_product.__dict__)



