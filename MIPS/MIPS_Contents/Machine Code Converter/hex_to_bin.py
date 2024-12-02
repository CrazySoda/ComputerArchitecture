def convert_hex_file_to_binary(input_file, output_file):
    """
    Converts space-separated hexadecimal codes in a file to 20-bit binary codes
    and saves the results into another file.

    Args:
        input_file (str): Path to the input file containing hex codes.
        output_file (str): Path to the output file to save 20-bit binary codes.
    """
    try:
        with open(input_file, 'r') as infile:
            data = infile.read().strip()  # Read and strip extra spaces/newlines

        # Split the space-separated hex codes
        hex_codes = data.split()

        # Convert each hex code to 20-bit binary
        binary_codes = []
        for hex_code in hex_codes:
            try:
                binary_code = bin(int(hex_code, 16))[2:].zfill(20)
                binary_codes.append(binary_code)
            except ValueError:
                binary_codes.append(f"Invalid Hex: {hex_code}")

        # Write the 20-bit binary codes to the output file
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(binary_codes))

        print(f"Conversion successful! Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
input_file = input("Enter the path to the input file: ").strip()
output_file = input("Enter the path to the output file: ").strip()
convert_hex_file_to_binary(input_file, output_file)
