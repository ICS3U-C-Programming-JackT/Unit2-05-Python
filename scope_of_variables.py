#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 15th, 2025

# Scope of variables program ran in python

import math

# Global variable
variableX = 25


def localVariable():
    # This shows what happens with local variables
    variableX = 10
    variableY = 30
    variableZ = 0  # Declare variableZ before using it

    variableX = variableX + 1
    variableZ = variableX + variableY

    print(
        "Local variableX, variableY, variableZ: {variableX} + {variableY} = {variableZ}\n"
    )


def globalVariable():
    # This shows what happens with global variables
    global variableX  # Explicitly reference global variableX
    variableY = 30
    variableZ = 0  # Declare variableZ before using it

    variableX = variableX + 1  # Modify global variableX
    variableZ = variableX + variableY

    print("Global variableX, variableY, variableZ:")
    print(variableX, "+", variableY, "=", variableZ)


def main():
    # This function calls local and global variable functions
    localVariable()
    globalVariable()

    print("Done.")


if __name__ == "__main__":
    main()
