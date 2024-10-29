import customer_analysis
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--output-file", type=str, required=True)

    args = parser.parse_args()

    customer_analysis.generate_report(args.input_file, args.output_file)
