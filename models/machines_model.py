# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MachinesModel(models.Model):
    _name = 'machines.model'
    _description = 'Model or Group of machines'

    name = fields.Char(string='Code')
    area = fields.Many2one(comodel_name='machines.area', string='Area')
