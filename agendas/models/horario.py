# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HorarioAgendas(models.Model):
   _name = 'agendas.horario'

  
   name = fields.Char(string="Nombre", required=True)
   cost = fields.Float(string="Valor", required=True )
   hour= fields.Datetime(string="Fecha y Hora Designada")
   image = fields.Binary(string="Imagen")
   category = fields.Selection([
       ("tattoo", "Tattoo"),
       ("piercing", "Piercing"),
       ], string="Categoria", default="tattoo")
   assistance = fields.Boolean("Confirmar Asistencia") 
   description = fields.Text(string="Descripción",
                             default="Breve descripción sobre el servicio")
   status_pago = fields.Selection([
       ("pendiente", "Pendiente"),
       ("efectuado", "Efectuado"),
       ], string="Estado de pago", default="pendiente") 
   status_servicio = fields.Boolean("Estado del servicio")                          