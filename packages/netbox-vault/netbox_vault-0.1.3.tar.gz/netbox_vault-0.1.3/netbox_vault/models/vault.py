from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from dcim.models import Device
from django.urls import reverse
import requests
from django.core.exceptions import ValidationError

class Vault(NetBoxModel):
	PrsID = models.IntegerField()
	device = models.OneToOneField(Device, on_delete=models.CASCADE, related_name='vault')

	def save(self, *args, **kwargs):
		device = self.get_device()
		if device is None:
			raise ValidationError(f"No device found with PrsID: {self.PrsID}")
		self.device = device
		super().save(*args, **kwargs)

	def get_device(self):
		try:
			return Device.objects.get(custom_field_data__PrsID=str(self.PrsID))
		except Device.DoesNotExist:
			return None

	class Meta:
		ordering = ('pk',)

	def __str__(self):
		return str(self.PrsID)

	def get_absolute_url(self):
		return reverse('plugins:netbox_vault:vault', args=[self.pk])
