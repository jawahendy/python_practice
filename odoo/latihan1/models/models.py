# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields

# class latihan1(models.Model):
#     _name = 'latihan1.latihan1'
#     _description = 'latihan1.latihan1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string="Name")
    horse_power = fields.Integer(string='Horse Power')
    door_number = fields.Integer(string='Doors Number')

    # driver_id = fields.Many2one('res.partner',string='Driver ID')
    # parking_id = fields.Many2one('parking.parking', string='parking')

# class Parking(models.Model):
#     _name= 'parking.parking'
#     name = fields.Char(string='Name')
#     car_ids = fields.One2many('car.car', 'parking_id', string='Cars')
