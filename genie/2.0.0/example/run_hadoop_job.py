#!/usr/bin/python2.7

# Copyright 2014 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#######################################################################################################################
# This script assumes setup.py has already been run to configure Genie and that this script is executed on the host
# where Genie is running. If it's executed on another host change the localhost line below.
#######################################################################################################################

import genie2.client.wrapper
import genie2.model.ClusterCriteria
import genie2.model.Job
import genie2.model.FileAttachment
import time

# Create a Genie client which proxies API calls through wrapper which retries failures based on various return codes
genie = genie2.client.wrapper.Genie2("http://localhost:8080/genie",
                                     genie2.client.wrapper.RetryPolicy(
                                         tries=8, none_on_404=True, no_retry_http_codes=range(400, 500)
                                     ))

# Create a job instance and fill in the required parameters
job = genie2.model.Job.Job()
job.name = "GenieDockerExampleHadoopJob"
job.user = "root"
job.version = "0.0.1"

# Create a list of cluster criterias which determine the cluster to run the job on
job.clusterCriterias = list()
cluster_criteria = genie2.model.ClusterCriteria.ClusterCriteria()
criteria = set()
criteria.add("prod")
criteria.add("yarn")
cluster_criteria.tags = criteria
job.clusterCriterias.append(cluster_criteria)

# Create the set of command criteria which will determine what command Genie executes for the job
command_criteria = set()
command_criteria.add("hadoop")
job.commandCriteria = command_criteria

# Any command line arguments to run along with the command. In this case it holds the actual query but this
# could also be done via an attachment or file dependency.
# This jar location is where it is installed on the Genie node but could also pass the jar as attachment and use
# it locally
job.commandArgs = \
    "jar /apps/hadoop/2.6.0/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar grep input output 'dfs[a-z.]+'"

# Submit the job to Genie
job = genie.submitJob(job)

while job.status != "SUCCEEDED" and job.status != "KILLED" and job.status != "FAILED":
    print "Job " + job.id + " is " + job.status
    time.sleep(10)
    job = genie.getJob(job.id)

print "Job " + job.id + " finished with status " + job.status