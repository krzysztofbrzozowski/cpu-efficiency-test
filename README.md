Sample test generated by GPT

## To run test natively
```
python -m venv venv
source venv/bin/activate
python cpu_efficiency_test.py
```

Saple output
```
Starting CPU efficiency test for 10 seconds using 4 processes...
Test completed in 10.02 seconds. 
Total operations completed: 11223                                                                        
CPU efficiency: 1120.31 operations per second.
```

## To run test in docker
```
docker build -t cpu-efficiency-test . && docker run --rm cpu-efficiency-test
```

Sample output
```
Starting CPU efficiency test for 10 seconds using 4 processes...
Test completed in 10.05 seconds.
Total operations completed: 17189
CPU efficiency: 1710.51 operations per second.
```