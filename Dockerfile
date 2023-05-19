FROM apache/spark-py:v3.1.3

ENV PATH=/opt/spark/bin:"$PATH"
COPY src src
COPY tests/ src/tests

CMD ["spark-submit", "--master", "local[*]", "--py-files", "src/utils.py", "src/word_count.py", "src/tests"]
