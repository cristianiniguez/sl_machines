# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MachinesModel(models.Model):
    _name = 'machines.model'
    _description = 'Model or Group of machines'

    name = fields.Char(string='Code')
    area_id = fields.Many2one(comodel_name='machines.area', string='Area')

    machine_ids = fields.One2many(
        comodel_name='machines.machine', inverse_name='model_id', string='Machines')
