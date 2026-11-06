#!/usr/bun/env python3
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
    pack_shape = input("Enter the shape of your package : ")
    match pack_shape:
        case "rectangle":
            # Get the length of the package
            pack_length_str = input("Enter the length of your package (m): ")
            try:
                # cast the length to a float
                pack_length_float = float(pack_length_str)
                # Get the width of the package
                pack_width_str = input("Enter the width of your package (m): ")
                try:
                    # cast the width to a float
                    pack_width_float = float(pack_width_str)
                    # Get the weight of the package
                    pack_weight_str = input("Enter the weight of your package (kg) : ")
                    try:
                        # cast the weight to a float
                        pack_weight_float = float(pack_weight_str)
                        # Get the height of the package
                        pack_height_str = input(
                            "Enter the height of your package (m): "
                        )
                        try:
                            # cast the weight to a float
                            pack_height_float = float(pack_height_str)
                            # Check if all the users all the the measurements are positive
                            if (
                                pack_height_float > 0
                                and pack_length_float > 0
                                and pack_width_float > 0
                                and pack_weight_float > 0
                            ):
                                # Calculate the volume
                                pack_volume = (
                                    pack_length_float
                                    * pack_height_float
                                    * pack_width_float
                                )
                                # Display volume
                                print(
                                    "The volume of your package is : {:,.2f}m³".format(
                                        pack_volume
                                    )
                                )
                                if (
                                    pack_weight_float > constants.MAX_WEIGHT
                                    or pack_volume > constants.MAX_VOLUME
                                ):
                                    if pack_weight_float > constants.MAX_WEIGHT:
                                        print(
                                            "your package is not acceptable because it is too heavy"
                                        )
                                    else:
                                        print("your package has an appropriate weight")
                                    if pack_volume > constants.MAX_VOLUME:
                                        print(
                                            "your package is not acceptable because it is too voluminous"
                                        )
                                    else:
                                        print("your package has an appropriate volume")
                                else:
                                    print("your package is acceptable")
                            else:
                                print(
                                    "wrong input , all measurements have to be greater than 0"
                                )
                        except ValueError:
                            print("The height of your package is invalid")
                    except ValueError:
                        print("The weight of your package is invalid")
                except ValueError:
                    print("The width of your package is invalid")
            except ValueError:
                print("The length of your package is invalid")
            finally:
                print("Thanks for playing !!")
        case _:
            print("sorry , your package has to be in a rectangular shape")


if __name__ == "__main__":
    main()
