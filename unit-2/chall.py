import math
import os
import random
import re
import sys
import yaml


# The function get_value should return a boolean based on result of evaluation
def evaluate(desired_actions, policies):
    # Write your code here
    print(desired_actions, policies)
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    data = yaml.load(sys.stdin)
    
    desired_actions = data["DesiredActions"]
    policies = data["Policies"]

    result = str(evaluate(desired_actions, policies))

    fptr.write(result + '\n')

    fptr.close()
