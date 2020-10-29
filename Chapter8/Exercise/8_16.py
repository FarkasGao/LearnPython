import sys
sys.path.append("..")

import Section2_PassParameter.ex_pets
Section2_PassParameter.ex_pets.describe_pet("A")

from Section2_PassParameter.ex_pets import describe_pet
describe_pet("B")

from Section2_PassParameter.ex_pets import describe_pet as pet
pet("C")

import Section2_PassParameter.ex_pets as pets
pets.describe_pet("D")

from Section2_PassParameter.ex_pets import *
describe_pet("E")