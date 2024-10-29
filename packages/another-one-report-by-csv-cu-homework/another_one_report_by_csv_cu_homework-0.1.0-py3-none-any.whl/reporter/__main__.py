import reporter
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="calculate_business")

    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--output-file", type=str)

    args = parser.parse_args()

    report = reporter.get_report(args.input_file)
    print(report)
    if args.output_file:
        reporter.save_report(report, args.output_file)