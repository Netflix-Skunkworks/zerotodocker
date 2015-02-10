#!/usr/bin/python2.7

import genie2.client.wrapper
import genie2.model.Command
import genie2.model.Cluster

# Create a Genie client which proxies API calls through wrapper which retries failures based on various return codes
genie = genie2.client.wrapper.Genie2("http://localhost:8080/genie",
                                     genie2.client.wrapper.RetryPolicy(
                                         tries=8, none_on_404=True, no_retry_http_codes=range(400, 500)
                                     ))

commands = list()

# Create a new command instance and set the required fields
hadoop_command = genie2.model.Command.Command()
hadoop_command.name = "hadoop"
hadoop_command.user = "root"
hadoop_command.version = "2.6.0"
hadoop_command.jobType = "hadoop"
hadoop_command.tags = list()
hadoop_command.tags.append("hadoop")
hadoop_command.tags.append("mr2")
hadoop_command.status = "ACTIVE"
hadoop_command.executable = "/apps/hadoop/2.6.0/bin/hadoop"

# Could set command id here or let it be set automatically
# cmd.id = "hadoop240"

hadoop_command = genie.createCommand(hadoop_command)

commands.append(hadoop_command)

# Create a new command instance and set the required fields
pig_command = genie2.model.Command.Command()
pig_command.name = "pig"
pig_command.user = "root"
pig_command.version = "0.14.0"
pig_command.jobType = "pig"
pig_command.tags = list()
pig_command.tags.append("pig")
pig_command.tags.append("0.14.0")
pig_command.tags.append("mr2")
pig_command.status = "ACTIVE"
pig_command.executable = "/apps/pig/0.14.0/bin/pig"

# Could set command id here or let it be set automatically
# cmd.id = "hadoop240"

pig_command = genie.createCommand(pig_command)

commands.append(pig_command)

cluster = genie2.model.Cluster.Cluster()
cluster.name = "h2prod"
cluster.version = "2.6.0"
cluster.user = "root"
cluster.status = "UP"
cluster.clusterType = "yarn"
cluster.tags = list()
cluster.tags.append("prod")
cluster.tags.append("yarn")
cluster.tags.append("sla")
cluster.configs = list()
cluster.configs.append("file:///apps/genie/hadoop/2.6.0/conf/core-site.xml")
cluster.configs.append("file:///apps/genie/hadoop/2.6.0/conf/mapred-site.xml")
cluster.configs.append("file:///apps/genie/hadoop/2.6.0/conf/yarn-site.xml")

# Could set cluster id here or let it be set automatically
# cluster.id = "h2prod"

cluster = genie.createCluster(cluster)

# Add the commands to the cluster
commands = genie.addCommandsForCluster(cluster.id, commands)
