# PySpark Word Counting
A simple Spark application for counting words.

## Usage
Run `src/word_count.py --help`. Here's what you should see:
```console
usage: word_count.py [-h] [-o OUTPUT_DIR] input_dir

Calculate word frequency for a set of files.

positional arguments:
  input_dir             Path of files to calculate word frequencies.

options:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output OUTPUT_DIR
                        Directory to save results, defaults to STDOUT.
```

You should run the application with `spark-submit`, e.g.:
```console
spark-submit --master local[*] --py-files src/utils.py src/word_count.py src/tests
```

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
