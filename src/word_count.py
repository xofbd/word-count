from argparse import ArgumentParser
from pyspark import SparkConf, SparkContext
from utils import filter, preprocess


conf = SparkConf()
conf.setAppName("word_count")
sc = SparkContext(conf=conf)
sc.setLogLevel("WARN")


def count_words(input_dir, output_dir):
    result = (
        sc.textFile(input_dir)
        .flatMap(lambda line: line.split())
        .map(preprocess)
        .filter(filter)
        .map(lambda word: (word, 1))
        .reduceByKey(lambda acc, val: acc + val)
        .sortBy(lambda x: x[1], ascending=False)
    )

    if output_dir is None:
        for row in result.collect():
            print(row)
    else:
        result.saveAsTextFile(output_dir)


def parse_args():
    parser = ArgumentParser(
        description="Calculate word frequency for a set of files."
    )
    parser.add_argument(
        "input_dir",
        help="Path of files to calculate word frequencies.",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_dir",
        help="Directory to save results, defaults to STDOUT.",
        default=None,
        type=str
    )

    return parser.parse_args()


def main():
    args = parse_args()
    count_words(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
