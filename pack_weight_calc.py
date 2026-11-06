#!/usr/bin/env python3
# Created by: Adrian student
# Date: 06 NOV 2026
# This program asks the user for package measurements,
# calculates the volume and checks package eligibility.
import constants


def main():
    """Get package measurements and determine package eligibility."""
    # Get the package shape
    pack_shape = input("Enter the shape of your package: ")
    match pack_shape:
        case "rectangle":
            # Get the length of the package
            pack_length_str = input("Enter the length (m): ")
            try:
                # Cast the length to a float
                pack_length_float = float(pack_length_str)
                # Get the width of the package
                pack_width_str = input("Enter the width (m): ")
                try:
                    # Cast the width to a float
                    pack_width_float = float(pack_width_str)
                    # Get the weight of the package
                    pack_weight_str = input("Enter the weight (kg): ")
                    try:
                        # Cast the weight to a float
                        pack_weight_float = float(pack_weight_str)
                        # Get the height of the package
                        pack_height_str = input("Enter the height (m): ")
                        try:
                            # Cast the height to a float
                            pack_height_float = float(pack_height_str)
                            # Check if all measurements are positive
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
                                    f"The volume of your package is: "
                                    f"{pack_volume:,.2f} m³"
                                )
                                # Check weight and volume eligibility
                                if (
                                    pack_weight_float > constants.MAX_WEIGHT
                                    or pack_volume > constants.MAX_VOLUME
                                ):
                                    # Check weight eligibility
                                    if pack_weight_float > constants.MAX_WEIGHT:
                                        print(
                                            "Your package is not acceptable "
                                            "because it is too heavy."
                                        )
                                    else:
                                        print(
                                            "Your package has an appropriate weight."
                                        )
                                    # Check volume eligibility
                                    if pack_volume > constants.MAX_VOLUME:
                                        print(
                                            "Your package is not acceptable "
                                            "because it is too voluminous."
                                        )
                                    else:
                                        print(
                                            "Your package has an appropriate volume."
                                        )
                                else:
                                    print("Your package is acceptable.")
                            else:
                                print(
                                    "Wrong input: All measurements must "
                                    "be greater than 0."
                                )
                        except ValueError:
                            print("The height of your package is invalid.")
                    except ValueError:
                        print("The weight of your package is invalid.")
                except ValueError:
                    print("The width of your package is invalid.")
            except ValueError:
                print("The length of your package is invalid.")
        case _:
            print(
                "Sorry, your package has to be in a rectangular shape."
            )
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
