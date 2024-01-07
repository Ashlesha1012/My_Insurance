from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Policy(models.Model):
    policy_holder = models.ForeignKey(Client, on_delete=models.CASCADE)
    coverage_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    clients = models.ManyToManyField(Client, related_name='policies', blank=True)

    def __str__(self):
        return f"{self.policy_holder.name}'s Policy"
    
class Claim(models.Model):
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Claim for {self.policy} - {self.status}"