import time
 
def MeasureTime(func):
    def wrapper(*args, **kwargs):
        print("Start measuring time.")
        start = time.perf_counter()
        rval = func(*args, **kwargs)
        end = time.perf_counter()
        result = int((end-start)*1000)
        print(f"Stop measuring time. Elapsed time: {result}ms")
        return rval
    return wrapper

class ETL:
    def __init__(self, fileName = "latest.txt"):
        self.fileName = fileName

    def read(self):
        with open(self.fileName, "r") as f:
            for line in f:
                yield line.strip()

    def transform(self):
        for line in self.read():
            values = [float(val) for val in line.split(",") if val != '-']
            miss = [ind for ind, val in enumerate(line.split(",")) if val == '-']
            ind = int(values[0])
            val = values[1:]
            acu = sum(val)
            avg = acu/(len(val))
            yield ind, acu, avg, miss
    
    def save(self):
        with open("values.csv", "w") as valFile, open("missing_values.csv", "w") as missFile:
            for ind, acu, avg, miss in self.transform():
                valFile.write(f"{ind},{acu},{avg}\n")
                if miss:
                    missFile.write(f"{ind},{','.join(map(str, miss))}\n")
    @MeasureTime
    def run(self):
        self.save()