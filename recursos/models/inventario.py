# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Inventario(models.Model):
     _name = 'recursos.inventario'

     image = fields.Binary(string="Imágen")
     name = fields.Char(string="Nombre", required=True)
     description = fields.Text(string="Descripción")
     date = fields.Date("Fecha de adquisición")

     proveedor_id = fields.Many2one('recursos.proveedor', string="Proveedor")

     categoria_id = fields.Many2one('recursos.categoria', string="Categoría de Recurso")


class CategoriaRecurso(models.Model):
     _name = 'recursos.categoria'

     name = fields.Char(string="Nombre", required=True)

     inventario_cat_ids = fields.One2many('recursos.inventario', 'categoria_id', string="Inventario")

     total_categoria = fields.Integer(string="Total de Recursos", compute="_total_categoria")

     @api.one
     def _total_categoria(self):
          self.total_categoria = len(self.inventario_cat_ids)


     


class Proveedor(models.Model):
     _name = 'recursos.proveedor'

     name = fields.Char(string="Nombre", required=True)

     inventario_prov_ids = fields.One2many('recursos.inventario', 'proveedor_id', string="Inventario")

     description = fields.Text(string="Descripción")
     address = fields.Text(string="Dirección")
     phone = fields.Integer(string="Teléfono")
     mail = fields.Text(string="Correo")
     
     total_proveedor = fields.Integer(string="Total de Recursos", compute="_total_proveedor")

     @api.one
     def _total_proveedor(self):
          self.total_proveedor = len(self.inventario_prov_ids)
