#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function

from pyspark import SparkContext
from pyspark.sql import SQLContext
import numpy as np
from pyspark.mllib.linalg import Vectors
# $example on$
from pyspark.mllib.random import RandomRDDs
# $example off$

if __name__ == "__main__":
    sc = SparkContext(appName="RandomDataGenerationExample") # SparkContext
    sqlContext = SQLContext(sc)

    # $example on$
    # Generate a random double RDD that contains 1 million i.i.d. values drawn from the
    # standard normal distribution `N(0, 1)`, evenly distributed in 10 partitions.
    u = RandomRDDs.normalRDD(sc, 1000L, 10)
    # Apply a transform to get a random double RDD following `N(1, 4)`.
    v = u.map(lambda x: 1.0 + 2.0 * x)
    # $example off$

    for each in u.collect():
        print(each)

    for each in v.collect():
        print(each)

    sc.stop()