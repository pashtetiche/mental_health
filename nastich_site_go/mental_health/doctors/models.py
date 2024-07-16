from django.db import models

class Doctor(models.Model):
    SPECIALIST_TYPE_CHOICES = [
        ('PSI1', 'Психолог'),
        ('PSI2', 'Психотерапевт'),
        ('PSI3', 'Психіатр'),
        ('DEF', 'Default')
    ]

    RECEPTION_TYPE_CHOICES = [
        ('ON', 'Онлайн'),
        ('OFF', 'Оффлайн'),
        ('BTH', 'Обидва')
    ]

    RECIPE_CHOICES = [
        ('STEM', 'Так, стимулятори'),
        ('NSTEM', 'Так, нестимулятори'),
        ('NO', 'Ні'),
    ]

    name = models.CharField(max_length=100)
    #specialty = models.CharField(max_length=100)
    #city = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    description = models.TextField()
    approved = models.BooleanField(default=False)

    specialty = models.CharField(max_length=100, choices=SPECIALIST_TYPE_CHOICES, default='DEF')
    city = models.CharField(max_length=255, default='Kyiv')
    reception_type = models.CharField(max_length=100, choices=RECEPTION_TYPE_CHOICES, default='ON')
    is_diagnostics = models.BooleanField(default=False)
    is_icd_diagnosis = models.BooleanField(default=False)
    medical_conclusion = models.BooleanField(default=False)
    recipe = models.CharField(max_length=100, choices=RECIPE_CHOICES, default='NO')
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Questionnaire(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Questionnaire for {self.doctor.name}"

class Review(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.doctor.name}"

class Recommendation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Recommendation for {self.doctor.name}"