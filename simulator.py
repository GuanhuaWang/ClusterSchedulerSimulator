import numpy as np
import random as rd

def scheduler (J1,J2,J3): 
    J1_num, = J1.shape
    J2_num, = J2.shape
    J3_num, = J3.shape
    sched_round=J1_num+J2_num+J3_num
    
    rr=np.zeros(sched_round)
    rr_job=np.zeros(sched_round)
    
    j1_count=0
    j2_count=0
    j3_count=0
    i = 0
#Round Robin Queue
    for j in range (0,10):
        rr[i]=J1[j1_count]
        rr_job[i]=1
        i += 1
        j1_count += 1

        rr[i]=J2[j2_count]
        rr_job[i]=2
        i += 1
        j2_count += 1
        
        rr[i]=J3[j3_count]
        rr_job[i]=3
        i += 1
        j3_count += 1
    
    for j in range (10,20):      
        rr[i]=J2[j2_count]
        rr_job[i]=2
        i += 1
        j2_count += 1
        
        rr[i]=J3[j3_count]
        rr_job[i]=3
        i += 1
        j3_count += 1  
    for j in range (20,40):      
        rr[i]=J3[j3_count]
        rr_job[i]=3
        i += 1
        j3_count += 1
    
    return rr,rr_job

#assign Tasks
def FIFO(q,qj,num):
    worker=np.zeros((6,500))
    length, = q.shape
    q_flag=0
    # worker[0] is the task running on node 1, worker[1] is the task's job ID on node 1
    # worker[2] is the task running on node 2, worker[3] is the task's job ID on node 2
    # worker[4] is the task running on node 3, worker[5] is the task's job ID on node 3
    for i in range (0,500):
        if ((worker[0][i] ==0 and worker[2][i]==0 and worker[4][i]==0) and q_flag<length):
            c1 = int(q[q_flag])
            c1_job = int(qj[q_flag])
            q_flag += 1
            for j in range (0,c1):
                worker[0][i+j] = c1
                worker[1][i+j] = c1_job
            c2 = int(q[q_flag])
            c2_job = int(qj[q_flag])
            q_flag += 1
            for m in range (0,c2):
                worker[2][i+m] = c2
                worker[3][i+m] = c2_job
            c3 = int(q[q_flag])
            c3_job = int(qj[q_flag])
            q_flag += 1
            for n in range (0,c3):
                worker[4][i+n] = c3
                worker[5][i+n] = c3_job
        elif ((worker[0][i] ==0 and worker[2][i]==0) and q_flag<length):
            c1 = int(q[q_flag])
            c1_job = int(qj[q_flag])
            q_flag += 1
            for j in range (0,c1):
                worker[0][i+j] = c1
                worker[1][i+j] = c1_job
            c2 = int(q[q_flag])
            c2_job = int(qj[q_flag])
            q_flag += 1
            for m in range (0,c2):
                worker[2][i+m] = c2
                worker[3][i+m] = c2_job
        elif ((worker[0][i] ==0 and worker[4][i]==0) and q_flag<length):
            c1 = int(q[q_flag])
            c1_job = int(qj[q_flag])
            q_flag += 1
            for j in range (0,c1):
                worker[0][i+j] = c1
                worker[1][i+j] = c1_job
            c3 = int(q[q_flag])
            c3_job = int(qj[q_flag])
            q_flag += 1
            for n in range (0,c3):
                worker[4][i+n] = c3
                worker[5][i+n] = c3_job
        elif ((worker[2][i] ==0 and worker[4][i]==0) and q_flag<length):
            c2 = int(q[q_flag])
            c2_job = int(qj[q_flag])
            q_flag += 1
            for m in range (0,c2):
                worker[2][i+m] = c2
                worker[3][i+m] = c2_job
            c3 = int(q[q_flag])
            c3_job = int(qj[q_flag])
            q_flag += 1
            for n in range (0,c3):
                worker[4][i+n] = c3
                worker[5][i+n] = c3_job
        elif(worker[0][i] ==0 and q_flag<length):
            c1 = int(q[q_flag])
            c1_job = int(qj[q_flag])
            q_flag += 1
            for j in range (0,c1):
                worker[0][i+j] = c1
                worker[1][i+j] = c1_job
        elif(worker[2][i] ==0 and q_flag<length):
            c2 = int(q[q_flag])
            c2_job = int(qj[q_flag])
            q_flag += 1
            for m in range (0,c2):
                worker[2][i+m] = c2
                worker[3][i+m] = c2_job
        elif(worker[4][i] ==0 and q_flag<length):
            c3 = int(q[q_flag])
            c3_job = int(qj[q_flag])
            q_flag += 1
            for n in range (0,c3):
                worker[4][i+n] = c3
                worker[5][i+n] = c3_job
            
            
    np.savetxt('test.csv', worker, delimiter=',')
    #find when Job 1 finishes
    flag1=0
    x = 0
    while (flag1 != 1):
        if (worker[1][499-x] == 1 or worker[3][499-x] == 1 or worker[5][499-x] == 1):
            flag1 = 1
            print "job1 finishes at time %s" %(500-x)
        else:
            x += 1
    
    #find when Job 2 finishes
    flag2=0
    x2 = 0
    while (flag2 != 1):
        if (worker[1][499-x2] == 2 or worker[3][499-x2] == 2 or worker[5][499-x2] == 2):
            flag2 = 1
            print "job2 finishes at time %s" %(500-x2)
        else:
            x2 += 1
    #find when Job 3 finishes
    flag3=0
    x3 = 0
    while (flag3 != 1):
        if (worker[1][499-x3] == 3 or worker[3][499-x3] == 3 or worker[5][499-x3] == 3):
            flag3 = 1
            print "job2 finishes at time %s" %(500-x3)
        else:
            x3 += 1
        
            
        
            
    
    
def SJF(q,qj,num):
    print q
    print qj
    
job1 = np.zeros(10)
job2 = np.zeros(20)
job3 = np.zeros(40)

for i in range (0,10):
    job1[i] =rd.randint(1,9)
for i in range (0,20):
    job2[i] =rd.randint(1,9)
for i in range (0,40):
    job3[i] =rd.randint(1,9)
    
queue, queue_job = scheduler (job1,job2,job3)

q = [1,2,3,4,5,6,7,8,9]
q_job = [1,2,3,1,2,3,1,2,3]
FIFO(queue,queue_job,3)
#SJF(queue,queue_job,3)