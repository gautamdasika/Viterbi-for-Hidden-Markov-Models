

prior={'s1':0.125,'s2':0.125,'s3':0.125,'s4':0.125,'s5':0.125,'s6':0.125,'s7':0.125,'s8':0.125,}
obs="1511623541265341625343132532112112316314316315211231113121313131221324231421456241241261"
obs_prob={}
obs_prob['s1']=obs_prob['s2']=obs_prob['s3']=obs_prob['s4']={'1':0.16666,'2':0.16666,'3':0.16666,'4':0.16666,'5':0.16666,'6':0.16666}
obs_prob['s8']=obs_prob['s5']=obs_prob['s6']=obs_prob['s7']={'1':0.05,'2':0.125,'3':0.125,'4':0.125,'5':0.125,'6':0.45}
trans_prob={}
trans_prob['s1']={'s1':0,'s2':1,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0}
trans_prob['s2']={'s1':0,'s2':0,'s3':1,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0}
trans_prob['s3']={'s1':0,'s2':0,'s3':0,'s4':1,'s5':0,'s6':0,'s7':0,'s8':0}
trans_prob['s4']={'s1':0.75,'s2':0,'s3':0,'s4':0,'s5':0.25,'s6':0,'s7':0,'s8':0}
trans_prob['s5']={'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':1,'s7':0,'s8':0}
trans_prob['s6']={'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':1,'s8':0}
trans_prob['s7']={'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':1}
trans_prob['s8']={'s1':0.25,'s2':0,'s3':0,'s4':0,'s5':0.75,'s6':0,'s7':0,'s8':0}


delta={}
delta1={}
psi={}
psi[1]={}
for s in prior.keys():
  delta[s]=prior[s]*obs_prob[s][obs[0]]
  psi[1][s]=0
print("delta at 1:")
print(delta)
print("psi at 1:")
print(psi[1])
j=1
for i in obs[1:]:
  j+=1
  psi[j]={}
  print("Delta at "+str(j))
  for s in prior.keys():
    delta1[s]=0
    for r in prior.keys():
      cur=delta[r]*trans_prob[r][s]*obs_prob[s][i]
      if cur>delta1[s]:
        delta1[s]=cur
        psi[j][s]=r
  for s in prior.keys():
    delta[s]=delta1[s]
  print(delta)
  print ("psi at"+str(j))
  print (psi[j])
maximum = max(delta, key=delta.get)
print(maximum)
while(j>0):
  print(psi[j][maximum])
  maximum=psi[j][maximum]
  j-=1
  






