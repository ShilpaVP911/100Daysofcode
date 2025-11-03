class student:
    score=[65,75,85,95]
    def avg(self):
        return sum(self.score)/len(self.score)
s1=student()
print("Average score:",s1.avg())