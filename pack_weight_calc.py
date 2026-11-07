#!/usr/bin/env python3
# Created by : Adrian student
# Date : 06 th NOV 2026
# This program asks the user for the weight of the package ,
# the length of the package , the width of the package and
# the height of the package then calculates the volume of the
# package and finally,it tells the user whether or not the company
# will accept the package and if the package is not accepted, tell them why
import constants


def main():
    # get the package shape
    pack_shape = input("Enter the shape of your package (lowercase letters): ")
    if (
        pack_shape == "rectangle"
        or pack_shape == "rectangular shape"
        or pack_shape == "rectangular"
    ):
        # Get the length of the package
        pack_length_str = input("Enter the length of your package (cm): ")
        try:
            # cast the length to a float
            pack_length_float = float(pack_length_str)
            # Get the width of the package
            pack_width_str = input("Enter the width of your package (cm): ")
            try:
                # cast the width to a float
                pack_width_float = float(pack_width_str)
                # Get the weight of the package
                pack_weight_str = input("Enter the weight of your package (kg) : ")
                try:
                    # cast the weight to a float
                    pack_weight_float = float(pack_weight_str)
                    # Get the height of the package
                    pack_height_str = input("Enter the height of your package (cm): ")
                    try:
                        # cast the height to a float
                        pack_height_float = float(pack_height_str)
                        # Check if all the users measurements are positive
                        if (
                            pack_height_float > 0
                            and pack_length_float > 0
                            and pack_width_float > 0
                            and pack_weight_float > 0
                        ):
                            # Calculate the volume
                            pack_volume = (
                                pack_length_float * pack_height_float * pack_width_float
                            )
                            # Display volume to 2 decimal places
                            print(
                                "The volume of your package is : {:,.2f}cm³".format(
                                    pack_volume
                                )
                            )
                            if (
                                pack_weight_float > constants.MAX_WEIGHT
                                or pack_volume > constants.MAX_VOLUME
                            ):
                                if pack_weight_float > constants.MAX_WEIGHT:
                                    print(
                                        "Your package is not acceptable because it is too heavy"
                                    )
                                else:
                                    print("Your package has an appropriate weight")
                                if pack_volume > constants.MAX_VOLUME:
                                    print(
                                        "Your package is not acceptable because it is too voluminous"
                                    )
                                else:
                                    print("Your package has an appropriate volume")
                            else:
                                print("Your package is acceptable")
                        else:
                            print(
                                "Wrong input , all measurements have to be greater than 0"
                            )
                    except ValueError:
                        print("The height of your package is not a valid number")
                except ValueError:
                    print("The weight of your package is not a valid number")
            except ValueError:
                print("The width of your package is not a valid number")
        except ValueError:
            print("The length of your package is not a valid number")
    else:
        print("Sorry , your package has to be in a rectangular shape")
    print("Thanks for playing !!")


if __name__ == "__main__":
    main()
