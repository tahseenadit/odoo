# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class Phonedirectory(models.Model):
    """Create and save phone directory"""

    _name = 'phone_directory.phonedirectory'

    firstname = fields.Char(string="First Name")
    lastname = fields.Char(string="Last Name")
    phone = fields.Char(string="Telephone")
    mobile = fields.Char(string="Mobile")
    company = fields.Char(string="Company")
    address = fields.Char(string="Address")
    country = fields.Char(string="Country")
    city = fields.Char(string="City")

    # @api.model
    # def create(self, vals):
    #
    #     if vals.get('id', 'New') == 'New':
    #         vals['id'] = self.env['ir.sequence'].next_by_code('phone_directory.id') or '/'
    #     return super(Phonedirectory, self).create(vals)
    #
    # @api.model
    # def save(self, vals):
    #
    #     if vals.get('id', 'New') == 'New':
    #         vals['id'] = self.env['ir.sequence'].next_by_code('phone_directory.id') or '/'
    #     return super(Phonedirectory, self).save(vals)
