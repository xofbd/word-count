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

## License
This project is distributed under the MIT license. Please see `LICENSE` for more information.
