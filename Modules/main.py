# import cả file => vd:converters.lbs_to_kg
import converters
import utils
# import 1 function  trong file
from converters import kg_to_lbs

# todo : modules

kg = converters.lbs_to_kg(70)
print(f"70 lbs = {kg} kg")

lbs = kg_to_lbs(31.5)
print(f"31.5 kg = {lbs} lbs")

numbers = [1, 4, 2]
max = utils.get_max(numbers)
print(f"Max of numbers is {max}")
