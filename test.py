
import sys
from app import calculate


assert calculate(sys.argv[2]) != 0, "Test Failed" # zero implies either wrong path or data absent

