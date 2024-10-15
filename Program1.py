# Elijah Gertsch
# UWYO COSC 1010
# 10/14/2024
# HW 01
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here

# Homework Question:
# 
# You are given a list of dictionaries where each dictionary represents a student and their scores 
# in different subjects.
# 
# Student Data:
students = [
     {"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
     {"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
     {"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
     {"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
 ]

#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.

# Your task is to calculate the average scores for each student and print the names of students
# whose average score is greater than 80.

#Solution

alice_score = students[0]["scores"]
alice_ave = sum(alice_score.values())/len(alice_score)
bob_score = students[1]["scores"]
bob_ave = sum(bob_score.values())/len(alice_score)
charlie_score = students[2]["scores"]
charlie_ave = sum(charlie_score.values())/len(alice_score)
david_score = students[3]["scores"]
david_ave = sum(david_score.values())/len(alice_score)

averages = {}

averages['alice'] = alice_ave
averages['bob'] = bob_ave
averages['charlie'] = charlie_ave
averages['david'] = david_ave

for key in averages:
    if averages[key] > 80:
     print(key)