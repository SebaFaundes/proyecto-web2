# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TattoosCatalogo(models.Model):
   _name = 'catalogo.tattoos'

  
   name = fields.Char(string="Nombre", required=True)
   cost = fields.Float(string="Valor", required=True )
   stock = fields.Integer(string="Cantidad")
   image = fields.Binary(string="Imagen")
   category = fields.Selection([
       ("tattoo", "Tattoo"),
       ("piercing", "Piercing"),
       ], string="Categoria", default="tattoo")
   description = fields.Text(string="Descripción",
                             default="Breve descripción del producto")    
  