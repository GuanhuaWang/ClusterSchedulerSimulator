# Cluster Scheduler Simulator (CSS)
[![Build Status](https://travis-ci.org/GuanhuaWang/ClusterSchedulerSimulator.svg?branch=master)](https://travis-ci.org/GuanhuaWang/ClusterSchedulerSimulator)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](LICENSE)

Cluster Scheduler Simulator (CSS) is a cluster scheduling simulator used for design new scheduling alogrithm in big data analytics cluster.
## Current stage
We generate  `job Queue` and `task Queue` here. Each task has its own processing time. The random generated  `task Queue` are mappting to different `job Queue` for scheduling. We use common matrics like Job Completion time (JCT), Fairness, etc to evaluate the scheduler performance.

We designed `Random Taks Queue Generator` with *varied* task processing time (estimited)

We developed `FIFO` (First In First Out) task scheduler with RoundRobin task choise among all the active jobs.

We developed `SRTF` (Shortest Remaining Time First) task scheduler, which achieves pretty good JCT. It is worth noting that this `SRTF` is *NOT* scheduled in a preemptive way.
