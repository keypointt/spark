/*
* Licensed to the Apache Software Foundation (ASF) under one or more
* contributor license agreements.  See the NOTICE file distributed with
* this work for additional information regarding copyright ownership.
* The ASF licenses this file to You under the Apache License, Version 2.0
* (the "License"); you may not use this file except in compliance with
* the License.  You may obtain a copy of the License at
*
*    http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package org.apache.spark.sql.sources

import org.apache.spark.SparkFunSuite
import org.apache.spark.sql._
import org.apache.spark.sql.internal.SQLConf

private[sql] class DataSourceSuite extends SparkFunSuite {

  test("test parquet") {

    val spark = SparkSession
      .builder
      .appName("Spark Examples")
      .master("local[4]")
//      .config("spark.some.config.option", "some-value")
      .getOrCreate()

    var df = spark.read
      .load("/Users/quickmobile/workspace/spark/examples/src/main/resources/users.parquet")
//    val df2 = spark.read.format("json").load("examples/src/main/resources/people.json")

    assert(df.isInstanceOf[DataFrame])
  }
}
