#!/bin/bash

echo "Running tests..."

# Test 1: if simulate.py runs without errors
python3 src/simulate.py > test_output.log 
if [ $? -ne 0 ]; then
    echo "Test failed: simulate.py did not run successfully"
    exit 1
fi

echo "Test 1 passed: simulate.py runs successfully."

cat test_output.log

# Test 2: Check if output files are created
touch results_N10.log results_N40.log results_N4000.log
rm results_N10.log results_N40.log results_N4000.log
python3 src/simulate.py --iterations 10 --N 10
python3 src/simulate.py --iterations 10 --N 40
python3 src/simulate.py --iterations 10 --N 4000


if [ ! -f "results_N10.log" ] || [ ! -s "results_N10.log" ]; then
    echo "Test failed: results_N10.log was not created or is empty"
    exit 1
fi
if [ ! -f "results_N40.log" ] || [ ! -s "results_N40.log" ]; then
    echo "Test failed: results_N40.log was not created or is empty"
    exit 1
fi
if [ ! -f "results_N4000.log" ] || [ ! -s "results_N4000.log" ]; then
    echo "Test failed: results_N4000.log was not created or is empty"
    exit 1
fi

echo "Test 2 passed: All output files were created successfully."

echo "All tests passed!"
