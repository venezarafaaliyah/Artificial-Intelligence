# -*- coding: utf-8 -*-
"""AUAI assignment 1 - AUSP220496

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UDB9fwBEyjfSIoDMt5fx4lWhLe3i0FEh

# AUAI assigment 1
ID: AUSP220496
Name : Veneza Rafa Aliyah

## IPO-I: input
"""

scores=[]
fin=open('scoreIn.txt')
for line in fin:
  paras = line.split()
  id, s1, s2, s3 = paras
  scores.append([id, s1, s2, s3, 0.0])
fin.close()

"""## IPO-P: process"""

for score in scores:
  score[4] = int(score[1])*.3 + int(score[2])*.3 + int(score[3])*.4
  print(f"{score[0]} {score[1]} {score[2]} {score[3]} {score[4]:.1f}")

scores2 = sorted(scores, key = lambda scores: scores[4], reverse = True)

"""## IPO-O: output"""

fout = open('scoreOut.txt', 'w')
for score in scores2:
  print(f"{score[0]} {score[4]:.1f}", file=fout)
fout.close()