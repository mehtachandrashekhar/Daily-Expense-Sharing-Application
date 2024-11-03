from django.db import models

class User(models.Model):
    objects = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Expense(models.Model):
    objects = None
    METHODS = [('equal', 'Equal'), ('exact', 'Exact'), ('percentage', 'Percentage')]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=10, choices=METHODS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    participants = models.ManyToManyField(User, related_name='expenses')
    exact_amounts = models.JSONField(blank=True, null=True)
    percentage_amounts = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} - {self.amount} - {self.method}"
