# Lab 2: Hadoop Streaming Log Analysis

Process web-server logs with Python mapper and reducer programs on a Hadoop cluster.

## How It Works

The mapper extracts an hour and IP address from each matching log record and emits tab-separated counts. A second mapper filters records to a requested hour range. The reducer groups counts by hour and IP and supports a top-K argument. The submitted report also records master/worker cluster configuration.

## Main Tasks

- Extract timestamps and addresses from log lines.
- Optionally filter by the start-inclusive and end-exclusive hour range.
- Aggregate mapped counts and inspect the selected results.

## Files

- [reduce_stage.py](reduce_stage.py): Python implementation or analysis script.
- [ECC_Lab2/map_stage_stat1.py](ECC_Lab2/map_stage_stat1.py): Python implementation or analysis script.
- [ECC_Lab2/map_stage_stat2.py](ECC_Lab2/map_stage_stat2.py): Python implementation or analysis script.
- [ECC_Lab2/reduce_stage_stat1_stat2.py](ECC_Lab2/reduce_stage_stat1_stat2.py): Python implementation or analysis script.
- [ECC_Lab2/Aryan_Shivali_ECC_Lab_2.pdf](ECC_Lab2/Aryan_Shivali_ECC_Lab_2.pdf): assignment instructions or submitted report in PDF format.
- [ECC_Lab2/README.pdf](ECC_Lab2/README.pdf): assignment instructions or submitted report in PDF format.
- [ECC_Lab2/Certificate of Pair Programming.txt](ECC_Lab2/Certificate%20of%20Pair%20Programming.txt): supporting lab file.
- [hadoop-streaming-3.4.0.jar](hadoop-streaming-3.4.0.jar): Hadoop Streaming support library.
- [sample.log](sample.log): supporting lab file.
- [sample1.log](sample1.log): supporting lab file.

## Local Mapper and Reducer Usage

From `Lab2`, Python can run the scripts on the included log without starting Hadoop:

```bash
python ECC_Lab2/map_stage_stat1.py < sample.log | python ECC_Lab2/reduce_stage_stat1_stat2.py 10
python ECC_Lab2/map_stage_stat2.py 13-14 < sample.log | python ECC_Lab2/reduce_stage_stat1_stat2.py 10
```

The first command counts IP occurrences by hour and selects up to ten entries per hour. The second restricts input records to hours from 13 inclusive to 14 exclusive before aggregation. The mapper and reducer communicate through tab-separated lines.
